# produccion_lactea.py
# Subsistema: Producción Láctea

def sistema_produccion_lactea(animales, produccion):

    while True:
        mostrar_menu_produccion()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_vaca_al_sistema(animales, produccion)

        elif opcion == "2":
            registrar_produccion_leche(animales, produccion)

        elif opcion == "3":
            listar_vacas_sistema(produccion)

        elif opcion == "4":
            reporte_por_vaca(animales, produccion)

        elif opcion == "5":
            produccion_por_fecha(produccion)

        elif opcion == "6":
            vaca_mas_productiva(animales, produccion)

        elif opcion == "7":
            resumen_general(produccion)

        elif opcion == "0":
            print("Volviendo...\n")
            break

        else:
            print("Opción inválida.\n")


def mostrar_menu_produccion():
    print("======================================")
    print("      SISTEMA DE PRODUCCIÓN LÁCTEA")
    print("======================================")
    print("1. Agregar vaca al sistema lechero")
    print("2. Registrar producción de leche")
    print("3. Listar vacas del sistema lechero")
    print("4. Ver reporte detallado de una vaca")
    print("5. Ver producción total por fecha")
    print("6. Ver vaca más productiva")
    print("7. Resumen general del sistema")
    print("0. Volver")
    print("======================================")


# -------- LÓGICA -------- #

def agregar_vaca_al_sistema(animales, produccion):
    id_vaca = input("ID de la vaca: ").strip()

    if not any(a["id"] == id_vaca for a in animales):
        print("La vaca NO existe en el registro general.\n")
        return

    if any(p["id"] == id_vaca for p in produccion):
        print("La vaca YA está en el sistema lechero.\n")
        return

    produccion.append({"id": id_vaca, "registros": []})
    print("Vaca agregada al sistema lechero.\n")


def registrar_produccion_leche(animales, produccion):
    id_vaca = input("ID: ").strip()

    vaca = next((p for p in produccion if p["id"] == id_vaca), None)
    if not vaca:
        print("Esta vaca no está en el sistema lechero.\n")
        return

    fecha = input("Fecha (YYYY-MM-DD): ")
    litros = float(input("Litros: "))

    vaca["registros"].append({"fecha": fecha, "litros": litros})
    print("Producción registrada.\n")


def listar_vacas_sistema(produccion):
    print("\n--- Vacas en producción ---")
    if not produccion:
        print("No hay vacas en el sistema.\n")
        return

    for v in produccion:
        print(f"- ID {v['id']} | Registros: {len(v['registros'])}")
    print()


def reporte_por_vaca(animales, produccion):
    id_vaca = input("ID: ").strip()
    vaca = next((p for p in produccion if p["id"] == id_vaca), None)

    if not vaca:
        print("No está en el sistema lechero.\n")
        return

    print(f"\n--- Reporte de {id_vaca} ---")
    total = sum(r["litros"] for r in vaca["registros"])

    for r in vaca["registros"]:
        print(f"{r['fecha']} → {r['litros']} litros")

    print(f"Total: {total} litros\n")


def produccion_por_fecha(produccion):
    fecha = input("Fecha: ")

    total = 0
    for v in produccion:
        for r in v["registros"]:
            if r["fecha"] == fecha:
                total += r["litros"]

    print(f"Total producido en {fecha}: {total} litros.\n")


def vaca_mas_productiva(animales, produccion):
    if not produccion:
        print("Sin vacas en el sistema.\n")
        return

    mas = None
    mayor = 0

    for v in produccion:
        total = sum(r["litros"] for r in v["registros"])
        if total > mayor:
            mayor = total
            mas = v

    print(f"La vaca más productiva es {mas['id']} con {mayor} litros.\n")


def resumen_general(produccion):
    total = 0
    registros = 0

    for v in produccion:
        for r in v["registros"]:
            total += r["litros"]
            registros += 1

    print("\n--- Resumen General ---")
    print(f"Total litros producidos: {total}")
    print(f"Registros totales: {registros}\n")
