nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    cantidad = int(input("¿Cuántas canciones deseas agregar? "))
    for i in range(cantidad):
        print(f"\nCanción {i+1}:")
        nombre = input("Nombre: ")
        artista = input("Artista: ")
        duracion = float(input("Duración en minutos: "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

def ver_reportes():
    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    max_pop = max(popularidades) if popularidades else 0
    min_pop = min(popularidades) if popularidades else 0
    promedio_pop = (sum(popularidades) / total_canciones) if total_canciones > 0 else 0

    cancion_mas_popular = nombres[popularidades.index(max_pop)] if total_canciones > 0 else "N/A"
    cancion_menos_popular = nombres[popularidades.index(min_pop)] if total_canciones > 0 else "N/A"

    print("\n Reportes:")
    print(f"Total de canciones: {total_canciones}")
    print(f"Duración total de la playlist: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {cancion_mas_popular} ({max_pop})")
    print(f"Canción menos popular: {cancion_menos_popular} ({min_pop})")
    print(f"Promedio de popularidad: {promedio_pop:.2f}")

def buscar_canciones():
    print("\n Buscar canciones:")
    print("1. Por artista")
    print("2. Por rango de popularidad")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        artista_buscar = input("Nombre del artista: ")
        print(f"\nCanciones de {artista_buscar}:")
        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar.lower():
                print(f"- {nombres[i]} ({popularidades[i]})")
    elif opcion == "2":
        min_pop = int(input("Popularidad mínima: "))
        max_pop = int(input("Popularidad máxima: "))
        print(f"\nCanciones con popularidad entre {min_pop} y {max_pop}:")
        for i in range(len(nombres)):
            if min_pop <= popularidades[i] <= max_pop:
                print(f"- {nombres[i]} ({popularidades[i]})")
    else:
        print("Opción inválida.")

def playlist_recomendada():
    promedio_pop = (sum(popularidades) / len(popularidades)) if len(popularidades) > 0 else 0
    print("\n🎧 Playlist recomendada (popularidad > promedio):")
    for i in range(len(nombres)):
        if popularidades[i] > promedio_pop:
            print(f"- {nombres[i]} ({popularidades[i]})")

def menu():
    salir = False
    while not salir:
        print("\n Festival Playlist ")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_canciones()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            playlist_recomendada()
        elif opcion == "5":
            print("¡Hasta luego")
            salir = True
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar menú principal
menu()