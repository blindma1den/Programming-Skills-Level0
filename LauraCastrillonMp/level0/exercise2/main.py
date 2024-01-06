import csv

# Load exchange rates and limits from a CSV file
def load_data():
    with open('exchange_data.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data

# Save updated exchange rates and limits to the CSV file
def save_data(data):
    with open('exchange_data.csv', 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(data)

# Convert currency
def convert_currency(amount, from_currency, to_currency):
    data = load_data()

    # Find exchange rates and limits for the specified currencies
    for row in data:
        if row[0] == from_currency and row[1] == to_currency:
            rate = float(row[2])
            min_limit = float(row[3])
            max_limit = float(row[4])
            break
    else:
        print("Invalid currency pair.")
        return

    # Check if the amount is within the limits
    if amount < min_limit or amount > max_limit:
        print("Amount exceeds limits.")
        return

    # Calculate converted amount
    converted_amount = amount * rate

    # Ask the user if they want to withdraw funds
    withdraw = input(f"Converted amount: {converted_amount:.2f} {to_currency}. Do you want to withdraw funds? (y/n): ").lower()

    if withdraw == 'y':
        # Apply 1% commission
        commission = converted_amount * 0.01
        withdrawn_amount = converted_amount - commission
        print(f"Withdrawn amount: {withdrawn_amount:.2f} {to_currency} (1% commission applied).")
    else:
        print("Funds not withdrawn.")

# Main function
def main():
    while True:
        print("\nCurrency Converter\n")
        print("1. CLP")
        print("2. ARS")
        print("3. USD")
        print("4. EUR")
        print("5. TRY")
        print("6. GBP")
        print("0. Exit")

        from_currency = input("Enter the number of the initial currency (0 to exit): ")
        if from_currency == '0':
            break

        to_currency = input("Enter the number of the currency you want to exchange to: ")
        amount = float(input("Enter the amount: "))

        convert_currency(amount, from_currency, to_currency)

# Run the program
if __name__ == "__main__":
    main()
