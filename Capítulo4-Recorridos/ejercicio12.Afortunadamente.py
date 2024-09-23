def meses_afortunados(balances):
    meses_largos = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]
    
    # Filtrar balances afortunados y obtener sus meses
    balances_afortunados = filter(lambda balance: balance["ganancia"] > 1000, balances)
    meses = map(lambda balance: balance["mes"], balances_afortunados)
    
    return list(meses)
