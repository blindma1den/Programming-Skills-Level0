currencies = {
    'CLP': 889.60,
    'ARS': 812.20,
    'EUR': 0.91,
    'USD': 1.00,
    'TRY': 29.82,
    'GBP': 0.78
}

currency_symbols = {
    'CLP': '$',
    'ARS': '$',
    'EUR': '€',
    'USD': '$',
    'TRY': '₺',
    'GBP': '£'
}



def show_currencies():
    print('\nAVAILABLE CURRENCIES:')
    for currency, value in currencies.items():
        print(f'{currency} - {value}')


def exchange():
    initial_currency = input('\nType your currency: ')
    initial_currency = initial_currency.upper().strip()
    while not initial_currency:
        print('You did not type your currency.')
        initial_currency = input('\nType your currency: ')

    currency_to_convert = input('\nType the currency to convert: ')
    currency_to_convert = currency_to_convert.upper().strip()
    while not currency_to_convert:
        print('You did not type the currency you want to convert.')
        currency_to_convert = input('\nType the currency to convert: ')

    amount = float(input(f'\nHow much money do you want to exchange?\n=> {currency_symbols[initial_currency]}'))

    convert_to_usd = amount / currencies[initial_currency]
    final_conversion = convert_to_usd * currencies[currency_to_convert]
    min_allowed_usd = 10
    max_allowed_usd = 2000
    min_limit_exchange = currencies[initial_currency] * min_allowed_usd
    max_limit_exchange = currencies[initial_currency] * max_allowed_usd

    while True:
      if convert_to_usd < min_allowed_usd:
            print(f'The minimum you can exchange is {currency_symbols[initial_currency]}{min_limit_exchange}')
            amount = float(input(f'\nHow much money do you want to exchange?\n=> {currency_symbols[initial_currency]}'))
            convert_to_usd = amount / currencies[initial_currency]
      elif convert_to_usd > max_allowed_usd:
            print(f'The maximum you can exchange is {max_limit_exchange}')
            amount = float(input(f'\nHow much money do you want to exchange?\n=> {currency_symbols[initial_currency]}'))
            convert_to_usd = amount / currencies[initial_currency]
      else:
            break

    # ? comission =

    match currency_to_convert:
        case 'CLP':
            print(f'You want to exchange from {initial_currency.upper().strip()} to {currency_to_convert.upper().strip()}')
            print(f'Initial value: {currency_symbols[initial_currency]}{amount} - Final conversion: {currency_symbols[currency_to_convert]}{round(final_conversion, 2)}')
            print(f'')
        case 'ARS':
            print(f'You want to exchange from {initial_currency.upper().strip()} to {currency_to_convert.upper().strip()}')
            convert_to_usd = amount / currencies[initial_currency]
            final_conversion = convert_to_usd * currencies['ARS']
            print(f'Initial value: {currency_symbols[initial_currency]}{amount} - Final conversion: {currency_symbols[currency_to_convert]}{round(final_conversion, 2)}')
        case 'EUR':
            print(f'You want to exchange from {initial_currency.upper().strip()} to {currency_to_convert.upper().strip()}')
            convert_to_usd = amount / currencies[initial_currency]
            final_conversion = convert_to_usd * currencies['EUR']
            print(f'Initial value: {currency_symbols[initial_currency]}{amount} - Final conversion: {currency_symbols[currency_to_convert]}{round(final_conversion, 2)}')
        case 'USD':
            print(f'You want to exchange from {initial_currency.upper().strip()} to {currency_to_convert.upper().strip()}')
            convert_to_usd = amount / currencies[initial_currency]
            final_conversion = convert_to_usd * currencies['USD']
            print(f'Initial value: {currency_symbols[initial_currency]}{amount} - Final conversion: {currency_symbols[currency_to_convert]}{round(final_conversion, 2)}')
        case 'TRY':
            print(f'You want to exchange from {initial_currency.upper().strip()} to {currency_to_convert.upper().strip()}')
            convert_to_usd = amount / currencies[initial_currency]
            final_conversion = convert_to_usd * currencies['TRY']
            print(f'Initial value: {currency_symbols[initial_currency]}{amount} - Final conversion: {currency_symbols[currency_to_convert]}{round(final_conversion, 2)}')
        case 'GBP':
            print(f'You want to exchange from {initial_currency.upper().strip()} to {currency_to_convert.upper().strip()}')
            convert_to_usd = amount / currencies[initial_currency]
            final_conversion = convert_to_usd * currencies['GBP']
            print(f'Initial value: {currency_symbols[initial_currency]}{amount} - Final conversion: {currency_symbols[currency_to_convert]}{round(final_conversion, 2)}')
        case _:
            print('THAT CURRENCY DOES NOT EXIST - TYPE ONE THAT IS ON THE LIST\n')
            exchange()

    return True


def run_app():
    print(' * * * WELCOME TO X-CHANGE * * *')
    show_currencies()
    exchange()


run_app()
