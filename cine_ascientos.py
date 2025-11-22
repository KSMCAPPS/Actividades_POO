filas = int(input("Número de filas del cine: "))
columnas = int(input("Número de columnas (asientos por fila): "))

sala = [["L"] * columnas for _ in range(filas)]

def mostrar_sala():
    for fila in sala:
        print(" ".join(fila))

def reservar_asiento():
    f = int(input("Fila: ")) - 1
    c = int(input("Columna: ")) - 1
    if f < 0 or f >= filas or c < 0 or c >= columnas:
        print("Ese asiento no existe.")
    elif sala[f][c] == "X":
        print(" El asiento ya está ocupado.")
    else:
        sala[f][c] = "X"
        print(" Asiento reservado.")

def liberar_asiento():
    f = int(input("Fila: ")) - 1
    c = int(input("Columna: ")) - 1
    if f < 0 or f >= filas or c < 0 or c >= columnas:
        print(" Ese asiento no existe.")
    elif sala[f][c] == "L":
        print(" El asiento ya está libre.")
    else:
        sala[f][c] = "L"
        print(" Asiento liberado.")

def contar_asientos():
    libres = sum(fila.count("L") for fila in sala)
    ocupados = sum(fila.count("X") for fila in sala)
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")

# Menú principal
while True:
    print("\n Menú Cine ")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_sala()
    elif opcion == "2":
        reservar_asiento()
    elif opcion == "3":
        liberar_asiento()
    elif opcion == "4":
        contar_asientos()
    elif opcion == "5":
        print(" Gracias por usar el sistema de cine.")
        break
    else:
        print(" Opción inválida.")