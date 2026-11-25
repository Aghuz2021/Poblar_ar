from datetime import datetime
import json
import os
import tkinter as tk
from tkinter import filedialog

from IPython.display import display, FileLink
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from tabulate import tabulate

from Conexion.cargar_datos import cargar_csv_con_pandas
from Limpieza.limpieza import limpiar_tipos_dataset

df = cargar_csv_con_pandas()
df = limpiar_tipos_dataset(df)


def ver_informacion_general(df):
    """
    Muestra los tipos de datos y columnas del DataFrame.
    """
    print("📊 INFORMACIÓN TIPOS DE DATOS")
    print("\n2. Tipos de datos y columnas:")
    print(df.dtypes)


def Cantidad_Provincias_Unicas(df):
    """
    Filtra por Tipo de jurisdicción == 'Provincia', cuenta la cantidad única de registros
    y muestra el resultado con un formato visual ordenado.
    """
    try:
        cantidad_unica = df.query("`Tipo de jurisdicción` in ['Provincia']")[
            "Nombre"
        ].nunique()

        resultado = pd.DataFrame({
            "Tipo de jurisdicción": [
                "Provincia",
            ],
            "Cantidad Única": [f"{int(cantidad_unica):,}".replace(",", ".")],
        })

        print(
            tabulate(
                resultado.values.tolist(),
                headers=["Tipo de jurisdicción", "Cantidad Única"],
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )
        return resultado
    except Exception as e:
        print(f"[Error en Cantidad_Provincias_Unicas]: {e}")


def Total_Habitantes_Provincia(df):
    """
    Filtra por Provincia, agrupa por Nombre, suma los habitantes,
    y muestra la tabla completa con un formato visual ordenado.
    """
    df["Total habitantes"] = pd.to_numeric(
        df["Total habitantes"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False),
        errors="coerce",
    )
    try:
        resultado = (
            df.query("`Tipo de jurisdicción` == 'Provincia'")
            .groupby("Nombre")["Total habitantes"]
            .sum()
            .reset_index()
            .sort_values(by="Total habitantes", ascending=False)
        )
        resultado["Total habitantes"] = resultado["Total habitantes"].apply(
            lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
        )
        print(
            tabulate(
                resultado,
                headers=["Provincia", "Total Habitantes"],
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )
        return resultado
    except Exception as e:
        print(f"[Error en Total_Habitantes_Provincia]: {e}")


def Habitantes_Por_Provincia(df, Provincia):
    """
    Filtra por Provincia, toma como parámetro el nombre de la provincia,
    agrupa por Nombre, suma los habitantes y muestra la tabla ordenada.
    """
    try:
        resultado = (
            df.query(
                "`Tipo de jurisdicción` == 'Provincia' and Nombre == @Provincia"
            )
            .groupby("Nombre")["Total habitantes"]
            .sum()
            .reset_index()
            .sort_values(by="Total habitantes", ascending=False)
        )
        resultado["Total habitantes"] = resultado["Total habitantes"].apply(
            lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
        )
        print(
            tabulate(
                resultado,
                headers=["Provincia", "Total Habitantes"],
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )
        return resultado
    except Exception as e:
        print(f"[Error en Habitantes_Por_Provincia]: {e}")


def count_Habitantes_Provincia(df):
    """
    Suma la cantidad total de habitantes de las provincias y muestra el resultado en una tabla.
    """
    df["Total habitantes"] = pd.to_numeric(
        df["Total habitantes"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False),
        errors="coerce",
    )
    try:
        total_valor = df.query("`Tipo de jurisdicción` in ['Provincia','Jurisdicción autónoma']")[
            "Total habitantes"
        ].sum()

        total_formateado = (
            f"{int(total_valor):,}".replace(",", ".")
            if pd.notnull(total_valor)
            else ""
        )

        resultado = pd.DataFrame({
            "Indicador": ["Total Habitantes"],
            "Total Habitantes": [total_formateado],
        })

        print(
            tabulate(
                resultado,  # type: ignore
                headers="keys",
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )

    except Exception as e:
        print(f"[Error en count_Habitantes_Provincia]: {e}")



def Estadisticas_Habitantes_Provincia(df):
    """
    Filtra por Provincia, agrupa por Nombre para sumar los habitantes de cada provincia,
    calcula cantidad, promedio, mínimo, máximo y mediana, y muestra la tabla ordenada.
    """
    try:
        datos = df.copy()
        datos["Total habitantes"] = pd.to_numeric(
            datos["Total habitantes"]
            .astype(str)
            .str.replace(r"\.0$", "", regex=True)
            .str.replace(".", "", regex=False)
            .str.replace(",", "", regex=False),
            errors="coerce",
        )

        por_provincia = (
            datos.query("`Tipo de jurisdicción` == 'Provincia'")
            .groupby("Nombre")["Total habitantes"]
            .sum()
        )

        cantidad = int(por_provincia.count())
        promedio = por_provincia.mean()
        minimo = por_provincia.min()
        maximo = por_provincia.max()
        mediana = por_provincia.median()

        def formatear(valor, decimales=False):
            if pd.isnull(valor):
                return ""
            if decimales:
                return (
                    f"{valor:,.2f}".replace(",", "X")
                    .replace(".", ",")
                    .replace("X", ".")
                )
            return f"{int(round(valor)):,}".replace(",", ".")

        resultado = pd.DataFrame({
            "Métrica": [
                "Cantidad de Provincias",
                "Promedio de Habitantes",
                "Mínimo de Habitantes",
                "Máximo de Habitantes",
                "Mediana de Habitantes",
            ],
            "Valor": [
                formatear(cantidad),
                formatear(promedio, decimales=False),
                formatear(minimo),
                formatear(maximo),
                formatear(mediana, decimales=False),
            ],
        })

        print(
            tabulate(
                resultado.values.tolist(),
                headers=["Métrica", "Valor"],
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )
        return resultado

    except Exception as e:
        print(f"[Error en Estadisticas_Habitantes_Provincia]: {e}")


def Total_Varon_Provincia(df):
    """
    Filtra por Provincia, agrupa por Nombre, suma varones/masculinos,
    y muestra la tabla completa con un formato visual ordenado.
    """
    df["Varon/Masculino"] = pd.to_numeric(
        df["Varon/Masculino"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False),
        errors="coerce",
    )
    try:
        resultado = (
            df.query("`Tipo de jurisdicción` == 'Provincia'")
            .groupby("Nombre")["Varon/Masculino"]
            .sum()
            .reset_index()
            .sort_values(by="Varon/Masculino", ascending=False)
        )
        resultado["Varon/Masculino"] = resultado["Varon/Masculino"].apply(
            lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
        )
        print(
            tabulate(
                resultado,
                headers=["Provincia", "Varon/Masculino"],
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )
    except Exception as e:
        print(f"[Error en Total_Varon_Provincia]: {e}")


def Total_Mujer_Provincia(df):
    """
    Filtra por Provincia, agrupa por Nombre, suma mujeres/femeninos,
    y muestra la tabla completa con un formato visual ordenado.
    """
    df["Mujer/Femenino"] = pd.to_numeric(
        df["Mujer/Femenino"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False),
        errors="coerce",
    )
    try:
        resultado = (
            df.query("`Tipo de jurisdicción` == 'Provincia'")
            .groupby("Nombre")["Mujer/Femenino"]
            .sum()
            .reset_index()
            .sort_values(by="Mujer/Femenino", ascending=False)
        )
        resultado["Mujer/Femenino"] = resultado["Mujer/Femenino"].apply(
            lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
        )
        print(
            tabulate(
                resultado,
                headers=["Provincia", "Mujer/Femenino"],
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )
    except Exception as e:
        print(f"[Error en Total_Mujer_Provincia]: {e}")


def Graficar_Top10_Provincias(df):
    """
    Filtra por Tipo de jurisdicción == 'Provincia', agrupa por Nombre,
    toma el Top 10 por habitantes y muestra un gráfico de barras horizontales.
    """
    try:
        datos = df.copy()
        datos["Total habitantes"] = pd.to_numeric(
            datos["Total habitantes"]
            .astype(str)
            .str.replace(r"\.0$", "", regex=True)
            .str.replace(".", "", regex=False)
            .str.replace(",", "", regex=False),
            errors="coerce",
        )

        top10 = (
            datos.query("`Tipo de jurisdicción` == 'Provincia'")
            .groupby("Nombre")["Total habitantes"]
            .sum()
            .reset_index()
            .sort_values(by="Total habitantes", ascending=False)
            .head(10)
        )

        # Invertimos el orden para que el #1 aparezca arriba
        top10 = top10.iloc[::-1]

        fig, ax = plt.subplots(figsize=(10, 6))
        barras = ax.barh(
            top10["Nombre"], top10["Total habitantes"], color="#1f77b4"
        )

        ax.set_title(
            "Top 10 Provincias de Argentina por Total de Habitantes",
            fontsize=12,
            fontweight="bold",
            pad=12,
        )
        ax.set_xlabel("Total de Habitantes")
        ax.set_ylabel("Provincia")

        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(
                lambda x, pos: f"{int(x):,}".replace(",", ".")
            )
        )

        for barra in barras:
            ancho = barra.get_width()
            ax.text(
                ancho,
                barra.get_y() + barra.get_height() / 2,
                f" {int(ancho):,}".replace(",", "."),
                va="center",
                ha="left",
                fontsize=9,
            )

        ax.set_xlim(0, top10["Total habitantes"].max() * 1.16)
        ax.grid(axis="x", linestyle="--", alpha=0.5)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"[Error en Graficar_Top10_Provincias]: {e}")


def Graficar_Distribucion_Genero_Provincias(df):
    try:
        datos = df.query("`Tipo de jurisdicción` == 'Provincia'").copy()

        for col in ["Varon/Masculino", "Mujer/Femenino"]:
            datos[col] = pd.to_numeric(
                datos[col]
                .astype(str)
                .str.replace(r"\.0$", "", regex=True)
                .str.replace(".", "", regex=False)
                .str.replace(",", "", regex=False),
                errors="coerce",
            )

        total_varones = int(datos["Varon/Masculino"].sum())
        total_mujeres = int(datos["Mujer/Femenino"].sum())
        total_general = total_varones + total_mujeres

        if total_general == 0:
            print("No hay datos numéricos válidos para graficar.")
            return None

        pct_varones = (total_varones / total_general) * 100
        pct_mujeres = (total_mujeres / total_general) * 100

        resultado = pd.DataFrame({
            "Género": ["Varón / Masculino", "Mujer / Femenino", "Total"],
            "Cantidad": [
                f"{total_varones:,}".replace(",", "."),
                f"{total_mujeres:,}".replace(",", "."),
                f"{total_general:,}".replace(",", "."),
            ],
            "Porcentaje": [
                f"{pct_varones:.2f}%".replace(".", ","),
                f"{pct_mujeres:.2f}%".replace(".", ","),
                "100,00%",
            ],
        })

        print(
            tabulate(
                resultado.values.tolist(),
                headers=["Género", "Cantidad", "Porcentaje"],
                tablefmt="pretty",
                disable_numparse=True,
                showindex=False,
            )
        )

        etiquetas = ["Varón / Masculino", "Mujer / Femenino"]
        valores = [total_varones, total_mujeres]
        colores = ["#2b7bba", "#e06d53"]

        def mostrar_cantidad_y_porcentaje(pct):
            absoluto = int(round((pct / 100.0) * total_general))
            cant_formateada = f"{absoluto:,}".replace(",", ".")
            pct_formateado = f"{pct:.2f}%".replace(".", ",")
            return f"{pct_formateado}\n({cant_formateada})"

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.pie(
            valores,
            labels=etiquetas,
            colors=colores,
            autopct=mostrar_cantidad_y_porcentaje,
            startangle=90,
            explode=(0.02, 0.02),
            textprops={"fontsize": 10, "fontweight": "bold"},
            wedgeprops={"edgecolor": "white", "linewidth": 1.5},
        )

        ax.set_title(
            "Distribución de Población por Género (Provincias de Argentina)",
            fontsize=13,
            fontweight="bold",
            pad=15,
        )
        ax.axis("equal")
        plt.tight_layout()

        plt.show()

        return resultado

    except Exception as e:
        print(f"[Error en Graficar_Distribucion_Genero_Provincias]: {e}")


def Exportar_Resumen_Provincias_JSON(
    df, nombre_archivo="resumen_provincias.json"
):
    """
    Filtra por Provincia para el detalle y métricas de género, suma también
    'Jurisdicción autónoma' únicamente en el Total Habitantes general, y
    exporta un archivo JSON con fecha/hora:
    1. Lo guarda automáticamente en la carpeta 'data/'.
    2. Abre una ventana para elegir dónde guardarlo en la PC y muestra enlace de descarga.
    """
    try:
        datos_provincias = df.query(
            "`Tipo de jurisdicción` == 'Provincia'"
        ).copy()
        datos_total_hab = df.query(
            "`Tipo de jurisdicción` in ['Provincia', 'Jurisdicción autónoma']"
        ).copy()

        columnas_numericas = [
            "Total habitantes",
            "Varon/Masculino",
            "Mujer/Femenino",
        ]
        for col in columnas_numericas:
            datos_provincias[col] = (
                pd.to_numeric(
                    datos_provincias[col]
                    .astype(str)
                    .str.replace(r"\.0$", "", regex=True)
                    .str.replace(".", "", regex=False)
                    .str.replace(",", "", regex=False),
                    errors="coerce",
                )
                .fillna(0)
            )

        datos_total_hab["Total habitantes"] = (
            pd.to_numeric(
                datos_total_hab["Total habitantes"]
                .astype(str)
                .str.replace(r"\.0$", "", regex=True)
                .str.replace(".", "", regex=False)
                .str.replace(",", "", regex=False),
                errors="coerce",
            )
            .fillna(0)
        )

        agrupado = (
            datos_provincias.groupby("Nombre")[columnas_numericas]
            .sum()
            .sort_values(by="Total habitantes", ascending=False)
        )

        # 1. Provincias con sus 3 valores adentro
        provincias_dict = {
            str(nombre): {
                "habitantes": int(fila["Total habitantes"]),
                "Varon/Masculino": int(fila["Varon/Masculino"]),
                "Mujer/Femenino": int(fila["Mujer/Femenino"]),
            }
            for nombre, fila in agrupado.iterrows()
        }

        # 2. Métricas generales (Total Habitantes incluye 'Jurisdicción autónoma')
        por_provincia = agrupado["Total habitantes"]
        total_varones = int(agrupado["Varon/Masculino"].sum())
        total_mujeres = int(agrupado["Mujer/Femenino"].sum())
        total_general = int(datos_total_hab["Total habitantes"].sum())

        metricas_dict = {
            "Cantidad de Provincias": int(por_provincia.count()),
            "Total Habitantes": total_general,
            "Promedio de Habitantes": round(float(por_provincia.mean()), 2),
            "Mínimo de Habitantes": int(por_provincia.min()),
            "Provincia con Mínimo Habitantes": str(por_provincia.idxmin()),
            "Máximo de Habitantes": int(por_provincia.max()),
            "Provincia con Máximo Habitantes": str(por_provincia.idxmax()),
            "Mediana de Habitantes": round(float(por_provincia.median()), 2),
            "Total Varon/Masculino": total_varones,
            "Total Mujer/Femenino": total_mujeres,
            "Porcentaje Varon/Masculino": (
                round((total_varones / total_general) * 100, 2)
                if total_general > 0
                else 0
            ),
            "Porcentaje Mujer/Femenino": (
                round((total_mujeres / total_general) * 100, 2)
                if total_general > 0
                else 0
            ),
        }

        fecha_hora_exportacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        reporte_json = {
            "fecha_exportacion": fecha_hora_exportacion,
            "provincias": provincias_dict,
            "metricas": metricas_dict,
        }
        ruta_data = os.path.join("Data", nombre_archivo)
        with open(ruta_data, "w", encoding="utf-8") as archivo:
            json.dump(reporte_json, archivo, ensure_ascii=False, indent=4)
    

        print(f"Copia guardada en: {os.path.abspath(ruta_data)}")

        try:
            display(
                FileLink(
                    ruta_data,
                    result_html_prefix=(
                        "Hacé clic acá para descargar el JSON: "
                    ),
                )
            )
        except Exception:
            pass

        try:
            ventana = tk.Tk()
            ventana.withdraw()
            ventana.attributes("-topmost", True)

            ruta_elegida = filedialog.asksaveasfilename(
                title="Elegí dónde guardar el archivo JSON",
                initialfile=nombre_archivo,
                defaultextension=".json",
                filetypes=[("Archivos JSON", "*.json")],
            )
            ventana.destroy()

            if ruta_elegida:
                with open(
                    ruta_elegida, "w", encoding="utf-8"
                ) as archivo_usuario:
                    json.dump(
                        reporte_json,
                        archivo_usuario,
                        ensure_ascii=False,
                        indent=4,
                    )
                print(f"Archivo guardado en la carpeta elegida: {ruta_elegida}")
            else:
                print(
                    "Selección de carpeta cancelada (quedó guardado en 'data')."
                )

        except Exception as e_ventana:
            print(
                f"No se pudo abrir el explorador de archivos ({e_ventana})."
                " Usá el enlace de descarga o la carpeta 'data'."
            )

        return reporte_json

    except Exception as e:
        print(f"[Error en Exportar_Resumen_Provincias_JSON]: {e}")