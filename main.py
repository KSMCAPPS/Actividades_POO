from clases.pokemon import Pokemon

pokemones = []

def capturar_pokemon():
    nombre = input("Nombre del Pokémon: ")
    tipo = input("Tipo: ")

    try:
        ataque = int(input("Ataque: "))
        defensa = int(input("Defensa: "))
        salud = int(input("Salud: "))
    except ValueError:
        print(" Ingresa solo números para ataque, defensa y salud.")
        return

    nuevo = Pokemon(nombre, tipo, ataque, defensa, salud)
    pokemones.append(nuevo)

def entrenar_pokemon():
    if not pokemones:
        print("No hay Pokémon para entrenar.")
        return

    for i, p in enumerate(pokemones):
        print(f"{i+1}. {p.nombre}")

    try:
        eleccion = int(input("¿Cuál quieres entrenar? ")) - 1
        ataque = int(input("Mejora de ataque (default 1): ") or "1")
        defensa = int(input("Mejora de defensa (default 1): ") or "1")
        salud = int(input("Mejora de salud (default 2): ") or "2")
        pokemones[eleccion].entrenar(ataque, defensa, salud)
    except (ValueError, IndexError):
        print(" Entrada inválida.")

def mostrar_todos():
    if not pokemones:
        print("No hay Pokémon capturados.")
        return

    for p in pokemones:
        p.mostrar_info()

def liberar_pokemon():
    if not pokemones:
        print("No hay Pokémon para liberar.")
        return

    for i, p in enumerate(pokemones):
        print(f"{i+1}. {p.nombre}")

    try:
        eleccion = int(input("¿Cuál quieres liberar? ")) - 1
        liberado = pokemones.pop(eleccion)
        del liberado
    except (ValueError, IndexError):
        print(" Entrada inválida.")

def mostrar_total_pokemons():
    Pokemon.mostrar_total()

def menu():
    while True:
        print("""
    MENÚ PRINCIPAL 
1. Capturar nuevo Pokémon 
2. Entrenar Pokémon 
3. Ver información de todos 
4. Ver total de Pokémon 
5. Liberar un Pokémon 
6. Salir
""")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_todos()
        elif opcion == "4":
            mostrar_total_pokemons()
        elif opcion == "5":
            liberar_pokemon()
        elif opcion == "6":
            print("¡Hasta la próxima aventura Pokémon! ")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()