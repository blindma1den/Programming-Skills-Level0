'''
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.   2. 
'''



# dictionary of users
users = {}

'''
1. Register and login
'''
# New user
def user():
    
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    if username not in users: 
        users[username] = {'password': password, 'balance': 2000.0} #puts the new username in the variable users and its password.
        print("Registered successfully.")
    else:
        print("Username already exists. Please choose a different username.")

# total attempts


attempts= 0

# Login and lockout 
def login():
    
    global attempts
    while attempts < 3:
        
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if username in users:
            if users[username]['password'] == password: #checks if the username and password exist and if they do you can acess successfully.
                print("Welcome,", username)
                return True, username
            else:
                attempts += 1
                print("Invalid username or password.")
                print("Attempts:", attempts, "Remember you only have 3 attempts to access your account.")
        else:
            print("Invalid username or password.")
    else:
        print("You cannot access your account. Too many unsuccessful attempts")
        return False, None
              


'''
4. deposit, withdraw, view, and transfer money.
5. menu for users to perform transactions
'''

def menu():
    login_successful, username = login()
    if login_successful:
        print("\nMenu:")
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

    num = input("Choose a nuber (1-5): ")

    if num == '1':
        print('Balance:', users[username]['balance'])
    elif num =='2':
        deposit= float(input('Deposit Amount: '))
        users[username]['balance'] += deposit
        print('New balance:', users[username]['balance'])
    elif num == '3':
        withdraw= float(input('Withdraw Amount: '))
        users[username]['balance'] -= withdraw
        print('New balance:', users[username]['balance'])
    elif num == '4':
        print("Logout successful.")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

user()        

menu()












