class Libro:
  def __init__(self, titulo, paginas, genero):
    self.titulo = titulo
    self.paginas = paginas
    self.genero = genero
     
  def es_largo(self):
    return self.paginas > 300
  

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
        else:
            raise ValueError("El objeto debe ser una instancia de la clase Libro")

    def libros_largos(self):
        return [libro for libro in self.libros if libro.es_largo()]

    def titulos_disponibles(self):
        return [libro.titulo for libro in self.libros]
      
biblioteca = Biblioteca()