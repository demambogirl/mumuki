class EstudianteDeVeterinaria:
    def alimentar(self, un_animal, una_comida, rehabilitar):
        un_animal.comer(una_comida)
        
    def rehabilitar(self, un_animal):
        un_animal.recibir_rehabilitacion()

class Animal:
    peso = 0
    rehabilitado = False

    
    def comer(self, cantidad):
        self.peso += cantidad
        
    def recibir_rehabilitacion(self):
      self.rehabilitado = True
        

estudiante = EstudianteDeVeterinaria()

caballo = Animal()
estudiante.alimentar(caballo, 800, 'rehabilitar')

gato = Animal()
estudiante.alimentar(gato, 300, 'rehabilitar')

golondrina = Animal()
estudiante.alimentar(golondrina, 40, 'rehabilitar')
