import os
import pandas as pd

def cargar_csv_con_pandas(nombre_archivo: str) -> pd.DataFrame:
    """
    Obtiene la ruta absoluta de forma segura con os y carga el CSV usando pandas.
    """
    # 1. Obtener la ruta absoluta usando os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.dirname(current_dir)
    ruta = os.path.join(backend_dir, 'data', nombre_archivo)
    
    try:
        # 2. Leer directamente con pandas manejando el archivo de forma segura
        df = pd.read_csv(ruta, encoding='utf-8')
        print(f"[Éxito] CSV leído correctamente con Pandas desde: {ruta}")
        return df
        
    except FileNotFoundError:
        raise FileNotFoundError(f"[Error] El archivo no se encuentra en la ruta: {ruta}")
    except Exception as e:
        raise IOError(f"[Error] Ocurrió un problema al procesar el archivo con Pandas: {e}")