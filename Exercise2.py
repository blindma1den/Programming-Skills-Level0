#Exercise 2#
#!Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP!#
#|The user must choose their initial currency and the currency they want to exchange to.
#?The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
#?Tf the user decides to withdraw the funds, the system will charge a 1% commission.
#?Tet a minimum and maximum amount for each currency, it can be of your choice.
#?The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.

currency_values = { #*I dont know how to put changing values :(
    1:0.0011,
    2:0.0012,
    3:1,
    4:1.09,
    5:0.034,
    6:1.27
}

currency_index = {
    1:"CLP",
    2:"ARS",
    3:"USD",
    4:"EUR",
    5:"TRY",
    6:"GBP"
}

min_max_values = {
    1: [1000, 1000000],
	2: [10, 100000],
	3: [1, 10000],
	4: [1, 10000],
	5: [1, 10000],
	6: [1, 10000]
}

def choose_currency(message):
    print("1.CLP\n2.ARS\n3.USD\n4.EUR\n5.TRY\n6.GBP")
    currency = input(message)
    if(currency.isnumeric() and (0 < int(currency) < 7)):
        return int(currency)
    else:
        print("The input is not valid. Try again.")
        return choose_currency(message)

def valdiate_value(amount, currency):
    min, max = min_max_values[currency]
    if(min <= amount <= max):
        pass
    else:
        print(f"The amount is not valid for {currency_index[currency]}. Try again.")
        set_balance(currency)

def set_balance(currency):
    balance = input(f"Enter the amount you'd like to convert: {currency_index[currency]}$")
    if(balance.isnumeric() and int(balance) > 0):
        valdiate_value(int(balance), currency)
        return int(balance)
    else:
        print(f"The amount is not valid. Try again.")
        return set_balance(currency)

def converter(FC, SC, amount):
    amount_converted = amount * currency_values[FC] / currency_values[SC]
    amount_converted = round(amount_converted, 2)
    print(f"You have ${amount} {currency_index[FC]}")
    print(f"This amount in {currency_index[SC]} is: ${amount_converted}")
    return amount_converted

def main(state):
    print("Welcome to the currency converter")
    first_currency = choose_currency("Choose your actual currency: ")
    second_currency = choose_currency("Choose the currency you want to convert to: ")
    actual_balance = set_balance(first_currency)
    converter(first_currency, second_currency, actual_balance)

    cycle = input("Would you like to do another conversion? (Y/N): ").lower()
    if(cycle == "y"):
        pass
    else:
        state = False
    return state

active = True
while(active == True):
    active = main(active)
else:
    print("Thanks for using the currency converter")