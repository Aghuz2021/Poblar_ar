from Filtros.Provincias import (
    Cantidad_Provincias_Unicas,
    Estadisticas_Habitantes_Provincia,
    Exportar_Resumen_Provincias_JSON,
    Graficar_Distribucion_Genero_Provincias,
    Graficar_Top10_Provincias,
    Habitantes_Por_Provincia,
    Total_Habitantes_Provincia,
    Total_Mujer_Provincia,
    Total_Varon_Provincia,
    count_Habitantes_Provincia,
)


def pausar() -> None:
    """Detiene el bucle para que el usuario pueda leer la tabla antes de volver al menú."""
    input("\nPresione Enter para continuar...")


def menu_provincias(df) -> None:
    """Muestra el menú interactivo de análisis poblacional por provincia argentina."""
    while True:
        print("\n\n" + "=" * 68)
        print("                   MENÚ - PROVINCIAS ARGENTINAS")
        print("=" * 68 + "\n")

        print("1. Habitantes por provincia:\n")
        print("   1.1 Ver listado completo de habitantes por provincia")
        print(
            "   1.2 Ver cantidad total de habitantes (Provincias de Argentina)"
        )
        print(
            "   1.3 Buscar y filtrar habitantes de una provincia específica"
        )
        print("   1.4 Gráfico de barras: Top 10 provincias más pobladas")
        print(
            "   1.5 Estadísticas generales (cantidad, promedio, mín, máx y"
            " mediana)\n"
        )

        print("2. Distribución por género (Varones y Mujeres):\n")
        print("   2.1 Ver cantidad de varones por provincia")
        print("   2.2 Ver cantidad de mujeres por provincia")
        print(
            "   2.3 Gráfico de distribución de género (Provincias de Argentina)\n"
        )

        print("3. Ver cantidad total de provincias únicas\n")
        print("4. Exportar resumen completo de provincias a archivo JSON\n")

        print("-" * 68)
        print("0. Volver al menú principal")
        print("=" * 68 + "\n")

        opcion = input("Seleccione una opción (ej. 1.1, 2.3, 4): ").strip()
        print()

        if opcion == "1.1":
            Total_Habitantes_Provincia(df)
            pausar()
        elif opcion == "1.2":
            count_Habitantes_Provincia(df)
            pausar()
        elif opcion == "1.3":
            provincia = input(
                "Ingrese el nombre de la provincia (ej. Córdoba): "
            ).strip()
            print()
            if provincia:
                Habitantes_Por_Provincia(df, provincia)
            else:
                print("Debe ingresar un nombre de provincia válido.")
            pausar()
        elif opcion == "1.4":
            Graficar_Top10_Provincias(df)
        elif opcion == "1.5":
            Estadisticas_Habitantes_Provincia(df)
            pausar()
        elif opcion == "2.1":
            Total_Varon_Provincia(df)
            pausar()
        elif opcion == "2.2":
            Total_Mujer_Provincia(df)
            pausar()
        elif opcion == "2.3":
            Graficar_Distribucion_Genero_Provincias(df)
        elif opcion == "3":
            Cantidad_Provincias_Unicas(df)
            pausar()
        elif opcion == "4":
            Exportar_Resumen_Provincias_JSON(df)
            pausar()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print(
                "Opción inválida. Por favor, ingrese una opción válida del"
                " menú."
            )
            pausar()