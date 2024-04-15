#2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
#The user must choose their initial currency and the currency they want to exchange to.
#The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
#If the user decides to withdraw the funds, the system will charge a 1% commission.
#The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.
#Set a minimum and maximum amount for each currency, it can be of your choice.


def apply_commision(amount):
    return amount * 0.99
def main():
    while True:
        print("\nWelcome to the currency converter, Please choice between these currency")
        print("1. CLP")
        print("2. ARS")
        print("3. USD")
        print("4. EUR")
        print("5. TRY")
        print("6. GBP")
        
        while True:
            initial_currency = int(input("Select initial currency: "))
            exchange_currency = int(input("Select currency you want to exchange to: "))
            if initial_currency == exchange_currency:
                print('initial and exchange currency has not to be the same, please make again')
            else:
                break
            
        amount = float(input("What is the amount you want to exchange: "))
        
        if amount > 10000 or amount< 200:
            print('the amount is out of the limit to make the operation')
            continue
        
        print("\nWhat do you want to do next?")
        print("1. Withdraw")
        print("2. Go to main menu")
        
        choice = int(input("Enter your choice: "))
        
        #feature for withdraw
        if choice == 1 :
            amount = apply_commision(amount)
            print(f'the new amount is: {amount}')
            
            yes_or_not = input("Do you want to make another operation? (Y/n): ")
            
            if yes_or_not == 'n':
                break
            
        
        
if __name__ == "__main__":
    main()