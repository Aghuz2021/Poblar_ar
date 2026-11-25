from Filtros.partido import (
    Cantidad_Partidos_Unicos,
    Estadisticas_Habitantes_Partido,
    Exportar_Resumen_JSON,
    Graficar_Distribucion_Genero,
    Graficar_Top10_BuenosAires,
    Habitantes_Por_Partido,
    Total_Habitantes_Partido,
    Total_Mujer_Partido,
    Total_Varon_Partido,
    count_Habitantes_Partido,
)


def pausar() -> None:
  """Detiene el bucle para que el usuario pueda leer la tabla antes de volver al menú."""
  input("\nPresione Enter para continuar...")


def menu_partidos(df) -> None:
  while True:
    print("\n\n" + "=" * 68)
    print("                 MENÚ - DEPARTAMENTOS / PARTIDOS")
    print("=" * 68 + "\n")

    print("1. Habitantes por partido:\n")
    print("   1.1 Ver listado completo de habitantes por partido")
    print("   1.2 Ver cantidad total de habitantes (Provincia de Buenos Aires)")
    print("   1.3 Buscar y filtrar habitantes de un partido específico")
    print("   1.4 Gráfico de barras: Top 10 partidos más poblados")
    print(
        "   1.5 Estadísticas generales (cantidad, promedio, mín, máx y"
        " mediana)\n"
    )

    print("2. Distribución por género (Varones y Mujeres):\n")
    print("   2.1 Ver cantidad de varones por partido")
    print("   2.2 Ver cantidad de mujeres por partido")
    print("   2.3 Gráfico de distribución de género (Buenos Aires)\n")

    print("3. Ver cantidad total de partidos / departamentos únicos\n")
    print("4. Exportar resumen completo a archivo JSON\n")

    print("-" * 68)
    print("0. Volver al menú principal")
    print("=" * 68 + "\n")

    opcion = input("Seleccione una opción (ej. 1.1, 2.3, 4): ").strip()
    print()

    if opcion == "1.1":
      Total_Habitantes_Partido(df)
      pausar()
    elif opcion == "1.2":
      count_Habitantes_Partido(df)
      pausar()
    elif opcion == "1.3":
      partido = input("Ingrese el nombre del partido (ej. La Plata): ").strip()
      print()
      if partido:
        Habitantes_Por_Partido(df, partido)
      else:
        print("Debe ingresar un nombre de partido válido.")
      pausar()
    elif opcion == "1.4":
      Graficar_Top10_BuenosAires(df)
    elif opcion == "1.5":
      Estadisticas_Habitantes_Partido(df)
      pausar()
    elif opcion == "2.1":
      Total_Varon_Partido(df)
      pausar()
    elif opcion == "2.2":
      Total_Mujer_Partido(df)
      pausar()
    elif opcion == "2.3":
      Graficar_Distribucion_Genero(df)
    elif opcion == "3":
      Cantidad_Partidos_Unicos(df)
      pausar()
    elif opcion == "4":
      Exportar_Resumen_JSON(df)
      pausar()
    elif opcion == "0":
      print("Volviendo al menú principal...")
      break
    else:
      print(
          "Opción inválida. Por favor, ingrese una opción válida del menú."
      )
      pausar()