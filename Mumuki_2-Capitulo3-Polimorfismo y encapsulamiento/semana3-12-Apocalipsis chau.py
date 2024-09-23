class Pasta:
    def __init__(self):
        self.ajies = 0

    def picantear(self):
        self.ajies += 5
        if self.ajies > 10:
            raise Exception("El plato ya está demasiado picante")

    def suavizar(self):
        self.ajies -= 1

class Pizza:
    def __init__(self):
        self.condimento = "adobo"

    def picantear(self):
        if self.condimento == "cayena":
            raise Exception("El plato ya está demasiado picante")
        self.condimento = "cayena"

    def suavizar(self):
        self.condimento = "orégano"

class Chef:
    def __init__(self, plato_del_dia):
        self.plato_del_dia = plato_del_dia

    def picantear(self):
        self.plato_del_dia.picantear()
        
        
class AyudanteDeCocina:
    def suavizar(self, plato):
        plato.suavizar()