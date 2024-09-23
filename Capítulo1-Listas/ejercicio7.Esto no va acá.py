lista_origen = [1, 2, 3]
lista_destino = [4, 5]
elemento = 3

def trasladar(lista_origen, lista_destino, elemento):
    if elemento in lista_origen:
        lista_origen.remove(elemento)  # Elimina el elemento de la lista de origen
        lista_destino.append(elemento)  # Agrega el elemento a la lista de destino

print(elemento)

trasladar(lista_origen, lista_destino, elemento)