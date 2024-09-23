class Gato:
  def __init__(self,una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad
    
  def recibir_rehabilitacion(self):
      self.comer(400)

  def comer(self,gramos):
    self.energia += gramos

  def cumplir_anios(self):
    self.edad += 1
    
class EstudianteDeVeterinaria:
    def rehabilitar(self, un_animal):
        un_animal.recibir_rehabilitacion()
        
pelu = EstudianteDeVeterinaria()
perez = Gato(30, 8)
pelu.rehabilitar(perez)