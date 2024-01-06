'''
*       Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice.
* 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; 
*       otherwise, the system should close.
'''
from enum import Enum

class Currency(Enum):
    USD = 1.0
    CLP = 880.00
    ARS = 811.10
    EUR = 0.92
    TRY = 29.76
    GBP = 0.79

MIN_VAL=10.0
MAX_VAL=2000.0
def conversion(funds:float,initial_currency, exchange_currency)->float:
    if initial_currency == exchange_currency:
        print("You don't need to convert the money")
        return funds
    funds*=exchange_currency/initial_currency
    print(f"converted ammount: {funds}")
    return funds
    

def withdraw(funds:float,exchange_currency, commission:float = 0.01):
    withdrawn = funds-funds*commission
    funds == 0
    print(f"success! You've received {withdrawn}{exchange_currency}")

def main():
    control = 'Y'
    while control == 'Y':
        initial_currency = input("TYPE you initial currency: CLP, ARS, USD, EUR, TRY, GBP.\n").upper()
        exchange_currency = input("TYPE the exchange currency: CLP, ARS, USD, EUR, TRY, GBP.\n").upper()
        funds = float(input("How much do you want to exchange?"))

        if MAX_VAL >= funds >= MIN_VAL:
            conversion(funds, initial_currency=getattr(Currency,initial_currency).value, exchange_currency=getattr(Currency,exchange_currency).value)
            option=input ("do you want to withdraw? Y/N").upper() 
            if option not in ['Y', 'N']:
                print("Wrong input, try again.\n")
            if option == 'Y':
                withdraw(conversion(funds, initial_currency=getattr(Currency,initial_currency).value, exchange_currency=getattr(Currency,exchange_currency).value), exchange_currency)
        else:
            print(f"El número a convertir es demasiado alto o bajo. intrese un monto entre {MIN_VAL} y {MAX_VAL}")

        control=input("Do you want to perform another operation? Y/N").upper()
        if control not in ['Y', 'N']:
            print("Wrong input, try again.\n")
            continue
        if control == 'N':
            print("Thank you for using our services!")
            break

if __name__ == "__main__":
    main()


