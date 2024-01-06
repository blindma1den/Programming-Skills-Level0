monedas = {
    1: 'CLP', # PESO CHILENO
    2: 'ARS', # PESO ARGENTINO
    3: 'USD', # DOLAR
    4: 'EUR', # EURO
    5: 'TRY', # LIRA TURCA
    6: 'GBP'  # LIBRA ESTERLINA
}

clp = {
    'ARS' : 0.000039,
    'USD' : 0.000027,
    'EUR' : 0.000022,
    'TRY' : 0.000007,
    'GBP' : 0.000025,
}

ars = {
    'CLP' : 258.41,
    'USD' : 0.68,
    'EUR' : 0.57,
    'TRY' : 0.18,
    'GBP' : 0.62,
}
usd = {
    'CLP' : 36,
    'ARG' : 1.47,
    'EUR' : 0.84,
    'TRY' : 0.22,
    'GBP' : 1,
}
eur = {
    'CLP' : 39.71,
    'ARG' : 1.61,
    'USD' : 1.18,
    'TRY' : 0.25,
    'GBP' : 1.12,
}
tr = {
    'CLP' : 16.38,
    'ARG' : 0.63,
    'USD' : 0.50,
    'EUR' : 0.41,
    'GBP' : 0.54,}
gbp = {
    'CLP' : 42.68,
    'ARG' : 1.71,
    'USD' : 1.27,
    'EUR' : 1.06,
    'TRY' : 0.28,
}

cambio = {
    'CLP': clp, # PESO CHILENO
    'ARS': ars, # PESO ARGENTINO
    'USD': usd, # DOLAR
    'EUR': eur, # EURO
    'TRY': tr, # LIRA TURCA
    'GBP': gbp  # LIBRA ESTERLINA
}
operaciones = {
    1: 'CAMBIAR',
    2: 'RETIRAR',
    0: 'SALIR',
}