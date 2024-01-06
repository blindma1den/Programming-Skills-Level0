import os
import sys

alive = True

# I use USD as a base.
# TODO: Obtain these prices thru an Api.
# The system allow you to exchange a total of 2000 USD max.
# You cannot exchange less than 50 USD.
usd = 1
clp = 892.86
ars = 811.2
eur = 0.91
try_price = 29.82
gbp = 0.79
exchange_rates = [usd, clp, ars, eur, try_price, gbp]

def exchange_currency(initial_currency, final_currency, initial_amount):
    result = (initial_amount / exchange_rates[initial_currency - 1]) * exchange_rates[final_currency - 1]
    return result    

def verify_min_max(currency, amount):
    amount_in_usd = amount / exchange_rates[currency - 1]
    if amount_in_usd >= 50 and amount_in_usd <= 2000:
        return True
    return False

def abreviation(option):
    abreviation = ""
    if option == 1:
        abreviation = "USD"
    elif option == 2:
        abreviation = "CLP"
    elif option == 3:
        abreviation = "ARS"
    elif option == 4:
        abreviation = "EUR"
    elif option == 5:
        abreviation = "TRY"
    elif option == 6:
        abreviation = "GBP"
    return abreviation

def print_currencies():
    print("1. (USD) American Dollar")
    print("2. (CLP) Chilean Peso")
    print("3. (ARS) Argentine Peso")
    print("4. (EUR) Euro")
    print("5. (TRY) Turkish Lira")
    print("6. (GBP) Pound Sterling")

while alive:
    os.system('clear')
    print("WELCOME TO CURRENCY CONVERTER")
    print("=============================")
    print("Select your initial currency:")
    print_currencies()
    initial_option = int(input("Choose an option: "))
    initial_money = float(input("How much money do you want to exchange? "))
    #Verify min and max.
    if verify_min_max(initial_option, initial_money):
        print("\n")
        print("Select the currency you want to convert to:")
        print_currencies()
        exchange_option = int(input("Choose an option: "))
        final_amount = exchange_currency(initial_option, exchange_option, initial_money)
        print("\n")
        print("Now you have {} {}".format(final_amount, abreviation(exchange_option)))
        another_exchange = input("Would you like to perform another operation? (Y/N) ")
        if another_exchange == "N" or another_exchange == "n":
            print("\n")
            print("Thank you for using our Currency Converter. Goodbye")
            alive = False
            #sys.exit()
    else:
        print("Sorry you can exchange from 50 USD to 2000 USD max.")
        alive = False