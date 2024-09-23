def ganancias(balances_ultimo_semestre):
    lista_ganancias = []  
    
    for mes in balances_ultimo_semestre:
        lista_ganancias.append(mes["ganancia"])  
        
    return lista_ganancias 
