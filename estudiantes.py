def capturar_calificaciones():
    try:
        estudiantes = int(input("¿Cuántos estudiantes hay en el grupo? "))
        materias = int(input("¿Cuántas materias tiene el grupo? "))

        if estudiantes <= 0 or materias <= 0:
            raise ValueError("Debe haber al menos un estudiante y una materia.")

        matriz = []

        for i in range(estudiantes):
            print(f"\nEstudiante {i+1}:")
            fila = []
            for j in range(materias):
                while True:
                    try:
                        nota = float(input(f"  Calificación en materia {j+1} (0–100): "))
                        if 0 <= nota <= 100:
                            fila.append(nota)
                            break
                        else:
                            print(" Calificación fuera de rango. Intenta de nuevo.")
                    except ValueError:
                        print(" Entrada inválida. Usa números.")
            matriz.append(fila)

        return matriz, estudiantes, materias

    except Exception as e:
        print("Error al capturar datos:", e)
        return [], 0, 0


def calcular_promedios(matriz, estudiantes, materias):
    print("\n Promedio por estudiante:")
    for i in range(estudiantes):
        promedio = sum(matriz[i]) / materias
        print(f"  Estudiante {i+1}: {promedio}")

    print("\nPromedio por materia:")
    for j in range(materias):
        suma = sum(matriz[i][j] for i in range(estudiantes))
        promedio = suma / estudiantes
        print(f"  Materia {j+1}: {promedio}")


def buscar_extremos(matriz):
    todas = [nota for fila in matriz for nota in fila]
    maximo = max(todas)
    minimo = min(todas)
    print(f"\nCalificación más alta: {maximo}")
    print(f"Calificación más baja: {minimo}")


def main():
    matriz, estudiantes, materias = capturar_calificaciones()
    if estudiantes > 0 and materias > 0:
        calcular_promedios(matriz, estudiantes, materias)
        buscar_extremos(matriz)
        print("\n Análisis completo.")
    else:
        print("No se pudo procesar la matriz.")

if __name__ == "__main__":
    main()