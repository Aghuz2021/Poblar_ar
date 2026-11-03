import pandas as pd
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
        # Usamos backticks por los espacios en el nombre de la columna
        # Y aseguramos la comparación evaluando mayúsculas/minúsculas si es necesario
        df_filtrado = df.query("`Medios de transporte` == 'Colectivo'")
        
        if df_filtrado.empty:
            print("⚠️ No se encontraron registros exactos para 'Colectivo'. Probando con minúscula...")
            df_filtrado = df.query("`Medios de transporte` == 'colectivo'")
            
        if df_filtrado.empty:
            print("❌ El filtro sigue vacío. Revisa si en tu CSV el valor dice otra cosa.")
            return

        resultado = (
            df_filtrado
            .groupby("Medios de transporte")
            .agg(mediana_total=("Valor", "median"))
            .reset_index()
        )
        
        print("\n--- RESULTADO DE LA MEDIANA ---")
        print(resultado)
        return resultado

    except Exception as e:
        print(f"[Error en medianaColectivos]: {e}")