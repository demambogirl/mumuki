from ejercicio6d import anio

def es_del_milenio_pasado(archivo):
    anio_creacion = anio(archivo["creacion"])

    return anio_creacion < 2000