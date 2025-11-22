# control_sanitario.py
from datetime import datetime


def sistema_control_sanitario(animales, fichas):

    while True:
        menu_sanitario()
        op = input("Opción: ")

        if op == "1":
            crear_ficha(animales, fichas)

        elif op == "2":
            registrar_vacuna(fichas)

        elif op == "3":
            registrar_tratamiento(fichas)

        elif op == "4":
            historial(fichas)

        elif op == "5":
            vacunas_atrasadas(fichas)

        elif op == "0":
            print("Volviendo...\n")
            break

        else:
            print("Opción inválida.\n")


def menu_sanitario():
    print("======================================")
    print("     SISTEMA DE CONTROL SANITARIO")
    print("======================================")
    print("1. Crear ficha sanitaria")
    print("2. Registrar vacuna")
    print("3. Registrar tratamiento")
    print("4. Ver historial sanitario")
    print("5. Vacunas atrasadas")
    print("0. Volver")
    print("======================================")


# --- LÓGICA ---

def crear_ficha(animales, fichas):
    id_a = input("ID animal: ").strip()

    if not any(a["id"] == id_a for a in animales):
        print("Ese animal NO existe en el registro.\n")
        return

    if any(f["id"] == id_a for f in fichas):
        print("Ya existe ficha.\n")
        return

    nombre = next(a["nombre"] for a in animales if a["id"] == id_a)

    fichas.append({
        "id": id_a,
        "nombre": nombre,
        "ultima": None,
        "proxima": None,
        "tratamientos": []
    })

    print("Ficha creada.\n")


def registrar_vacuna(fichas):
    id_a = input("ID: ")
    f = next((x for x in fichas if x["id"] == id_a), None)

    if not f:
        print("No hay ficha.\n")
        return

    u = input("Fecha última vacuna (YYYY-MM-DD): ")
    p = input("Fecha próxima vacuna (YYYY-MM-DD): ")

    f["ultima"] = u
    f["proxima"] = p
    print("Vacuna registrada.\n")


def registrar_tratamiento(fichas):
    id_a = input("ID: ")
    f = next((x for x in fichas if x["id"] == id_a), None)

    if not f:
        print("No existe ficha.\n")
        return

    fecha = input("Fecha: ")
    desc = input("Tratamiento: ")

    f["tratamientos"].append({"fecha": fecha, "desc": desc})
    print("Tratamiento guardado.\n")


def historial(fichas):
    id_a = input("ID: ")
    f = next((x for x in fichas if x["id"] == id_a), None)

    if not f:
        print("No existe ficha.\n")
        return

    print("\n--- Historial ---")
    print(f"Animal: {f['nombre']} (ID {f['id']})")
    print(f"Última vacuna: {f['ultima']}")
    print(f"Próxima vacuna: {f['proxima']}")
    print("Tratamientos:")

    for t in f["tratamientos"]:
        print(f" - {t['fecha']}: {t['desc']}")

    print()


def vacunas_atrasadas(fichas):
    if not fichas:
        print("No hay fichas sanitarias.\n")
        return

    hoy_str = input("Fecha actual (YYYY-MM-DD): ").strip()

    # Validación simple para evitar que el sistema se caiga
    try:
        hoy = datetime.strptime(hoy_str, "%Y-%m-%d").date()
    except ValueError:
        print("Formato incorrecto. Usa el formato YYYY-MM-DD.\n")
        return

    print("\n========== VACUNAS ATRASADAS ==========")

    encontrados = False

    for f in fichas:
        if f["proxima"]:
            try:
                fecha_p = datetime.strptime(f["proxima"], "%Y-%m-%d").date()
            except ValueError:
                print(f"Fecha inválida guardada en la ficha de {f['nombre']}.")
                continue

            if fecha_p < hoy:
                print(f"➡ {f['nombre']} (ID {f['id']}) — Vacuna vencida: {f['proxima']}")
                encontrados = True

    if not encontrados:
        print("No hay animales con vacunas atrasadas.\n")
    else:
        print()