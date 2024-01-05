# 5. Develop a finance management application with the following features:
# * 		The user records their total income.
# * 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
# * 		The user can list their expenses within the categories and get the total for each category.
# * 		The user can obtain the total of their expenses.
# * 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
# * 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
# * 		If the user spends more than they earn, the system will display advice to improve the user's financial health.


import sys

class menu:

    def __init__(self) -> None:
        self.select()
  

    def select(self):
        while True:
            print("----------------------")
            print("1. registrar ingresos")
            print("2. ver gastos totales")
            print("3. exit")
            print("----------------------")
            opcion = int(input(f"Enter option: "))
            self.algo(opcion)
            
        
    
    def algo(self, opcion):
        if opcion == 1:

            opciones.ingresos(self)
        elif opcion == 2:
            
            opciones.categorias(self)
        elif opcion == 3:
            sys.exit()
        else:
            print("Invalid option")
       


class opciones(menu):

 


    def ingresos(self):   
      
        self.medicos = 0
        self.hogar = 0
        self.ocio = 0
        self.ahorro = 0
        self.educacion = 0
        
        print("registrar los ingresos")
        self.sueldo = int(input("ingresar sueldo: "))

        print("ingresar los siguientes gastos")

        self.medicos =int(input("ingresar gastos medicos: "))
        self.hogar = int(input("ingresar gastos del hogar: "))
        self.ocio = int(input("ingresar gastos de ocio: "))
        self.ahorro = int(input("ingresar gastos en ahorro: "))
        self.educacion = int(input("ingresar gastos en educacion: "))
        
    
    def categorias(self):
    
        
        total = (self.medicos + self.hogar + self.ocio + self.ahorro + self.educacion)
        
        print(f"El total de los gastos es de: {total} y se dividen en:")
        print(f"medicos: {self.medicos}")
        print(f"hogar: {self.hogar}")
        print(f"ocio: {self.ocio}")
        print(f"ahorro: {self.ahorro}")
        print(f"educacion: {self.educacion}")

        if total > self.sueldo:
            print("Gastas más que tus ingresos")
        elif total < self.sueldo:
            print("tienes más ingresos que gastos. Felicitaciones!")
        else:
            print("tus ingresos son iguales a tus gastos")
        

    







menu()







