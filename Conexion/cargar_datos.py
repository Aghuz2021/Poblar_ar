import os
import pandas as pd


def cargar_csv_con_pandas():
    """
    Obtiene la ruta absoluta de forma segura con os y carga el CSV usando pandas.
    """
    # 1. Obtener la ruta absoluta usando os
    archivo = os.path.join(
        os.path.dirname(__file__), "..", "data", "bd.csv"
    )
    try:
        # 2. Leer directamente con pandas manejando el archivo de forma segura
        df = pd.read_csv(archivo, encoding="utf-8")
        print(f"CSV leído correctamente con Pandas desde: {archivo}")
        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"[Error] El archivo no se encuentra en la ruta: {archivo}"
        )
    except Exception as e:
        raise IOError(
            f"[Error] Ocurrió un problema al procesar el archivo con Pandas: {e}"
        )

