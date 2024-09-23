class Jugueteria:
    def __init__(self):
        self.productos = []

    def adquirir_producto(self, producto):
        self.productos.append(producto)

    def catalogo_de_oferta(self):
        return [producto.nombre for producto in self.productos if producto.es_barato()]

autito = Juguete("Relámpago Marquinhos", 400, 300, set(["ruedas", "carcaza", "batería"]))
pinocho = Juguete("Pinocho", 500, 420, set(["cuerpo", "ropa", "cuerda"]))

jugueteria = Jugueteria()
jugueteria.adquirir_producto(autito)
jugueteria.adquirir_producto(pinocho)