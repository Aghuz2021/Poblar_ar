
from Conexion.cargar_datos import cargar_csv_con_pandas


from Filtros.filtros import ver_informacion_general, medianaColectivos,calcular_y_guardar_estadisticas,guardar_json
def main():
    try:
        # Nombre de tu archivo dentro de la carpeta 'data/'
       
        # Cargar el DataFrame usando la función del módulo conexion
        df = cargar_csv_con_pandas()

        # Llamar a la función para ver la información general
        #ver_informacion_general(df)
        #medianaColectivos(df)
        calcular_y_guardar_estadisticas(df,nombre_salida="estadisticas_viajes.json")
    

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()