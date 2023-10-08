def donde_estan_las_llaves(cadena_numeros):
    posicion = 0  # Inicializamos la variable para almacenar la posición
    for numero in cadena_numeros:
        posicion += 1  # Incrementamos la posición en cada iteración
        if numero == '🔑':
            return posicion
   