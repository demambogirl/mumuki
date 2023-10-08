def cuantas_veces_supero_objetivo(duraciones): 
  veces = 0

  for duracion in duraciones:
    if duracion < 3:
      veces += 1

  return veces

def cuantas_veces_entreno_lo_suficiente(duraciones): 
  veces = 0

  for duracion in duraciones:
    if duracion > 30:
      veces += 1

  return veces