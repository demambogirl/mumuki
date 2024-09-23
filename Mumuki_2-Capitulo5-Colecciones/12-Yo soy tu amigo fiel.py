class Juguete:
    def __init__(self, nombre, precio_minorista, precio_mayorista, partes):
        self.nombre = nombre
        self.precio_minorista = precio_minorista
        self.precio_mayorista = precio_mayorista
        self.partes = partes

    def es_barato(self):
        return self.precio_minorista < 1000 and self.precio_mayorista < 600

    def precios_con_iva(self):
        precio_minorista_con_iva = self.precio_minorista * 1.21
        precio_mayorista_con_iva = self.precio_mayorista * 1.21
        return (precio_minorista_con_iva, precio_mayorista_con_iva)

    def es_electronico(self):
        return "batería" in self.partes

autito = Juguete("Relámpago Marquinhos", 400, 300, set(["ruedas", "carcaza", "batería"]))
pinocho = Juguete("Pinocho", 500, 420, set(["cuerpo", "ropa", "cuerda"]))
