def balances_de_meses_largos(balances):
    meses_largos = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]
    return [balance for balance in balances if balance["mes"] in meses_largos]
