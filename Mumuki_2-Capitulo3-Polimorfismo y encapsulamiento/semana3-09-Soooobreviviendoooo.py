class Sobreviviente:
    def __init__(self, adrenalina):
        self.adrenalina = adrenalina

    def atacar(self, contrincante):
        if not contrincante.es_un_peligro():
            contrincante.recibir_danio(self.adrenalina / 2)
            self.adrenalina += 20