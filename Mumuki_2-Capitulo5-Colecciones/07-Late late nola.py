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
        self.libros = []

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise ValueError("El objeto debe ser una instancia de la clase Libro")
        
        if libro.titulo not in [libro_existente.titulo for libro_existente in self.libros]:
            self.libros.append(libro)
            return True  # El libro fue agregado con éxito
        return False  # El libro ya estaba en la biblioteca

    def libros_largos(self):
        return [libro for libro in self.libros if libro.es_largo()]

    def titulos_disponibles(self):
        return [libro.titulo for libro in self.libros]