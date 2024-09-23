class Libro:
    def __init__(self, titulo, paginas, genero, autoria):
        self.titulo = titulo
        self.paginas = paginas
        self.genero = genero
        self.autoria = autoria

    def es_largo(self):
        return self.paginas > 300

    def nacionalidad(self):
        return self.autoria["nacionalidad"]

class Biblioteca:
    def __init__(self):
        self.libros = set()

    def agregar_libro(self, libro):
        self.libros.add(libro)

    def libros_largos(self):
        return [libro for libro in self.libros if libro.es_largo()]

    def titulos_disponibles(self):
        return [libro.titulo for libro in self.libros]