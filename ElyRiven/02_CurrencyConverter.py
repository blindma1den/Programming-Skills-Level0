# 2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
# * 	The user must choose their initial currency and the currency they want to exchange to.
# * 	The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
# * 	If the user decides to withdraw the funds, the system will charge a 1% commission.
# * 	Set a minimum and maximum amount for each currency, it can be of your choice.
# * 	The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.

DefaultUser = {
    'username': 'ElyRiven',
    'funds': 10000.00
}

CURRENCY_CONVERSION = {
    'clp': {
        'ars': 0.91467,
        'usd': 0.0011,
        'eur': 0.0010,
        'try': 0.034,
        'gbp': 0.00090,
    },
    'ars': {
        'clp': 1.09,
        'usd': 0.00123,
        'eur': 0.0011,
        'try': 0.037,
        'gbp': 0.00098,
    },
    'usd': {
        'clp': 884.33,
        'ars': 810.66,
        'eur': 0.91,
        'try': 29.74,
        'gbp': 0.79,
    },
    'eur': {
        'clp': 967.61,
        'ars': 887.00,
        'usd': 1.09,
        'try': 32.53,
        'gbp': 0.87,
    },
    'try': {
        'clp': 29.74,
        'ars': 27.27,
        'usd': 0.034,
        'eur': 0.031,
        'gbp': 0.027,
    },
    'gbp': {
        'clp': 1116.02,
        'ars': 1023.06,
        'usd': 1.26,
        'eur': 1.15,
        'try': 37.52,
    },
}

def main():
    end = 1
    # currentFund = DefaultUser.get('funds')
    while end != 0:
        print(f'\t\t\tCurrency Converter\n\n{DefaultUser.get("username")}s Account\nCurrent Fund: {"{:.2f}".format(DefaultUser.get("funds"))}\n\nInitial Currency\n')
        initCurrency = selectCurrency()
        if initCurrency != None:
            print('\nTarget Currency\n')
            targetCurrency = selectCurrency()
            try:
                amount = float(input('Enter the amount you want to convert: '))
                result = calculateConversion(CURRENCY_CONVERSION.get(initCurrency).get(targetCurrency), amount)
                print(f"{'{:.2f}'.format(amount)} {initCurrency.upper()} is equivalent to {result} {targetCurrency.upper()}")
                try:
                    checkWithdraw = input('\nWould you like to withdraw the converted currency? [Y/N] ').lower()
                    if checkWithdraw == 'y':
                        checkFund = float('{:.2f}'.format(DefaultUser.get('funds') - amount))
                        if checkFund < 0:
                            print('You do not have enough funds in your account. Operation Canceled\n')
                        else:
                            fundUpdate = float('{:.2f}'.format(DefaultUser.get('funds') - amount))
                            DefaultUser['funds'] = fundUpdate
                            print('Operation completed succesfully')
                except:
                    print('Invalid input')
            except:
                print('Invalid amount input. Enter a valid amount')
        
        try:
            checkUser = input('\nWould you like to make another operation? [Y/N] ').lower()
            if checkUser == 'n':
                end = 0
            else:
                continue
        except:
            print('Invalid input')

def selectCurrency():
    try:
        initialCurrency = input('Select the desired Currency: CLP - ARS - USD - EUR - TRY - GBP\n').lower()
        if initialCurrency == 'clp':
            return initialCurrency
        if initialCurrency == 'ars':
            return initialCurrency
        if initialCurrency == 'usd':
            return initialCurrency
        if initialCurrency == 'eur':
            return initialCurrency
        if initialCurrency == 'try':
            return initialCurrency
        if initialCurrency == 'gbp':
            return initialCurrency
        print('Input doesnt match any supported currency. Please try again\n')
    except:
        print('\nInvalid input. Select a valid currency')

def calculateConversion(tarCurrency, amount):
    return amount * tarCurrency

if __name__ == '__main__':
    main()