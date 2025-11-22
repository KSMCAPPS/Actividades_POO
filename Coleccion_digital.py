import pickle
ARCHIVO_TXT = "stranger_things.txt"
ARCHIVO_BIN = "stranger_things.bin"
def agregar_elemento():
    try:
        nombre = input("Nombre del personaje: ")
        anio = input("Año de aparición: ")
        creador = "Stranger Things (Netflix)"
        calificacion = input("Calificación (1-10): ")

        with open(ARCHIVO_TXT, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{anio},{creador},{calificacion}\n")

        popularidad = int(input("Popularidad (1-100): "))
        rareza = int(input("Rareza (1-100): "))

        try:
            datos = {}
            with open(ARCHIVO_BIN, "rb") as fb:
                datos = pickle.load(fb)
        except FileNotFoundError:
            datos = {}

        datos[nombre] = (popularidad, rareza)

        with open(ARCHIVO_BIN, "wb") as fb:
            pickle.dump(datos, fb)

        print(" Elemento agregado correctamente.")
    except Exception as e:
        print(" Error al agregar:", e)

def mostrar_coleccion():
    try:
        with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
            print("\n Colección completa:")
            for linea in f:
                print(linea.strip())
    except FileNotFoundError:
        print(" No existe el archivo de texto.")

def buscar_elemento():
    nombre = input("Nombre a buscar: ")
    try:
        with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
            encontrado = False
            for linea in f:
                if nombre.lower() in linea.lower():
                    print(" Encontrado:", linea.strip())
                    encontrado = True
            if not encontrado:
                print(" No se encontró el personaje.")
    except FileNotFoundError:
        print(" No existe el archivo de texto.")

def mostrar_binarios():
    try:
        with open(ARCHIVO_BIN, "rb") as fb:
            datos = pickle.load(fb)
            print("\n Datos binarios:")
            for nombre, (pop, rare) in datos.items():
                print(f"{nombre}: Popularidad={pop}, Rareza={rare}")
    except FileNotFoundError:
        print(" No existe el archivo binario.")

def menu():
    while True:
        print("\n===== MI COLECCIÓN DIGITAL =====")
        print("1. Agregar elemento")
        print("2. Mostrar colección completa")
        print("3. Buscar elemento por nombre")
        print("4. Mostrar datos binarios")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_elemento()
        elif opcion == "2":
            mostrar_coleccion()
        elif opcion == "3":
            buscar_elemento()
        elif opcion == "4":
            mostrar_binarios()
        elif opcion == "5":
            print(" Byee")
            break
        else:
            print(" Opción inválida.")
            
menu()