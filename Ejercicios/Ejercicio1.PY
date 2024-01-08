import sys


class account:    
    def __init__(self):
        self.user = "a"
        self.password = "1"
        self.balance = 2000

    def balance(self):
        print(self.balance)

class login(account):
    def __init__(self):
        super().__init__()
        self.failed_attempts = 0
    
    def verify_user(self, input_user, input_password):
        if input_user == self.user and input_password == self.password:
            print("Successful Login!!")

            return True
            
        else:
            print("Incorrect Password!")
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                print("error number 3. The program will close")
                sys.exit()
            return False



class menu(account):
    def select(self):
    
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Transfer money")
        print("5. Exit")
    
    
    
        self.opcion = int(input(f"Enter option: "))
        return self.opcion


class actions(menu):
    
    def deposit(self):
        to_deposit = int(input(f"Enter amount to DEPOSIT: "))
        self.balance += to_deposit
        print(f"The updated balance is: {self.balance}")
        
   
    def withdraw(self):
        will_withdraw = int(input(f"Enter amount to WITHDRAW: "))
        self.balance -= will_withdraw
        print(f"The updated balance is: {self.balance}")
   
    def check_balance(self):
        print(f"The account balance is: {self.balance} ")
        
   
    def transfer_money(self):
        friend = input(f"Enter user to transfer: ")
        to_transfer = int(input(f"Enter amount to transfer: "))
        self.balance -= to_transfer
        print(f"Will be transdered: {to_transfer}")
        print(f"to the user: {friend}")
        print(f"updated balance: {self.balance}")
   
    def exit(self):
        print("exit")
        sys.exit()

    def numbers(self, opcion):
        if opcion == 1:
            self.deposit()
        elif opcion == 2:
            self.withdraw()
        elif opcion == 3:
            self.check_balance()
        elif opcion == 4:
            self.transfer_money()
        elif opcion == 5:
            self.exit()
        else:
           print("Invalid option")


if __name__ == "__main__":
    login_instance = login()

    logging = False
    while not logging:
        input_user = input("Enter your username: ")
        input_password = input("Enter your password: ")
        logging = login_instance.verify_user(input_user, input_password)
    menu_instance = menu()
    
    actions_instance = actions()
    while True:
        opcion = menu_instance.select()
        actions_instance.numbers(opcion)
        
           

