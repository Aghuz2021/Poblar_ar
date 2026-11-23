import pandas as pd
import os
from tabulate import tabulate 
#Total de habitantes por partido
def TotalHabitantesPartido(df):
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
        print(f"[Error en TotalHabitantesPartido]: {e}")

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
        print(f"[Error en TotalHabitantesPartido]: {e}")


def countHabitantesPartido(df):
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
        print(f"[Error en countHabitantesPartido]: {e}")



def TotalVaronPartido(df):
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
        print(f"[Error en TotalVaronPartido]: {e}")

def TotalMujerPartido(df):
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
        print(f"[Error en TotalMujerPartido]: {e}")