from Conexion.cargar_datos import cargar_csv_con_pandas
import pandas as pd


df = cargar_csv_con_pandas()
def limpiar_tipos_dataset(df):
  """
    Limpia separadores de miles, valores nulos o guiones y convierte
    las columnas numéricas a int64 y las de texto a str.
    """
  try:
    df = df.copy()

    columnas_texto = ["Nombre", "Tipo de jurisdicción","Provincia/estado","Codigo"]
    columnas_enteras = [
        "Casa",
        "Rancho",
        "Departamento",
        "Otro tipo de vivienda",
        "Total de viviendas",
        "Varon/Masculino",
        "Mujer/Femenino",
        "Total habitantes",
    ]

    # 1. Limpiar columnas de texto
    for col in columnas_texto:
      if col in df.columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

    # 2. Limpiar y convertir columnas a int64
    for col in columnas_enteras:
      if col in df.columns:
        if pd.api.types.is_integer_dtype(df[col]):
          df[col] = df[col].astype("int64")
        else:
          df[col] = (
              pd.to_numeric(
                  df[col]
                  .astype(str)
                  .str.strip()
                  .str.replace(r"\.0$", "", regex=True)
                  .str.replace(".", "", regex=False)
                  .str.replace(",", "", regex=False),
                  errors="coerce",
              )
              .fillna(0)
              .astype("int64")
          )

    return df

  except Exception as e:
    print(f"[Error en limpiar_tipos_dataset]: {e}")
    return df


# Forma correcta de ejecutarlo: primero cargás el CSV y después lo pasás a limpiar
