# registro_ganado.py
# Subsistema: Registro general de ganado

def sistema_registro_ganado(animales):

    while True:
        mostrar_menu_registro()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_animal(animales)
        elif opcion == "2":
            listar_animales(animales)
        elif opcion == "3":
            buscar_animal_por_id_interactivo(animales)
        elif opcion == "4":
            actualizar_peso(animales)
        elif opcion == "5":
            eliminar_animal(animales)
        elif opcion == "6":
            mostrar_estadisticas(animales)
        elif opcion == "0":
            print("Volviendo al menú principal...\n")
            break
        else:
            print("Opción inválida.\n")


def mostrar_menu_registro():
    print("======================================")
    print("       SISTEMA DE REGISTRO GANADERO")
    print("======================================")
    print("1. Registrar nuevo animal")
    print("2. Listar todos los animales")
    print("3. Buscar animal por ID")
    print("4. Actualizar peso de un animal")
    print("5. Eliminar animal del registro")
    print("6. Ver estadísticas del hato")
    print("0. Volver al menú principal")
    print("======================================")


# ----------- LÓGICA ----------- #

def crear_animal(id_animal, nombre, raza, edad, peso, sexo, categoria, notas):
    return {
        "id": id_animal,
        "nombre": nombre,
        "raza": raza,
        "edad": edad,
        "peso": peso,
        "sexo": sexo,
        "categoria": categoria,
        "notas": notas
    }


def buscar_animal_por_id(animales, id_animal):
    for animal in animales:
        if animal["id"] == id_animal:
            return animal
    return None


def eliminar_animal_por_id(animales, id_animal):
    for i, animal in enumerate(animales):
        if animal["id"] == id_animal:
            animales.pop(i)
            return True
    return False


def calcular_estadisticas_hato(animales):
    if not animales:
        return {"total":0, "peso_total":0, "promedio":0, "categorias":{}}

    total = len(animales)
    peso_total = sum(a["peso"] for a in animales)

    categorias = {}
    for a in animales:
        categorias[a["categoria"]] = categorias.get(a["categoria"],0) + 1

    return {
        "total": total,
        "peso_total": peso_total,
        "promedio": peso_total / total,
        "categorias": categorias
    }


# ----------- INTERACCIÓN ----------- #

def registrar_animal(animales):
    print("\n--- Registrar nuevo animal ---")

    id_animal = input("ID: ").strip()
    if buscar_animal_por_id(animales, id_animal):
        print("Ese ID ya existe.\n")
        return

    nombre = input("Nombre: ").strip()
    raza = input("Raza: ").strip()
    edad = float(input("Edad (años): "))
    peso = float(input("Peso (kg): "))
    sexo = input("Sexo (M/H): ").strip().upper()
    categoria = input("Categoría: ").strip()
    notas = input("Notas: ").strip()

    animales.append(
        crear_animal(id_animal, nombre, raza, edad, peso, sexo, categoria, notas)
    )
    print("Animal registrado.\n")


def listar_animales(animales):
    print("\n--- Lista del ganado ---")
    if not animales:
        print("Sin animales.\n")
        return

    for a in animales:
        print(f"ID:{a['id']} | {a['nombre']} | {a['raza']} | {a['peso']}kg | {a['categoria']}")
    print()


def buscar_animal_por_id_interactivo(animales):
    id_animal = input("ID: ").strip()
    a = buscar_animal_por_id(animales, id_animal)

    if not a:
        print("No encontrado.\n")
        return

    print("\n--- Datos del animal ---")
    for k,v in a.items():
        print(f"{k.capitalize()}: {v}")
    print()


def actualizar_peso(animales):
    id_animal = input("ID del animal: ").strip()
    a = buscar_animal_por_id(animales, id_animal)

    if not a:
        print("ID no encontrado.\n")
        return

    nuevo = float(input("Nuevo peso: "))
    a["peso"] = nuevo
    print("Peso actualizado.\n")


def eliminar_animal(animales):
    id_animal = input("ID a eliminar: ").strip()
    if eliminar_animal_por_id(animales, id_animal):
        print("Eliminado.\n")
    else:
        print("No encontrado.\n")


def mostrar_estadisticas(animales):
    stats = calcular_estadisticas_hato(animales)
    if stats["total"] == 0:
        print("Sin datos.\n")
        return

    print("\n--- Estadísticas del hato ---")
    print(f"Total animales: {stats['total']}")
    print(f"Peso total: {stats['peso_total']} kg")
    print(f"Promedio: {stats['promedio']:.2f} kg")
    print("Categorías:")
    for c,n in stats["categorias"].items():
        print(f"  - {c}: {n}")
    print()
