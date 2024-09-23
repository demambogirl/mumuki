class Celular:
  def __init__(self, una_bateria, un_saldo):
    self.bateria = una_bateria
    self.saldo = un_saldo

  def cargar_a_tope(self):
      self.bateria = 100

  def necesita_saldo(self):
    return self.saldo == 0