
from Conexion.cargar_datos import cargar_csv_con_pandas
from Filtros.Menu_Partido import menu_partidos
from Filtros.partido import ver_informacion_general
from Limpieza.limpieza import limpiar_tipos_dataset







def main() -> None:

    print("Cargando dataset...")
    df_crudo = cargar_csv_con_pandas()
    df = limpiar_tipos_dataset(df_crudo)

    while True:

        print("\n" + "=" * 45)
        print("       SISTEMA DE ANÁLISIS DE HABITANTES")
        print("=" * 45)
        print("1. Por Departamento / Partidos")
        print("2. Por Provincias")
        print("3. Ver información general del dataset")
        print("0. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
          menu_partidos(df=cargar_csv_con_pandas())

        elif opcion == "2":
            print("Futura actualización: Análisis por Provincias aún no implementado.")
            # Aquí puedes agregar la lógica para manejar la opción 2
        elif opcion == "3":
            ver_informacion_general(df)
            
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
