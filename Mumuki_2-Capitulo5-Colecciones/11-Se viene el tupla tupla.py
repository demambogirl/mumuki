class Persona:
    def __init__(self, un_nombre, un_segundo_nombre, un_apellido):
        self.nombre = un_nombre
        self.segundo_nombre = un_segundo_nombre
        self.apellido = un_apellido

    def iniciales(self):
        return (self.nombre[0], self.segundo_nombre[0], self.apellido[0])

