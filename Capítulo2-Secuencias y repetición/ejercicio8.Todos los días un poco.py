def alguna_vez_supero_objetivo(duraciones): 
  supero = False # en principio, no se superó la marca de 3 minutos

  for duracion in duraciones:
    supero = supero or duracion < 3 # pero si alguna de ellas es menor a 3 minutos,
                                    # entonces sí la habrá superado

  return supero


def todos_los_dias_un_poco(duraciones): 
  supero = True
  
  for duracion in duraciones:
    supero = supero and duracion >= 30 
  
  return supero