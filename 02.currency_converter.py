import os
import sys

# I use USD as a base.
# TODO: Obtain these prices thru an api.
# The system allow you to exchange a total of 2000 USD max.
# You cannot exchange less than 50 USD.
usd_price = 1
clp_price = 892.86
ars_price = 811.2
eur_price = 0.91
try_price = 29.82
gbp_price = 0.79

def verify_min_max(currency, amount):
    amount_in_usd = 0
    if currency == "USD":
        amount_in_usd = amount / usd_price
    elif currency == "CLP":
        amount_in_usd = amount / clp_price
    elif currency == "ARS":
        amount_in_usd = amount / ars_price
    elif currency == "EUR":
        amount_in_usd = amount / eur_price
    elif currency == "TRY":
        amount_in_usd = amount / try_price
    elif currency == "GBP":
        amount_in_usd = amount / gbp_price

    if amount_in_usd >= 50 and amount_in_usd <= 2000:
        return True
    return False

def print_currencies():
    print("1. (USD) American Dollar")
    print("2. (CLP) Chilean Peso")
    print("3. (ARS) Argentine Peso")
    print("4. (EUR) Euro")
    print("5. (TRY) Turkish Lira")
    print("6. (GBP) Pound Sterling")

os.system('clear')
print("WELCOME TO CURRENCY CONVERTER")
print("=============================")
print("Select your initial currency:")
print_currencies()
initial_option = int(input("Choose an option: "))
initial_money = float(input("How much money do you want to exchange? "))
#Verify min and max.
if initial_option == 1 and verify_min_max("USD", initial_money):
    print("Select the currency you want to convert to:")
    print_currencies()
    exchange_option = int(input("Choose an option: "))