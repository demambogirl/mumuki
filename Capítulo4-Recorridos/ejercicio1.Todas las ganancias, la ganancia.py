balances_ultimo_semestre = [
    { "mes": "julio", "ganancia": 50 }, 
    { "mes": "agosto", "ganancia": -12 }, 
    { "mes": "septiembre", "ganancia": 1000 }, 
    { "mes": "octubre", "ganancia": 300 }, 
    { "mes":  "noviembre", "ganancia": 200 }, 
    { "mes": "diciembre", "ganancia": 0 }
]

def ganancia_total(balances_ultimo_semestre):
    total = 0
    for mes in balances_ultimo_semestre:
        total += mes["ganancia"]
    return total