class Planeta:
    contador_planetas = 0  
    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia 
        Planeta.contador_planetas += 1
        print(f" Planeta '{self.nombre}' registrado.")

    def __del__(self):
        print(f" Planeta '{self.nombre}' eliminado.")


class NaveEspacial:
    contador_naves = 0  

    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad  
        self.destino = None
        self.misiones = []
        self.recursos = {}
        NaveEspacial.contador_naves += 1
        print(f" Nave '{self.nombre}' registrada.")

    def __del__(self):
        print(f" Nave '{self.nombre}' destruida.")

    def asignar_destino(self, planeta):
        self.destino = planeta
        print(f" Destino asignado: {planeta.nombre}")

    def calcular_tiempo_viaje(self):
        if self.destino:
            tiempo = self.destino.distancia / self.velocidad
            print(f" Tiempo estimado de viaje a {self.destino.nombre}: {tiempo:.2f} horas")
        else:
            print(" No se ha asignado un destino.")

    def cargar_mision(self, *args, **kwargs):
        self.misiones.extend(args)
        self.recursos.update(kwargs)
        print(f" Misiones cargadas: {args}")
        print(f" Recursos asignados: {kwargs}")

    def mostrar_info(self):
        print(f"\n Información de la nave '{self.nombre}':")
        print(f"Velocidad: {self.velocidad} millones km/h")
        if self.destino:
            print(f"Destino: {self.destino.nombre}")
        print(f"Misiones: {self.misiones}")
        print(f"Recursos: {self.recursos}")



planetas = []
naves = []

def mostrar_menu():
    print("\n MENÚ INTERPLANETARIO")
    print("1. Registrar planeta")
    print("2. Registrar nave")
    print("3. Asignar destino")
    print("4. Calcular tiempo de viaje")
    print("5. Mostrar información")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del planeta: ")
        distancia = float(input("Distancia desde la Tierra (millones de km): "))
        planetas.append(Planeta(nombre, distancia))

    elif opcion == "2":
        nombre = input("Nombre de la nave: ")
        velocidad = float(input("Velocidad (millones de km/h): "))
        nave = NaveEspacial(nombre, velocidad)
        misiones = input("Misiones (separadas por coma): ").split(",")
        recursos = input("Recursos (clave=valor separados por coma): ")
        recursos_dict = dict(item.split("=") for item in recursos.split(",") if "=" in item)
        nave.cargar_mision(*misiones, **recursos_dict)
        naves.append(nave)

    elif opcion == "3":
        if not planetas or not naves:
            print(" Primero registra al menos una nave y un planeta.")
            continue
        for i, nave in enumerate(naves):
            print(f"{i+1}. {nave.nombre}")
        nave_idx = int(input("Selecciona la nave: ")) - 1

        for i, planeta in enumerate(planetas):
            print(f"{i+1}. {planeta.nombre}")
        planeta_idx = int(input("Selecciona el planeta: ")) - 1

        naves[nave_idx].asignar_destino(planetas[planeta_idx])

    elif opcion == "4":
        for i, nave in enumerate(naves):
            print(f"{i+1}. {nave.nombre}")
        nave_idx = int(input("Selecciona la nave: ")) - 1
        naves[nave_idx].calcular_tiempo_viaje()

    elif opcion == "5":
        print(f"\n Total de planetas registrados: {Planeta.contador_planetas}")
        print(f" Total de naves registradas: {NaveEspacial.contador_naves}")
        for nave in naves:
            nave.mostrar_info()

    elif opcion == "6":
        print(" Cerrando el sistema interplanetario...")
        break

    else:
        print(" Opción inválida. Intenta de nuevo.")
