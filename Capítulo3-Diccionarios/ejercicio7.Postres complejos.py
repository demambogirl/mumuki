def mas_dificil_de_cocinar(postre1, postre2):
  
   if len (postre1["ingredientes"]) > len(postre2["ingredientes"]):
    return postre1
   else: 
     return postre2
