import pandas as pd
import json
def ver_informacion_general(df):
    """
    Opción 2: Muestra las primeras filas, nombres, tipos y nulos por columna.
    Registra la acción en el log y devuelve el DataFrame.
    """
    print("📊 INFORMACIÓN TIPOS DE DATOS")
    print("\n2. Tipos de datos y columnas:")
    print(df.dtypes)


def medianaColectivos(df):
    """
    Opción 3: Calcula la mediana de la columna 'total' para el medio de transporte 'Colectivo'.
    """
    try:
        resultado = (
            df.query("`Medios de transporte` == 'Colectivo'")
            .groupby("Medios de transporte")
            .agg(mediana_total=("Valor", "median"))
            .reset_index()
        )
        print("\n--- RESULTADO DE LA MEDIANA ---")
        print(resultado)
    except Exception as e:
        print(f"[Error en medianaColectivos]: {e}")
        


def guardar_json(datos, ruta_json):
    """Guarda las estadísticas en formato JSON."""
    with open(ruta_json, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)