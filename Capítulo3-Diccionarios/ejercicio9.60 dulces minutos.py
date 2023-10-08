def agregar_a_postres_rapidos(lista_postres_rapidos, postre):
    tiempo_de_coccion = postre.get("tiempo_de_coccion", 0)  # Obtener el tiempo de cocción del postre (por defecto 0 minutos si no se especifica)

    if tiempo_de_coccion <= 60:  # Verificar si el tiempo de cocción es de una hora o menos (60 minutos)
        lista_postres_rapidos.append(postre)