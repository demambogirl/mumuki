biblioteca_de_emma = Biblioteca()

autor_carl_sagan = {"nombre": "Carl", "apellido": "Sagan", "nacionalidad": "Estados Unidos"}
autor_elsa_bornemann = {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina"}

contacto = Libro("Contacto", 400, "Ciencia ficción", autor_carl_sagan)
socorro = Libro("Socorro", 250, "Terror", autor_elsa_bornemann)

biblioteca_de_emma.agregar_libro(contacto)
biblioteca_de_emma.agregar_libro(socorro)