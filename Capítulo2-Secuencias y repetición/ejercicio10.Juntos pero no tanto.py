def juntar(separador, lista_de_cadenas):
    resultado = ""
    
    for elemento in range(len(lista_de_cadenas)):
        resultado += lista_de_cadenas[elemento]
        
        if elemento < len(lista_de_cadenas) - 1:
            resultado += separador
    
    return resultado