class Notebook:
  def __init__(self, bateria):
    self.bateria = bateria
    
  def utilizar(self, minutos):
    self.bateria -= minutos
    
  def tiene_bateria(self):
      return self.bateria > 20
    
  def tiene_bateria_maxima(self):
      return self.bateria == 100
    
  def cargar_a_tope(self):
      self.bateria = 100