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
            print("1. ver monedas")
            print("2. cambiar")
            print("3. exti")
            print("----------------------")
            opcion = int(input(f"Enter option: "))
            self.algo(opcion)
            
        
    
    def algo(self, opcion):
        if opcion == 1:
            valores()
        elif opcion == 2:
            cambio()
        elif opcion == 3:
            sys.exit()
        else:
            print("Invalid option")

class valores(menu):

    def __init__(self) -> None:
        self.monedas()
        self.ver_monedas()


    def monedas(self):

        self.clp = 888
        self.arg = 811
        self.eur = 0.91
        self.lira = 29
        self.gbp = 0.79
    
    def ver_monedas(self):
        print("----------------------")
        print("Valores \n 1 dolar equivale a:")
        print(f" chile = {self.clp}\n arg = {self.arg} \n eur = {self.eur}\n try = {self.lira} \n gdp = {self.gbp}")
        print("----------------------")


class cambio(valores):
    

    def __init__(self) -> None:
        super().__init__()
        moneda_inicial = input("elegir una moneda entre clp, arg, eur, try, gdp: ")
        print(f"ingresar cantidad de $ {moneda_inicial}")

        if moneda_inicial == "clp":
            moneda_inicial = self.clp
        elif moneda_inicial == "arg":
            moneda_inicial = self.arg
        elif moneda_inicial == "eur":
            moneda_inicial = self.eur
        elif moneda_inicial == "try":
            moneda_inicial = self.lira
        elif moneda_inicial == "gbp":
            moneda_inicial = self.gbp
        else:
            print("moneda incorrecta")
            print("cerrando programa")
            sys.exit()
        print (moneda_inicial)
        
        
        cantidad = float(input("ingresar cantidad a cambiar: "))
        total_dolares = cantidad / moneda_inicial

        moneda_final = input("ingresar la moneda a la que quiere convertir: ")
        print(f"moneda a convertir: {moneda_final}")
        if moneda_final == "clp":
            moneda_final = self.clp
        elif moneda_final == "arg":
            moneda_final = self.arg
        elif moneda_final == "eur":
            moneda_final = self.eur
        elif moneda_final == "try":
            moneda_final = self.lira
        elif moneda_final == "gbp":
            moneda_final = self.gbp
        else:
            print("moneda incorrecta")
            print("cerrando programa")
            sys.exit()
        print (moneda_final)

        total = (total_dolares * moneda_final) 

        print(f"el total es de:{total} ")

        
menu()