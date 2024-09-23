def meses(balances_ultimo_semestre):
    lista_meses = []  
    
    for balance in balances_ultimo_semestre:
        lista_meses.append(balance["mes"]) 
        
    return lista_meses