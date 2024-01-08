#  2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
# * 		The user must choose their initial currency and the currency they want to exchange to.
# * 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
# * 		If the user decides to withdraw the funds, the system will charge a 1% commission.
# * 		Set a minimum and maximum amount for each currency, it can be of your choice.
# * 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.
import sys

class menu:

    def __init__(self) -> None:
        self.select()
  

    def select(self):
        while True:
            print("----------------------")
            print("1. view coins")
            print("2. change")
            print("3. exit")
            print("----------------------")
            opcion = int(input(f"Enter option: "))
            self.algo(opcion)
            
        
    
    def algo(self, opcion):
        if opcion == 1:
            values()
        elif opcion == 2:
            change()
        elif opcion == 3:
            sys.exit()
        else:
            print("Invalid option")

class values(menu):

    def __init__(self) -> None:
        self.coins()
        self.view_coins()


    def coins(self):

        self.clp = 888
        self.arg = 811
        self.eur = 0.91
        self.lira = 29
        self.gbp = 0.79
    
    def view_coins(self):
        print("----------------------")
        print("Values \n 1 dollar equals :")
        print(f" clp = {self.clp}\n arg = {self.arg} \n eur = {self.eur}\n try = {self.lira} \n gdp = {self.gbp}")
        print("----------------------")


class change(values):
    

    def __init__(self) -> None:
        super().__init__()
        initial_currency = input("choose a coin between clp, arg, eur, try, gdp: ")
        print(f"enter amount of $ {initial_currency}")

        if initial_currency == "clp":
            initial_currency = self.clp
        elif initial_currency == "arg":
            initial_currency = self.arg
        elif initial_currency == "eur":
            initial_currency = self.eur
        elif initial_currency == "try":
            initial_currency = self.lira
        elif initial_currency == "gbp":
            initial_currency = self.gbp
        else:
            print("Wrong coin")
            print("Closing program...")
            sys.exit()
        print (initial_currency)
        
        
        amount = float(input("ingresar cantidad a cambiar: "))
        total_dollars = amount / initial_currency

        final_coin = input("Enter the coin you want to convert to:")
        print(f"coin to convert: {final_coin}")
        if final_coin == "clp":
            final_coin = self.clp
        elif final_coin == "arg":
            final_coin = self.arg
        elif final_coin == "eur":
            final_coin = self.eur
        elif final_coin == "try":
            final_coin = self.lira
        elif final_coin == "gbp":
            final_coin = self.gbp
        else:
            print("Wrong coin")
            print("Closing program...")
            sys.exit()
        print (final_coin)

        total = (total_dollars * final_coin) 

        print(f"el total es de:{total} ")

        
menu()