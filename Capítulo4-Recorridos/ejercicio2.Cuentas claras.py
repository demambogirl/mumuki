def cantidad_de_balances_positivos(balances_ultimo_semestre):
    count = 0 
    
    for mes in balances_ultimo_semestre:
        if mes["ganancia"] > 0: 
            count += 1  
            
    return count