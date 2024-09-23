class EstudianteDeVeterinaria:
    def alimentar(self, un_animal, una_comida):
        un_animal.comer(una_comida)

class Animal:
    peso = 0
    
    def comer(self, cantidad):
        self.peso += cantidad

estudiante = EstudianteDeVeterinaria()

caballo = Animal()
estudiante.alimentar(caballo, 800)

gato = Animal()
estudiante.alimentar(gato, 300)

golondrina = Animal()
estudiante.alimentar(golondrina, 40)