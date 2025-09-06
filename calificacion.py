calificacion = int(input("Ingresa tu calificación (0–100): "))

if 0 <= calificacion <= 100:
    if calificacion >= 90:
        print("A")
    elif calificacion >= 80:
        print("B")
    elif calificacion >= 70:
        print("C")
    elif calificacion >= 60:
        print("D")
    else:
        print("F")
else:
    print("La calificación debe estar entre 0 y 100.")
