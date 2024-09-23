def anio(fecha):
    return int(fecha[:4])

archivo = {"creacion": "1999-01-01"}

def es_del_milenio_pasado(archivo):
    anio_creacion = anio(archivo["creacion"])
    return anio_creacion < 2000

resultado = es_del_milenio_pasado(archivo)
print(resultado)