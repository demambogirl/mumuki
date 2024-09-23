class MedioDeTransporte:
  def __init__(self, combustible):
    self.combustible = combustible

  def cargar_combustible(self, cantidad):
    self.combustible += cantidad

  def entran_personas(self, cantidad):
    return cantidad <= self.maximo_personas()
  
class Colectivo(MedioDeTransporte):
  def __init__(self, combustible):
    super().__init__(combustible)
    self.pasajeros = 0
  
  def entran_personas(self, cantidad):
    return True
  
  def recorrer(self, distancia):
    consumo = distancia * 2
    if consumo <= self.combustible:
      self.combustible -= consumo

  def cargar_combustible(self, cantidad):
        super().cargar_combustible(cantidad)
        self.pasajeros = 0