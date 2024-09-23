class Caballo:
    def __init__(self, una_energia, una_raza):
        self.energia = una_energia
        self.raza = una_raza

    def comer(self, gramos):
        self.energia += gramos * 2

    def galopar(self, kms):
        self.energia -= kms


caballo = Caballo(100, "Pura Sangre")


caballo.comer(100)
caballo.comer(300)
caballo.galopar(10)
caballo.galopar(20)
