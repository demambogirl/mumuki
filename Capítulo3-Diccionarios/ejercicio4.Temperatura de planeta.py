temperatura_de_planeta_template = "(planeta) tiene una temperatura promedio de [temperatura_promedio]"
planeta = {"nombre": "Tierra", "temperatura_promedio": 15}

def temperatura_de_planeta(planeta):
    if "nombre" in planeta and "temperatura_promedio" in planeta:
        nombre = planeta["nombre"]
        temperatura_promedio = planeta["temperatura_promedio"]
        return '{} tiene una temperatura promedio de {} grados'.format(nombre, temperatura_promedio)
    else:
        return "El diccionario de planeta no contiene la información necesaria."
    
resultado = temperatura_de_planeta(planeta)
print(resultado)