def trasladar(lista_origen, lista_destino, elemento):
    if elemento in lista_origen:
        lista_origen.remove(elemento)  # Elimina el elemento de la lista de origen
        lista_destino.append(elemento)  # Agrega el elemento a la lista de destino