class PlantaCarnivoraZombi:
    def __init__(self, clorofila):
        self.clorofila = clorofila

    def es_un_peligro(self):
        return self.clorofila > 40

    def hacer_fotosintesis(self, minutos):
        self.clorofila += minutos

    def recibir_danio(self, cantidad, *args):
        self.clorofila -= 10