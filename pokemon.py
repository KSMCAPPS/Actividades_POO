class Pokemon:
    contador = 0  # Variable de clase para contar Pokémon

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        Pokemon.contador += 1
        print(f"¡{self.nombre} ha sido capturado! ")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado ")
        Pokemon.contador -= 1

    def entrenar(self, ataque_extra=1, defensa_extra=1, salud_extra=2):
        self.nivel += 1
        self.ataque += ataque_extra
        self.defensa += defensa_extra
        self.salud += salud_extra
        print(f"{self.nombre} ha entrenado y ahora está en nivel {self.nivel} ")

    def mostrar_info(self):
        print(f"""
    Información de {self.nombre}
Tipo: {self.tipo}
Nivel: {self.nivel}
Ataque: {self.ataque}
Defensa: {self.defensa}
Salud: {self.salud}
""")

    def atacar(self, objetivo):
        daño = self.ataque - objetivo.defensa
        daño = max(daño, 0)
        objetivo.salud -= daño
        objetivo.salud = max(objetivo.salud, 0)
        print(f"{self.nombre} atacó a {objetivo.nombre} causando {daño} de daño ")

    def mostrar_total():
        print(f"Actualmente hay {Pokemon.contador} Pokémon en el mundo ")