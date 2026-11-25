import pandas as pd
import os
from tabulate import tabulate 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from IPython.display import display
import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from IPython.display import FileLink
from Limpieza.limpieza import limpiar_tipos_dataset
from Conexion.cargar_datos import cargar_csv_con_pandas

df = cargar_csv_con_pandas()
df = limpiar_tipos_dataset(df)

def ver_informacion_general(df):
    """
    Opción 2: Muestra las primeras filas, nombres, tipos y nulos por columna.
    Registra la acción en el log y devuelve el DataFrame.
    """
    print("📊 INFORMACIÓN TIPOS DE DATOS")
    print("\n2. Tipos de datos y columnas:")
    print(df.dtypes)


def Cantidad_Partidos_Unicos(df):
  """
    Filtra por Tipo de jurisdicción == 'Partido', cuenta la cantidad única de registros
    y muestra el resultado con un formato visual ordenado.
    """
  try:
    cantidad_unica = df.query("`Tipo de jurisdicción` in ['Partido']")[
        "Nombre"
    ].nunique()

    resultado = pd.DataFrame({
        "Tipo de jurisdicción": ["Partido",],
        "Cantidad Única": [f"{int(cantidad_unica):,}".replace(",", ".")],
    })

    # .values.tolist() satisface el tipado estricto de tabulate
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
    print(f"[Error en Cantidad_Partidos_Unicos]: {e}")

#Total de habitantes por partido
def Total_Habitantes_Partido(df):
    """
    Filtra por Partido, agrupa por Nombre, suma los habitantes,
    y muestra la tabla completa con un formato visual ordenado.
    """
    df["Total habitantes"] = pd.to_numeric(
            df["Total habitantes"].astype(str)
            .str.replace('.', '', regex=False)
            .str.replace(',', '', regex=False), 
            errors='coerce'
        )
    try:
        resultado = (
            df.query("`Tipo de jurisdicción` == 'Partido'")
            .groupby("Nombre")["Total habitantes"]
            .sum()
            .reset_index()
            .sort_values(by="Total habitantes", ascending=False)
        )
        resultado["Total habitantes"] = resultado["Total habitantes"].apply(
            lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
        )
        # Imprimir usando tabulate con un diseño estético de grilla y sin mostrar el índice numérico
        print(tabulate(
            resultado, 
            headers=['Partido', 'Total Habitantes'], 
            tablefmt="pretty",  # mantené el tablefmt que estés usando
            disable_numparse=True,
            showindex=False
        ))
        return resultado
    except Exception as e:
        print(f"[Error en Total_Habitantes_Partido]: {e}")

def Habitantes_Por_Partido(df,Partido):
    """
    Filtra por Partido,Toma como parametro el nombre del partido, agrupa por Nombre, suma los habitantes,
    y muestra la tabla completa con un formato visual ordenado.
    """
    try:
        resultado = (
            df.query("`Tipo de jurisdicción` == 'Partido' and Nombre == @Partido")
            .groupby("Nombre")["Total habitantes"]
            .sum()
            .reset_index()
            .sort_values(by="Total habitantes", ascending=False)
        )
        resultado["Total habitantes"] = resultado["Total habitantes"].apply(
                    lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
                )
        # Imprimir usando tabulate con un diseño estético de grilla y sin mostrar el índice numérico
        print(tabulate(
            resultado, 
            headers=['Partido', 'Total Habitantes'], 
            tablefmt="pretty",  # mantené el tablefmt que estés usando
            disable_numparse=True,
            showindex=False
        ))
        return resultado
    except Exception as e:
        print(f"[Error en Total_Habitantes_Partido]: {e}")


def count_Habitantes_Partido(df):
    """
    Cuenta la cantidad de habitantes por partido y muestra el resultado en una tabla.
    """
    df["Total habitantes"] = pd.to_numeric(
                df["Total habitantes"].astype(str)
                .str.replace('.', '', regex=False)
                .str.replace(',', '', regex=False), 
                errors='coerce'
            )
    try:
        # 1. Filtrar por Provincia y calcular la mediana directa de la columna
        mediana_valor = (
           df.query("`Tipo de jurisdicción` in ['Partido']")["Total habitantes"]
            .sum()
        )
        
        # 2. Formatear el número con punto como separador de miles (ej: 300.000)
        mediana_formateada = f"{int(mediana_valor):,}".replace(",", ".") if pd.notnull(mediana_valor) else ""
        
        # 3. Crear una tabla de una sola fila para mostrar el resultado con tabulate
        resultado = pd.DataFrame({
            "Indicador": ["Total Habitantes"],
            "Total Habitantes": [mediana_formateada]
        })
        
        # 4. Imprimir con diseño estético
        print(tabulate(
            resultado,  # type: ignore
            headers='keys', 
            tablefmt="pretty",  # mantené el tablefmt que estés usando
            disable_numparse=True,
            showindex=False
        ))
        
    except Exception as e:
        print(f"[Error en count_Habitantes_Partido]: {e}")

def Estadisticas_Habitantes_Partido(df):
  """
    Filtra por Partido, agrupa por Nombre para sumar los habitantes de cada partido,
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

    # Agrupamos por Nombre igual que en tu función modelo para obtener el total por Partido
    por_partido = (
        datos.query("`Tipo de jurisdicción` == 'Partido'")
        .groupby("Nombre")["Total habitantes"]
        .sum()
    )

    cantidad = int(por_partido.count())
    promedio = por_partido.mean()
    minimo = por_partido.min()
    maximo = por_partido.max()
    mediana = por_partido.median()

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
            "Cantidad de Partidos",
            "Promedio de Habitantes",
            "Mínimo de Habitantes",
            "Máximo de Habitantes",
            "Mediana de Habitantes",
        ],
        "Valor": [
            formatear(cantidad),
            formatear(promedio, decimales=  False),
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
    print(f"[Error en Estadisticas_Habitantes_Partido]: {e}")

def Total_Varon_Partido(df):
    """
    Filtra por Partido, agrupa por Nombre, suma los habitantes,
    y muestra la tabla completa con un formato visual ordenado.
    """
    df["Varon/Masculino"] = pd.to_numeric(
                df["Varon/Masculino"].astype(str)
                .str.replace('.', '', regex=False)
                .str.replace(',', '', regex=False),
                errors='coerce'
            )
    try:
        resultado = (
            df.query("`Tipo de jurisdicción` == 'Partido'")
            .groupby("Nombre")["Varon/Masculino"]
            .sum()
            .reset_index()
            .sort_values(by="Varon/Masculino", ascending=False)
        )
        resultado["Varon/Masculino"] = resultado["Varon/Masculino"].apply(
            lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
        )
        # Imprimir usando tabulate con un diseño estético de grilla y sin mostrar el índice numérico
        print(tabulate(
         resultado,
        headers=["Partido", "Varon/Masculino"],
        tablefmt="pretty",  # mantené el tablefmt que estés usando
        disable_numparse=True,
        showindex=False
))
    except Exception as e:
        print(f"[Error en Total_Varon_Partido]: {e}")

def Total_Mujer_Partido(df):
    """
    Filtra por Partido, agrupa por Nombre, suma los habitantes,
    y muestra la tabla completa con un formato visual ordenado.
    """
    df["Mujer/Femenino"] = pd.to_numeric(
                df["Mujer/Femenino"].astype(str)
                .str.replace('.', '', regex=False)
                .str.replace(',', '', regex=False),
                errors='coerce'
            )
    try:
        resultado = (
            df.query("`Tipo de jurisdicción` == 'Partido'")
            .groupby("Nombre")["Mujer/Femenino"]
            .sum()
            .reset_index()
            .sort_values(by="Mujer/Femenino", ascending=False)
        )
        resultado["Mujer/Femenino"] = resultado["Mujer/Femenino"].apply(
            lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else ""
        )
        # Imprimir usando tabulate con un diseño estético de grilla y sin mostrar el índice numérico
        print(tabulate(
         resultado,
        headers=["Partido", "Mujer/Femenino"],
        tablefmt="pretty",  # mantené el tablefmt que estés usando
        disable_numparse=True,
        showindex=False
))
    except Exception as e:
        print(f"[Error en Total_Mujer_Partido]: {e}")


def Graficar_Top10_BuenosAires(df):
  """
    Filtra por Tipo de jurisdicción == 'Partido' (Provincia de Buenos Aires),
    agrupa por Nombre, toma el Top 10 por habitantes y muestra un gráfico de barras.
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
        datos.query("`Tipo de jurisdicción` == 'Partido'")
        .groupby("Nombre")["Total habitantes"]
        .sum()
        .reset_index()
        .sort_values(by="Total habitantes", ascending=False)
        .head(10)
    )

    # Invertimos el orden para que el #1 aparezca arriba
    top10 = top10.iloc[::-1]

    fig, ax = plt.subplots(figsize=(10, 6))
    barras = ax.barh(top10["Nombre"], top10["Total habitantes"], color="#1f77b4")

    ax.set_title(
        "Top 10 Departamentos / Partidos de la Provincia de Buenos Aires",
        fontsize=12,
        fontweight="bold",
        pad=12,
    )
    ax.set_xlabel("Total de Habitantes")
    ax.set_ylabel("Partido")

    # Formatear eje X con puntos de miles en lugar de notación científica
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", "."))
    )

    # Mostrar la cantidad exacta al lado de cada barra
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
    print(f"[Error en Graficar_Top10_BuenosAires]: {e}")
    


def Graficar_Distribucion_Genero(df):
 try:
    datos = df.query("`Tipo de jurisdicción` == 'Partido'").copy()

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
        "Distribución de Población por Género (Provincia de Buenos Aires)",
        fontsize=13,
        fontweight="bold",
        pad=15,
    )
    ax.axis("equal")
    plt.tight_layout()

    # Para consola (.py) usá plt.show()
    plt.show()

    return resultado

 except Exception as e:
    print(f"[Error en Graficar_Distribucion_Genero]: {e}")

def Exportar_Resumen_JSON(df, nombre_archivo="resumen_partidos.json"):
  """
    Filtra por Partido, agrupa por Nombre y exporta un archivo JSON con fecha/hora:
    1. Lo guarda automáticamente en la carpeta 'data/'.
    2. Abre una ventana para elegir dónde guardarlo en la PC y muestra enlace de descarga.
    """
  try:
    datos = df.query("`Tipo de jurisdicción` == 'Partido'").copy()

    # Limpieza de columnas numéricas
    columnas_numericas = [
        "Total habitantes",
        "Varon/Masculino",
        "Mujer/Femenino",
    ]
    for col in columnas_numericas:
      datos[col] = pd.to_numeric(
          datos[col]
          .astype(str)
          .str.replace(r"\.0$", "", regex=True)
          .str.replace(".", "", regex=False)
          .str.replace(",", "", regex=False),
          errors="coerce",
      ).fillna(0)

    # Agrupamos las 3 columnas por Nombre y ordenamos por Total habitantes de mayor a menor
    agrupado = (
        datos.groupby("Nombre")[columnas_numericas]
        .sum()
        .sort_values(by="Total habitantes", ascending=False)
    )

    # 1. Partidos con sus 3 valores adentro
    partidos_dict = {
        str(nombre): {
            "habitantes": int(fila["Total habitantes"]),
            "Varon/Masculino": int(fila["Varon/Masculino"]),
            "Mujer/Femenino": int(fila["Mujer/Femenino"]),
        }
        for nombre, fila in agrupado.iterrows()
    }

    # 2. Métricas generales
    por_partido = agrupado["Total habitantes"]
    total_varones = int(agrupado["Varon/Masculino"].sum())
    total_mujeres = int(agrupado["Mujer/Femenino"].sum())
    total_general = int(por_partido.sum())

    metricas_dict = {
        "Cantidad de Partidos": int(por_partido.count()),
        "Total Habitantes": total_general,
        "Promedio de Habitantes": round(float(por_partido.mean()), 2),
        "Mínimo de Habitantes": int(por_partido.min()),
        "Partido con Mínimo Habitantes": str(por_partido.idxmin()),
        "Máximo de Habitantes": int(por_partido.max()),
        "Partido con Máximo Habitantes": str(por_partido.idxmax()),
        "Mediana de Habitantes": round(float(por_partido.median()), 2),
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

    # Fecha y hora del momento en que se exporta
    fecha_hora_exportacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Estructura final del JSON
    reporte_json = {
        "fecha_exportacion": fecha_hora_exportacion,
        "partidos": partidos_dict,
        "metricas": metricas_dict,
    }

    # 1) Guardar automáticamente en la carpeta 'data'
    ruta_data = os.path.join("data", nombre_archivo)
    with open(ruta_data, "w", encoding="utf-8") as archivo:
      json.dump(reporte_json, archivo, ensure_ascii=False, indent=4)

    print(f"Copia guardada en: {os.path.abspath(ruta_data)}")

    # 2) Enlace de descarga directa si estás en Jupyter Notebook
    try:
      display(
          FileLink(
              ruta_data,
              result_html_prefix="Hacé clic acá para descargar el JSON: ",
          )
      )
    except Exception:
      pass

    # 3) Abrir ventana "Guardar como..." para elegir carpeta en tu PC
    try:
      ventana = tk.Tk()
      ventana.withdraw()  # Oculta la ventana vacía de tkinter
      ventana.attributes("-topmost", True)  # Pone el diálogo al frente de todo

      ruta_elegida = filedialog.asksaveasfilename(
          title="Elegí dónde guardar el archivo JSON",
          initialfile=nombre_archivo,
          defaultextension=".json",
          filetypes=[("Archivos JSON", "*.json")],
      )
      ventana.destroy()

      if ruta_elegida:
        with open(ruta_elegida, "w", encoding="utf-8") as archivo_usuario:
          json.dump(reporte_json, archivo_usuario, ensure_ascii=False, indent=4)
        print(f"Archivo guardado en la carpeta elegida: {ruta_elegida}")
      else:
        print("Selección de carpeta cancelada (quedó guardado en 'data').")

    except Exception as e_ventana:
      print(
          f"No se pudo abrir el explorador de archivos ({e_ventana}). Usá el"
          " enlace de descarga o la carpeta 'data'."
      )

    return reporte_json

  except Exception as e:
    print(f"[Error en Exportar_Resumen_JSON]: {e}")