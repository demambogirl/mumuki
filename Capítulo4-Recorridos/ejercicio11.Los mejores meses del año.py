def meses_afortunados(balances):
    meses_largos = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]
    return [balance["mes"] for balance in balances if balance["ganancia"] > 1000 and balance["mes"] in meses_largos]