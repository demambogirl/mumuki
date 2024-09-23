def balances_positivos(balances):
    balances_positivos = []
    for balance in balances:
        if balance["ganancia"] > 0:  # Verifica si la ganancia es mayor que cero
            balances_positivos.append(balance)  # Agrega el balance a la lista de balances positivos
    return balances_positivos