"""2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw,
 it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice. X
* 		The system should ask the user if they want to perform another operation. If they choose to do so,
 it should restart the process; otherwise, the system should close."""


print("Currency Converter")
print()

exchange_rates = {
    'CLP': 0.0030,
    'ARS': 0.020,
    'USD': 1.0,
    'EUR': 1.15,
    'TRY': 0.15,
    'GBP': 1.35,
}
commission_rate = 0.01

min_amount = {
    'CLP': 5,
    'ARS': 5,
    'USD': 5,
    'EUR': 5,
    'TRY': 5,
    'GBP': 5,
}
max_amount = {
    'CLP': 20000,
    'ARS': 20000,
    'USD': 20000,
    'EUR': 20000,
    'TRY': 20000,
    'GBP': 20000,
}

while True:

    from_currency = input("Insert you currency initial (for example, ARG): ")
    to_currency = input("Insert the coin to change (for example, GBP): ")

    amount = float(input(f"Enter the amount in {from_currency}: "))

    if amount < min_amount[from_currency] or amount > max_amount[from_currency]:
        print(f"Enter the amount in {min_amount[from_currency]} y {max_amount[from_currency]} {from_currency}.")
        continue

    withdraw_funds = input("¿withdraw their funds? (yes/no): ") == 'yes'

    if withdraw_funds:
        converted_amount = amount * exchange_rates[to_currency] * (1 - commission_rate)
        print(f"Amount converted after a 1% commission: {converted_amount:.3f} {to_currency}")
    else:
        converted_amount = amount * exchange_rates[to_currency]
        print(f"Amount converted: {converted_amount:.3f} {to_currency}")

    another_operation = input("¿Do you want to perform another operation? (yes/no): ")
    if another_operation != 'yes':
        print("See so bro!!!")
        break