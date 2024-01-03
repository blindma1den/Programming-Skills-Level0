'''
2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice.
* 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.



'''
CLP = 0.0014
ARS = 0.010
USD =  1
EUR = 1.21
TRY = 0.12
GBP = 1.39

currencies = {'CLP': CLP, 'ARS': ARS, 'USD': USD, 'EUR': EUR, 'TRY': TRY, 'GBP': GBP}

def currency():

    continue_ = True

    while continue_:

        print('These are the available currencies, choose one: CLP, ARS, USD, EUS, TRY, GBP')
        print("\nMenu:")
        print("1. CLP")
        print("2. ARS")
        print("3. USD")
        print("4. EUR")
        print("5. TRY")
        print("6. GBP")


        i_currency= input("Enter initial currency (choose a number from the given list): ")
        

        if 1 <= int(i_currency) and int(i_currency) <= 6:   #checks
            i_currency = list(currencies.keys())[int(i_currency) -1]

        else:
            print('Invalid. Choose a number from the given list')
            i_currency= input("Enter initial currency (choose a number): ")
            if 1 <= int(i_currency) <= 6:   #checks
                i_currency = list(currencies.keys())[int(i_currency) -1]
            else:
                continue

        f_currency = input('Enter the currency you want to exchange to (choose a number from the givrn list): ')

        if 1 <= int(f_currency) <= 6:   #checks
            f_currency = list(currencies.keys())[int(f_currency) -1]
    
        else:
            print('Invalid. Choose a number from the given list')
            f_currency= input("Enter initial currency (choose a number): ")
            if 1 <= int(f_currency) <= 6:   #checks
                f_currency = list(currencies.keys())[int(f_currency) -1]
            else:
                continue

        money= float(input('Enter the quantity of money to convert: '))

        if not 1 <= money <= 7000:
            print('Invalid amount. Please enter a number between 1 and 7000')
            continue

        withdraw = input('Do you want to withdraw funds? (y/n): ').lower()
        
        if withdraw == 'y':
            commision = 1.01
            converted_money = money* currencies[i_currency]* commision
            print('Converted money applying 1% comision: ', converted_money)
        else:
            converted_money = money* currencies[i_currency]
            print('Converted money: ', converted_money)

        other= input('Want to do another operation (y/n)? ')
        continue_ = (other == 'y')

        if other == 'n':
            print('Thank you for converting yourr money. Have a nice day!')
            

if __name__ == "__main__":
	currency()
    
    

    

