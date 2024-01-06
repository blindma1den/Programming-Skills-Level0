# Exchanger rate January 5th, 2024
currency = {
    "USD": 1,
    "CLP": 889.95,
    "ARS": 811.20,
    "EUR": 0.91,
    "TRY": 29.82,
    "GBP": 0.79
}


def currency_exchanger(initial, exchanged, currency_amount):
    if initial == exchanged:
        return "No exchange made, initial currency is the same as final currency"

    exchanged_currency = currency_amount / currency[initial]
    final_amount = exchanged_currency * currency[exchanged]
    return f"{final_amount:.2f}"


print("Welcome to the Currency Exchange System")

while True:
    print("Available currency")
    print("CLP, USD, ARS, EUR, TRY, GBP")
    initial_currency = input("Select your initial currency: ").upper().strip()
    currency_to_exchange = input("Select the currency that you want to exchange to: ").upper().strip()
    amount = float(input("Enter the amount to exchange: "))

    if initial_currency not in currency or currency_to_exchange not in currency or amount < 0:
        print("Invalid data. Closing program.")
        break

    exchanged_currency_amount = float(currency_exchanger(initial_currency, currency_to_exchange, amount))
    print(f"You exchanged ${amount} {initial_currency} to ${exchanged_currency_amount} {currency_to_exchange}.")

    if amount <= 10:
        print("Can't perform the operation. You are trying to exchange too little money")
        break
    elif amount >= 1000:
        print("Can't perform the operation. You are trying to exchange too much money")
        break

    choice = input("Do you want to withdraw this amount? There will be a charge of 1% on the amount exchanged. "
                   "Y/N: ").lower().strip()

    if choice == "y":
        commission = float(exchanged_currency_amount) * 0.01
        withdrawn_amount = exchanged_currency_amount - commission
        print(f"You have withdrawn the amount of {withdrawn_amount:.2f}. "
              f"A commission of {commission:.2f} was charged to the amount that you withdrawn")
    elif choice == "n":
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Please try again.")

    final_choice = input("Do you want to preform another operation? Y/N: ").lower().strip()
    if final_choice == "n":
        break
