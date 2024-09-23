def afortunados(balances):
    return list(filter(lambda balance: balance["ganancia"] > 1000, balances))
