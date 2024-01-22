# Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:

#base dolar
list_exchange = {
"CLP": 913.40,
"ARS": 817.68,
"USD": 1,
"EUR": 0.92,
"TRY": 30.11,
"GBP": 0.79
}

amount = 0
comission = 0
amount_min = 100
amount_max = 1000

# The user must choose their initial currency and the currency they want to exchange to.
# The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.


def main_menu():    
    print("Welcome!")
    print("Type your initial currency: ")
    print("CLP") 
    print("ARS")     
    print("USD")     
    print("EUR")
    print("TRY") 
    print("GBP")

    option_currency1 = input()

    print("Enter the amount")
    amount = int(input())
    # Set a minimum and maximum amount for each currency, it can be of your choice.
    if amount > amount_min and amount < amount_max:
        print("Type the currency you want to exchange to: ")
        print("CLP") 
        print("ARS")     
        print("USD")     
        print("EUR")
        print("TRY") 
        print("GBP")

        option_currency2 = input() 
    else:
        print("The amount should be between the limits: 100 and 1000")
        main_menu()
    
    result_exchange = ((amount * list_exchange.get("USD")) / list_exchange.get(option_currency1)) * list_exchange.get(option_currency2)
    
    print ("The exchange is", result_exchange)
    
    # If the user decides to withdraw the funds, the system will charge a 1% commission.
    print("Do you want to withdraw your funds?")
    print("Yes") 
    print("No")
    
    option_withdraw = input()
    
    if option_withdraw == "Yes":
        comission = result_exchange * 0.01
        print("Your comission is", comission)
        
    elif option_withdraw == "No":
        print("Thank you. Do you want to do another exchange?")
        print("Yes") 
        print("No")
        option = input()

        # The system should ask the user if they want to perform another operation.If they choose to do so, it should restart the process; 
        # otherwise, the system should close.
        if option == "Yes":
                main_menu()
        else:
            print("Thank you for your operation.")
            
main_menu()

