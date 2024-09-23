class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


autor_carl_sagan = Autoria("Carl", "Sagan", "EEUU")
autor_elsa_bornemann = Autoria("Elsa", "Bornemann", "AR")

contacto = Libro("Contacto", "Ciencia Ficción", 400, autor_carl_sagan)
socorro = Libro("Socorro", "Terror", 250, autor_elsa_bornemann)

biblioteca_de_emma = Biblioteca()
biblioteca_de_emma.agregar_libro(contacto)
biblioteca_de_emma.agregar_libro(socorro)


# Imprimir información de la biblioteca
print("Biblioteca de Emma:")
for libro in biblioteca_de_emma.libros:
    print(f"Título: {libro.titulo}")
    print(f"Género: {libro.genero}")
    print(f"Páginas: {libro.paginas}")
    print(f"Autor: {libro.autoria.nombre} {libro.autoria.apellido} {libro.autoria.nacionalidad}")
    print()# Press Ctrl+F8 to toggle the breakpoint.