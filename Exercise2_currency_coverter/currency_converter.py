# Currency converter using USD as base
USD = {
    'CLP': 0.11,
    'ARS': 0.12,
    'EUR': 0.91,
    'TRY': 0.33,
    'GBP': 0.78,
    'USD': 1,
}
# Create variables with min amount $10.00 and max amount $10.000
min_amount = 10
max_amount = 10000


# Create a menu
def menu():
    while True:
        message = """*** WELCOME TO CURRENCY CONVERTER ***"
        "1.-CLP - 2.-ARS - 3.-EUR - 4.-TRY - 5.-GBP - 6.-USD"""
        print(message)
        # Convert the world to upper if the user enter lowercase
        initial_currency = input("Enter Initial currency ").upper()
        currency_exchange = input("Enter the exchange rate you want ").upper()
        amount_to_exchange = float(input("Enter amount to exchange "))
        exchange_result = exchange(initial_currency, currency_exchange, amount_to_exchange)
        if not exchange_result:
            break


# Ask for initial currency and currency you want to exchange and amount
def exchange(initial_currency, currency_exchange, amount_to_exchange):
    if initial_currency and currency_exchange in USD and min_amount <= amount_to_exchange <= max_amount:
        # Exchange currency with dictionary data
        exchange_rate = USD[currency_exchange] / USD[initial_currency]
        total = round(amount_to_exchange * exchange_rate, 2)
        # Withdraw the funds
        print(f"Your funds are {total} ")
        withdraw = input("Do you want to withdraw your funds?  commission 1% Y/N ").upper()
        if withdraw == 'Y':
            # System will charge a 1% commission.
            commission = round(total * 0.01, 2)
            withdraw_funds = round(total - commission, 2)
            print(withdraw_funds)
            another_transaction = input("Do you want to make another transaction? (Y/N): ").upper()
            if another_transaction == 'Y':
                return True
            else:
                return False
    else:
        print("Error entering data")


menu()

