class Golondrina:
    def __init__(self, una_energia, una_ciudad):
        self.energia = una_energia
        self.ciudad = una_ciudad
    
    def comer(self, gramos):
        self.energia += gramos * 0.5

    def volar_hacia(self, una_ciudad):
        self.ciudad = una_ciudad
        self.energia *= 0.5
