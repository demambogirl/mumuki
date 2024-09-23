flan_casero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }

def mas_dificil_de_cocinar(postre1, postre2):
  
   if len (postre1["ingredientes"]) > len(postre2["ingredientes"]):
    return postre1
   else: 
     return postre2

resultado = mas_dificil_de_cocinar(flan_casero, cheesecake)
print(resultado)