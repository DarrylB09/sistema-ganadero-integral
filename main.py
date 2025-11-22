# main.py

"""
Sistema Ganadero Integral

Este programa reúne tres módulos principales:
1. Registro de Ganado – administra la base de animales.
2. Producción Láctea – usa los animales registrados para manejar
   producción de leche y estadísticas.
3. Control Sanitario – gestiona fichas de salud, vacunas y tratamientos.

El archivo main.py funciona como menú central y comparte las listas
de datos entre los módulos, permitiendo que todo el sistema trabaje
con la misma información.
"""

from registro_ganado import sistema_registro_ganado
from produccion_lactea import sistema_produccion_lactea
from control_sanitario import sistema_control_sanitario


def main():
    # LISTAS CENTRALES COMPARTIDAS ENTRE TODOS LOS MÓDULOS
    animales = []            # Registro general del hato
    vacas_lecheras = []      # Producción láctea
    fichas_sanitarias = []   # Control sanitario

    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            sistema_registro_ganado(animales)

        elif opcion == "2":
            sistema_produccion_lactea(animales, vacas_lecheras)

        elif opcion == "3":
            sistema_control_sanitario(animales, fichas_sanitarias)

        elif opcion == "4":
            print("¡Gracias por usar el Sistema Ganadero Integral!")
            break

        else:
            print("Opción no válida.\n")


def mostrar_menu_principal():
    print("======================================")
    print("      SISTEMA GANADERO INTEGRAL")
    print("======================================")
    print("1. Sistema de Registro de Ganado")
    print("2. Sistema de Producción Láctea")
    print("3. Sistema de Control Sanitario")
    print("4. Salir")
    print("======================================")

if __name__ == "__main__":
    main()
