#1. Create an online banking system with the following features:

#* Users must be able to log in with a username and password.
#* If the user enters the wrong credentials three times, the system must lock them out.
#* The initial balance in the bank account is $2000.
#* The system must allow users to deposit, withdraw, view, and transfer money.
#* The system must display a menu for users to perform transactions.
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Account():
    """A class to represent a bank account for an online banking system.

    Attributes:
        username (str): The account username.
        password (str): The hashed password for the account.
        balance (int): The account balance. Initialized to $2000.
        login_attempts (int): The number of unsuccessful login attempts.
        locked (bool): Status indicating whether the account is locked.
    """
    
    def __init__(self, username, password) -> None:
        
        """Initialize a new account with a username and password."""
        
        self.username = username
        self.set_security_password(password)
        #self.hashed = False
        self.balance = 2000
        self.login_attempts = 0
        self.locked = False
                
    def set_security_password(self, password) -> None:
        
        """Hash the provided password and store it."""
        
        self.password = pwd_context.hash(password)
        
    def verify_password(self, password) -> bool:
        
        """Verify the provided password against the stored hash.

        Locks the account after 3 unsuccessful attempts.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        
        if self.locked:
            print("Account is locked")
            return False
        
        if pwd_context.verify(password, self.password):
            self.login_attempts = 0
            return True
        
        else:
            self.login_attempts += 1
            if self.login_attempts >= 3:
                self.locked = True
                print("Failed 3 times or more, Account Locked")
                return False 
        
        return pwd_context.verify(password, self.password)
    
    #In this features, i have to managed balance or amount = 0
    def deposit(self,deposit) -> None:
        
        """Increase the account balance by the deposit amount."""
        
        self.balance += deposit
        print("Your deposit was sucesfully")
    
    def withdraw(self,withdraw) -> None:
        
        """Decrease the account balance by the withdrawal amount."""

        self.balance -= withdraw
        print("Amount retired")
    
    def view(self) -> None:
        
        """Print the current account balance."""
        
        print(f"Your balance is ${self.balance}")
    
    def transfer(self, account, amount):
        
        """Transfer amount to another account.

        Decreases the sender's balance and increases the recipient's balance.
        """
        
        self.balance -= amount
        account.balance += amount
        print("The Transfer was succesfully")

def verify_account():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        
        if username in accounts:
            
            user_account = accounts[username]
            
            if user_account.locked:
                print("Account is locked due to multiple failed login attempts.")
                return None
            
            if accounts[username].verify_password(password):
                #current_account = accounts[username]
                print("Login Succesfull")
                return user_account
            
            else:
                print("Wrong Password, please try again")
                if user_account.locked:
                    print("Your account has been locked")
                    return None
                continue
        else:
            accounts[username] = Account(username, password)
            #current_account = accounts[username]
            print("Account created")
            return accounts[username]


accounts = {} # Store accounts (maybe a little db)

def main():
    
    
    current_account = None
    
    while True:
        print("\nWelcome to the Online Banking System")
        print("1. Login / Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Transfer Money")
        print("6. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            current_account = verify_account()
            if current_account is None:
                print("Exiting the system because locked account")
                break
            
        elif choice == '2':
            if current_account:
                amount = float(input("Please enter amount to deposit: "))
                current_account.deposit(amount)
            else:
                print("Please be logged")
        elif choice == '3':
            if current_account:
                amount = float(input("Please enter amount to withdraw: "))
                current_account.withdraw(amount)
            else:
                print("Please be logged")
        elif choice == '4':
            if current_account:
                #amount = float(input("Please enter amount to withdraw: "))
                current_account.view()
            else:
                print("Please be logged")
        elif choice == '5':
            if current_account:
                amount = float(input("Please enter amount to transfer: "))
                second_account = input("Please enter the account to transfer: ")
                if second_account in accounts:
                    current_account.transfer(accounts[second_account], amount)
                else:
                    print("Not account Found")
            else:
                print("Please be logged")

        elif choice == '6':
            print("Exit")
            break

        else:
            print("Invalid option, try again.")
    
    #Testing if password is correctly hashed
    #print(accounts)
    #print(accounts[username].username)
    #print(accounts[username].password)
            
if __name__ == "__main__":
    main()
    
# Note: This script requires a specific version of bcrypt library (e.g., bcrypt==4.0.1)
# due to compatibility issues with newer versions. Ensure to install the correct version
# with `pip install bcrypt==4.0.1`.