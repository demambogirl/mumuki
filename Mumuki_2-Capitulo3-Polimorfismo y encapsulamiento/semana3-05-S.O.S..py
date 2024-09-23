class Caballo:
    def __init__(self, una_energia, una_raza):
        self.energia = una_energia
        self.raza = una_raza

    def comer(self, gramos):
        self.energia += gramos * 2

    def galopar(self, kms):
        self.energia -= kms

    def recibir_rehabilitacion(self):
        self.galopar(3)  
        self.comer(3000)  
        self.galopar(5) 


class Golondrina:
    def __init__(self, una_energia, una_ciudad):
        self.energia = una_energia
        self.ciudad = una_ciudad

    def comer(self, gramos):
        self.energia += gramos / 2

    def volar_hacia(self, destino):
        self.ciudad = destino
        self.energia /= 2

    def recibir_rehabilitacion(self):
        self.volar_hacia("Lihuel Calel") 