def afortunados(balances):
    balances_afortunados = []
    for balance in balances:
        if balance["ganancia"] > 1000:  # Verifica si la ganancia es mayor a $1000
            balances_afortunados.append(balance)  # Agrega el balance a la lista de balances afortunados
    return balances_afortunados