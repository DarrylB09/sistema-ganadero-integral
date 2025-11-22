# registro_ganado.py
# Subsistema: Registro general de ganado

CATEGORIAS = [
    "Vaca de ordeño",
    "Vaca seca",
    "Toro",
    "Novillo",
    "Ternero",
    "Ganado de engorde",
]


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
            print("Opción no válida.\n")


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


# --------- FUNCIONES DE APOYO --------- #

def pedir_float(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Formato incorrecto. Ingresa un número válido.\n")


def elegir_categoria():
    print("\nElige la categoría del animal:")
    for i, cat in enumerate(CATEGORIAS, start=1):
        print(f"{i}. {cat}")

    while True:
        opcion = input("Opción: ").strip()
        if opcion.isdigit():
            indice = int(opcion)
            if 1 <= indice <= len(CATEGORIAS):
                return CATEGORIAS[indice - 1]
        print("Opción inválida. Intenta de nuevo.\n")


def crear_animal(id_animal, nombre, raza, edad, peso, sexo, categoria, notas):
    return {
        "id": id_animal,
        "nombre": nombre,
        "raza": raza,
        "edad": edad,
        "peso": peso,
        "sexo": sexo,
        "categoria": categoria,
        "notas": notas,
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
        return {"total": 0, "peso_total": 0, "promedio": 0, "categorias": {}}

    total = len(animales)
    peso_total = sum(a["peso"] for a in animales)
    categorias = {}

    for a in animales:
        cat = a["categoria"]
        categorias[cat] = categorias.get(cat, 0) + 1

    return {
        "total": total,
        "peso_total": peso_total,
        "promedio": peso_total / total,
        "categorias": categorias,
    }


# --------- INTERACCIÓN --------- #

def registrar_animal(animales):
    print("\n--- Registrar nuevo animal ---")
    id_animal = input("ID del animal: ").strip()
    if buscar_animal_por_id(animales, id_animal):
        print("Ya existe un animal con ese ID.\n")
        return

    nombre = input("Nombre: ").strip()
    raza = input("Raza: ").strip()
    edad = pedir_float("Edad (años): ")
    peso = pedir_float("Peso (kg): ")
    sexo = input("Sexo (M/H): ").strip().upper()
    categoria = elegir_categoria()
    notas = input("Notas (opcional): ").strip()

    animal = crear_animal(id_animal, nombre, raza, edad, peso, sexo, categoria, notas)
    animales.append(animal)
    print(f"Animal '{nombre}' registrado correctamente.\n")


def listar_animales(animales):
    print("\n--- Lista de animales registrados ---")
    if not animales:
        print("No hay animales registrados.\n")
        return

    for a in animales:
        print(
            f"ID:{a['id']} | Nombre:{a['nombre']} | Raza:{a['raza']} | "
            f"Edad:{a['edad']} años | Peso:{a['peso']} kg | Sexo:{a['sexo']} | "
            f"Categoría:{a['categoria']}"
        )
    print()


def buscar_animal_por_id_interactivo(animales):
    print("\n--- Buscar animal por ID ---")
    if not animales:
        print("No hay animales registrados.\n")
        return

    id_animal = input("ID: ").strip()
    a = buscar_animal_por_id(animales, id_animal)
    if not a:
        print("No se encontró un animal con ese ID.\n")
        return

    print("\nInformación del animal:")
    for k, v in a.items():
        print(f"{k.capitalize()}: {v}")
    print()


def actualizar_peso(animales):
    print("\n--- Actualizar peso ---")
    if not animales:
        print("No hay animales registrados.\n")
        return

    id_animal = input("ID del animal: ").strip()
    a = buscar_animal_por_id(animales, id_animal)
    if not a:
        print("No se encontró ese ID.\n")
        return

    print(f"Peso actual de {a['nombre']}: {a['peso']} kg")
    nuevo_peso = pedir_float("Nuevo peso (kg): ")
    a["peso"] = nuevo_peso
    print("Peso actualizado.\n")


def eliminar_animal(animales):
    print("\n--- Eliminar animal ---")
    if not animales:
        print("No hay animales registrados.\n")
        return

    id_animal = input("ID a eliminar: ").strip()
    if eliminar_animal_por_id(animales, id_animal):
        print("Animal eliminado.\n")
    else:
        print("No se encontró ese ID.\n")


def mostrar_estadisticas(animales):
    print("\n--- Estadísticas del hato ---")
    stats = calcular_estadisticas_hato(animales)
    if stats["total"] == 0:
        print("No hay datos.\n")
        return

    print(f"Total de animales: {stats['total']}")
    print(f"Peso total: {stats['peso_total']} kg")
    print(f"Peso promedio: {stats['promedio']:.2f} kg")
    print("Animales por categoría:")
    for cat, n in stats["categorias"].items():
        print(f" - {cat}: {n}")
    print()
