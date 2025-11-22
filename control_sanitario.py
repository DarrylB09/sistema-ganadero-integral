# control_sanitario.py
# Subsistema: Control sanitario del hato

from datetime import datetime
from registro_ganado import CATEGORIAS


def sistema_control_sanitario(animales, fichas):
    while True:
        mostrar_menu_sanitario()
        op = input("Opción: ").strip()

        if op == "1":
            crear_ficha_sanitaria(animales, fichas)
        elif op == "2":
            registrar_o_actualizar_vacuna(fichas)
        elif op == "3":
            registrar_tratamiento(fichas)
        elif op == "4":
            ver_historial(fichas)
        elif op == "5":
            vacunas_atrasadas(fichas)
        elif op == "0":
            print("Volviendo al menú principal...\n")
            break
        else:
            print("Opción no válida.\n")


def mostrar_menu_sanitario():
    print("======================================")
    print("     SISTEMA DE CONTROL SANITARIO")
    print("======================================")
    print("1. Crear ficha sanitaria")
    print("2. Registrar/actualizar vacuna")
    print("3. Registrar tratamiento")
    print("4. Ver historial sanitario")
    print("5. Ver animales con vacunas atrasadas")
    print("0. Volver")
    print("======================================")


# ---------- APOYO ---------- #

def pedir_fecha(mensaje):
    while True:
        fecha_str = input(mensaje).strip()
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha_str
        except ValueError:
            print("Formato incorrecto. Usa YYYY-MM-DD.\n")


def elegir_categoria():
    print("\nSelecciona la categoría:")
    for i, cat in enumerate(CATEGORIAS, start=1):
        print(f"{i}. {cat}")

    while True:
        op = input("Opción: ").strip()
        if op.isdigit():
            idx = int(op)
            if 1 <= idx <= len(CATEGORIAS):
                return CATEGORIAS[idx - 1]
        print("Opción inválida.\n")


def animales_en_categoria(animales, categoria):
    return [a for a in animales if a["categoria"] == categoria]


def buscar_ficha_por_id(fichas, id_animal):
    for f in fichas:
        if f["id"] == id_animal:
            return f
    return None


# ---------- FUNCIONALIDAD ---------- #

def crear_ficha_sanitaria(animales, fichas):
    print("\n--- Crear ficha sanitaria ---")
    if not animales:
        print("No hay animales registrados.\n")
        return

    categoria = elegir_categoria()
    lista = animales_en_categoria(animales, categoria)

    if not lista:
        print(f"No hay animales en la categoría '{categoria}'.\n")
        return

    print(f"Animales en categoría '{categoria}':")
    for a in lista:
        print(f"ID:{a['id']} | Nombre:{a['nombre']}")

    id_animal = input("Ingresa el ID del animal: ").strip()
    animal = next((a for a in lista if a["id"] == id_animal), None)

    if not animal:
        print("ID no válido para esa categoría.\n")
        return

    if buscar_ficha_por_id(fichas, id_animal):
        print("Ya existe una ficha sanitaria para ese animal.\n")
        return

    ficha = {
        "id": id_animal,
        "nombre": animal["nombre"],
        "ultima": None,
        "proxima": None,
        "tratamientos": [],
    }
    fichas.append(ficha)
    print(f"Ficha sanitaria creada para '{animal['nombre']}'.\n")


def registrar_o_actualizar_vacuna(fichas):
    print("\n--- Registrar/actualizar vacuna ---")
    if not fichas:
        print("No hay fichas sanitarias registradas.\n")
        return

    id_animal = input("ID del animal: ").strip()
    ficha = buscar_ficha_por_id(fichas, id_animal)

    if not ficha:
        print("No se encontró ficha para ese ID.\n")
        return

    ultima = pedir_fecha("Fecha de última vacuna (YYYY-MM-DD): ")
    proxima = pedir_fecha("Fecha de próxima vacuna (YYYY-MM-DD): ")

    ficha["ultima"] = ultima
    ficha["proxima"] = proxima
    print("Datos de vacuna actualizados.\n")


def registrar_tratamiento(fichas):
    print("\n--- Registrar tratamiento ---")
    if not fichas:
        print("No hay fichas sanitarias.\n")
        return

    id_animal = input("ID del animal: ").strip()
    ficha = buscar_ficha_por_id(fichas, id_animal)

    if not ficha:
        print("No se encontró ficha para ese ID.\n")
        return

    fecha = pedir_fecha("Fecha del tratamiento (YYYY-MM-DD): ")
    descripcion = input("Descripción del tratamiento: ").strip()

    ficha["tratamientos"].append({"fecha": fecha, "desc": descripcion})
    print("Tratamiento registrado.\n")


def ver_historial(fichas):
    print("\n--- Historial sanitario ---")
    if not fichas:
        print("No hay fichas sanitarias.\n")
        return

    id_animal = input("ID del animal: ").strip()
    ficha = buscar_ficha_por_id(fichas, id_animal)

    if not ficha:
        print("No se encontró ficha para ese ID.\n")
        return

    print("\n======= HISTORIAL SANITARIO =======")
    print(f"Animal: {ficha['nombre']} (ID:{ficha['id']})")
    print(f"Última vacuna: {ficha['ultima'] or 'SIN REGISTRO'}")
    print(f"Próxima vacuna: {ficha['proxima'] or 'SIN REGISTRO'}")
    print("Tratamientos:")

    if not ficha["tratamientos"]:
        print("  No hay tratamientos registrados.")
    else:
        for t in ficha["tratamientos"]:
            print(f" - {t['fecha']}: {t['desc']}")
    print()


def vacunas_atrasadas(fichas):
    print("\n--- Animales con vacunas atrasadas ---")
    if not fichas:
        print("No hay fichas sanitarias.\n")
        return

    hoy_str = pedir_fecha("Fecha actual (YYYY-MM-DD): ")
    hoy = datetime.strptime(hoy_str, "%Y-%m-%d").date()

    encontrados = False

    for ficha in fichas:
        if ficha["proxima"]:
            try:
                fecha_prox = datetime.strptime(ficha["proxima"], "%Y-%m-%d").date()
            except ValueError:
                print(f"Fecha inválida en ficha de {ficha['nombre']}.")
                continue

            if fecha_prox < hoy:
                print(f"- {ficha['nombre']} (ID:{ficha['id']}) → vacuna vencida el {ficha['proxima']}")
                encontrados = True

    if not encontrados:
        print("No hay animales con vacunas atrasadas.\n")
    else:
        print()
