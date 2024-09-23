class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    if isinstance(libro, Libro):
      self.libros.append(libro)
    else:
      return ValueError("El objeto debe ser una instancia de la clase Libro")
    
biblioteca_de_mar = Biblioteca()

class Libro:
  def __init__(self, titulo, paginas, genero):
    self.titulo = titulo
    self.paginas = paginas
    self.genero = genero
   
    
  def es_largo(self):
    return self.paginas > 300