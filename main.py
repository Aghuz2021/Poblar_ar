
from Conexion.cargar_datos import cargar_csv_con_pandas
from Filtros.partido import TotalHabitantesPartido, Habitantes_Por_Partido,TotalVaronPartido,TotalMujerPartido,countHabitantesPartido


def menu_partidos(df):

    while True:
        print("\n" + "=" * 45)
        print("           MENÚ - DEPARTAMENTO / PARTIDOS")
        print("=" * 45)
        print("1.Habitantes por partido:")
        print("  *Ingrese la opcion 1.1 o 1.2 o 1.3 para ver la información correspondiente:")
        print("  1.1 Ver listado completo de habitantes por partido")
        print("  1.2 Ver cantidad total de habitantes por partido")
        print("  1.3 Filtrar habitantes por partido")
        print("3.Varones y mujeres por departamento / partido:")
        print("  3.1 Ver cantidad de varones por departamento /partido")
        print("  3.2 Ver cantidad de mujeres por departamento /partido")
        print("0. Volver al menú principal")
        print("=" * 45)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1.1":
            TotalHabitantesPartido(df)
        if opcion == "1.2":
            countHabitantesPartido(df)
        elif opcion == "1.3":
            partido = input("Ingrese el nombre del partido: ").strip()
            Habitantes_Por_Partido(df, partido)
        elif opcion == "3.1":
            TotalVaronPartido(df)
        elif opcion == "3.2":
            TotalMujerPartido(df)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


def menu_provincias(df):

    while True:
        print("\n" + "=" * 45)
        print("              MENÚ - PROVINCIAS")
        print("=" * 45)
        print("1. Ver listado de habitantes por provincia")
        print("2. Filtrar por provincia")
        print("0. Volver al menú principal")
        print("=" * 45)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("Funcionalidad pendiente de implementar.")

        elif opcion == "2":
            print("Funcionalidad pendiente de implementar.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


def main() -> None:

    print("Cargando dataset...")
    df = cargar_csv_con_pandas()

    while True:

        print("\n" + "=" * 45)
        print("       SISTEMA DE ANÁLISIS DE HABITANTES")
        print("=" * 45)
        print("1. Departamento / Partidos")
        print("2. Provincias")
        print("0. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_partidos(df)

        elif opcion == "2":
            menu_provincias(df)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
