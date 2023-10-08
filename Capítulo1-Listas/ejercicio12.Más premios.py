def medalla_segun_puesto(puesto):
    medallero = ["oro", "plata", "bronce"]
    if puesto <= 3 and puesto >= 1:
       return medallero[puesto - 1]
    else:
        return "nada"