ranking = ['Breaking bad', 'Black mirror', 'Better call saul', 'Dr. House', 'Los simpsons', 'El marginal', 'The walking dead', '24', 'Gotham', 'Epitafios']
def serie_no_recomendable(serie):
    return serie not in ranking or ranking.index(serie) >= len(ranking) -5

print(ranking)