# produccion_lactea.py
# Subsistema: Producción Láctea

from datetime import datetime
from registro_ganado import CATEGORIAS  # usamos la misma lista por coherencia


CATEGORIA_ORDEÑO = "Vaca de ordeño"


def sistema_produccion_lactea(animales, produccion):
    while True:
        mostrar_menu_produccion()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_vaca_al_sistema_lechero(animales, produccion)
        elif opcion == "2":
            registrar_produccion_leche(animales, produccion)
        elif opcion == "3":
            listar_vacas_sistema_lechero(animales, produccion)
        elif opcion == "4":
            reporte_detallado_vaca(animales, produccion)
        elif opcion == "5":
            produccion_total_por_fecha(produccion)
        elif opcion == "6":
            mostrar_vaca_mas_productiva(animales, produccion)
        elif opcion == "7":
            mostrar_resumen_general(produccion)
        elif opcion == "0":
            print("Volviendo al menú principal...\n")
            break
        else:
            print("Opción no válida.\n")


def mostrar_menu_produccion():
    print("======================================")
    print("      SISTEMA DE PRODUCCIÓN LÁCTEA")
    print("======================================")
    print("1. Agregar vaca de ordeño al sistema lechero")
    print("2. Registrar producción de leche")
    print("3. Listar vacas del sistema lechero")
    print("4. Ver reporte detallado de una vaca")
    print("5. Ver producción total por fecha")
    print("6. Ver vaca más productiva")
    print("7. Ver resumen general de producción")
    print("0. Volver")
    print("======================================")


# ---------- APOYO ---------- #

def pedir_float(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Formato incorrecto. Ingresa un número válido.\n")


def pedir_fecha(mensaje):
    while True:
        fecha_str = input(mensaje).strip()
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha_str
        except ValueError:
            print("Formato incorrecto. Usa YYYY-MM-DD.\n")


def buscar_animal_por_id(animales, id_animal):
    for a in animales:
        if a["id"] == id_animal:
            return a
    return None


def buscar_registro_produccion(produccion, id_animal):
    for registro in produccion:
        if registro["id"] == id_animal:
            return registro
    return None


def animales_de_ordeño(animales):
    return [a for a in animales if a["categoria"] == CATEGORIA_ORDEÑO]


# ---------- FUNCIONALIDAD PRINCIPAL ---------- #

def agregar_vaca_al_sistema_lechero(animales, produccion):
    print("\n--- Agregar vaca de ordeño al sistema lechero ---")
    vacas_ordeño = animales_de_ordeño(animales)

    if not vacas_ordeño:
        print("No hay animales registrados en la categoría 'Vaca de ordeño'.\n")
        return

    print("Vacas de ordeño disponibles:")
    for a in vacas_ordeño:
        print(f"ID:{a['id']} | Nombre:{a['nombre']}")

    id_vaca = input("Ingresa el ID de la vaca que deseas agregar: ").strip()
    animal = buscar_animal_por_id(vacas_ordeño, id_vaca)

    if not animal:
        print("ID no válido para vaca de ordeño.\n")
        return

    if buscar_registro_produccion(produccion, id_vaca):
        print("Esta vaca ya está en el sistema lechero.\n")
        return

    produccion.append({"id": id_vaca, "registros": []})
    print(f"Vaca '{animal['nombre']}' agregada al sistema lechero.\n")


def registrar_produccion_leche(animales, produccion):
    print("\n--- Registrar producción de leche ---")
    if not produccion:
        print("No hay vacas en el sistema lechero.\n")
        return

    listar_vacas_sistema_lechero(animales, produccion)
    id_vaca = input("Ingresa el ID de la vaca: ").strip()

    registro = buscar_registro_produccion(produccion, id_vaca)
    if not registro:
        print("Esa vaca no está en el sistema lechero.\n")
        return

    fecha = pedir_fecha("Fecha de producción (YYYY-MM-DD): ")
    litros = pedir_float("Litros producidos: ")

    registro["registros"].append({"fecha": fecha, "litros": litros})
    print("Producción registrada.\n")


def listar_vacas_sistema_lechero(animales, produccion):
    print("\n--- Vacas en el sistema lechero ---")
    if not produccion:
        print("No hay vacas en el sistema lechero.\n")
        return

    for reg in produccion:
        animal = buscar_animal_por_id(animales, reg["id"])
        nombre = animal["nombre"] if animal else "Desconocido"
        print(f"ID:{reg['id']} | Nombre:{nombre} | Registros:{len(reg['registros'])}")
    print()


def reporte_detallado_vaca(animales, produccion):
    print("\n--- Reporte detallado de una vaca ---")
    if not produccion:
        print("No hay vacas en el sistema lechero.\n")
        return

    id_vaca = input("ID de la vaca: ").strip()
    registro = buscar_registro_produccion(produccion, id_vaca)

    if not registro:
        print("Esa vaca no está en el sistema lechero.\n")
        return

    animal = buscar_animal_por_id(animales, id_vaca)
    nombre = animal["nombre"] if animal else "Desconocido"

    print(f"\nVaca: {nombre} (ID:{id_vaca})")
    if not registro["registros"]:
        print("Sin registros de producción.\n")
        return

    total = 0
    for r in registro["registros"]:
        print(f"- {r['fecha']} → {r['litros']} litros")
        total += r["litros"]

    promedio = total / len(registro["registros"])
    print(f"Total producido: {total:.2f} litros")
    print(f"Promedio por registro: {promedio:.2f} litros\n")


def produccion_total_por_fecha(produccion):
    print("\n--- Producción total por fecha ---")
    if not produccion:
        print("No hay vacas en el sistema lechero.\n")
        return

    fecha = pedir_fecha("Fecha a consultar (YYYY-MM-DD): ")
    total = 0

    for reg in produccion:
        for r in reg["registros"]:
            if r["fecha"] == fecha:
                total += r["litros"]

    print(f"Total producido en {fecha}: {total:.2f} litros.\n")


def mostrar_vaca_mas_productiva(animales, produccion):
    print("\n--- Vaca más productiva ---")
    if not produccion:
        print("No hay vacas en el sistema lechero.\n")
        return

    mejor_id = None
    mejor_total = 0

    for reg in produccion:
        total = sum(r["litros"] for r in reg["registros"])
        if total > mejor_total:
            mejor_total = total
            mejor_id = reg["id"]

    if mejor_id is None:
        print("No hay datos de producción.\n")
        return

    animal = buscar_animal_por_id(animales, mejor_id)
    nombre = animal["nombre"] if animal else "Desconocido"
    print(f"La vaca más productiva es {nombre} (ID:{mejor_id}) con {mejor_total:.2f} litros.\n")


def mostrar_resumen_general(produccion):
    print("\n--- Resumen general de producción ---")
    if not produccion:
        print("No hay vacas en el sistema lechero.\n")
        return

    total_litros = 0
    total_registros = 0

    for reg in produccion:
        for r in reg["registros"]:
            total_litros += r["litros"]
            total_registros += 1

    print(f"Total de litros producidos: {total_litros:.2f}")
    print(f"Total de registros: {total_registros}")
    if total_registros > 0:
        print(f"Promedio por registro: {total_litros / total_registros:.2f} litros\n")
    else:
        print()
