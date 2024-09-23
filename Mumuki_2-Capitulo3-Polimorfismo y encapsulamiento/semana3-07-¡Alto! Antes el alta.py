class EstudianteDeVeterinaria:
    def alimentar(self, un_animal, una_comida, rehabilitar):
        un_animal.comer(una_comida)
        
    def rehabilitar(self, un_animal):
        un_animal.recibir_rehabilitacion()

    def puede_dar_el_alta(self, un_animal):
        return un_animal.esta_feliz()

class Animal:
    peso = 0
    rehabilitado = False
    
    def comer(self, cantidad):
        self.peso += cantidad
        
    def recibir_rehabilitacion(self):
        self.rehabilitado = True

class Gato(Animal):
    def __init__(self, una_energia, una_edad):
        self.energia = una_energia
        self.edad = una_edad
    
    def recibir_rehabilitacion(self):
        self.comer(400)

    def esta_feliz(self):
        return self.energia > 30

    def comer(self, gramos):
        self.energia += gramos

    def cumplir_anios(self):
        self.edad += 1
    
class Caballo(Animal):
    def __init__(self, una_energia, una_raza):
        self.energia = una_energia
        self.raza = una_raza

    def comer(self, gramos):
        self.energia += gramos * 2

    def galopar(self, kms):
        self.energia -= kms

    def recibir_rehabilitacion(self):
        self.galopar(3)  
        self.comer(3000)  
        self.galopar(5)

    def esta_feliz(self):
        return True

class Golondrina(Animal):
    def __init__(self, una_energia, una_ciudad):
        self.energia = una_energia
        self.ciudad = una_ciudad

    def comer(self, gramos):
        self.energia += gramos / 2

    def volar_hacia(self, destino):
        self.ciudad = destino
        self.energia /= 2

    def recibir_rehabilitacion(self):
        self.volar_hacia("Lihuel Calel")

    def esta_feliz(self):
        return self.ciudad == "Lihuel Calel"