class Tablet:
  def __init__(self, tiene_bateria):
    self.bateria = tiene_bateria
    
  def utilizar(self, minutos):
      self.bateria -= minutos / 2
    
    
  def tiene_bateria(self):
      return self.bateria > 20
    
  def tiene_bateria_maxima(self):
      return self.bateria == 100
    
  def cargar_a_tope(self):
      self.bateria = 100