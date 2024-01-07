import random

login_attempts = 0

def shipping_system():
    global login_attempts
    if login_attempts >= 3:
        print("You have exceeded the maximum number of login attempts. The system is locked.")
        return
    
    username = input("Username: ")
    password = input("Password: ")
    
    if validate_login(username, password):
        while True:
            print("Main Menu:")
            print("1. Send a Package")
            print("2. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                send_package()
            elif choice == '2':
                print("Thank you for using the shipping system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        login_attempts += 1
        print("Incorrect login credentials. Please try again.")
        shipping_system()

def validate_login(username, password):
    if username == 'admin' and password == 'password':
        return True
    else:
        return False

def send_package():
    sender_name = input("Sender Name: ")
    sender_address = input("Sender Address: ")
    
    recipient_name = input("Recipient Name: ")
    recipient_address = input("Recipient Address: ")
    
    package_weight = float(input("Package Weight (in kg): "))
    
    package_number = random.randint(1000, 9999)
    
    shipping_price = package_weight * 2
    
    print("Package Details:")
    print("Package Number:", package_number)
    print("Sender Name:", sender_name)
    print("Sender Address:", sender_address)
    print("Recipient Name:", recipient_name)
    print("Recipient Address:", recipient_address)
    print("Package Weight:", package_weight, "kg")
    print("Shipping Price: $", shipping_price)
    
    choice = input("Do you want to perform another operation? (yes/no): ")
    
    if choice.lower() == 'yes':
        return
    elif choice.lower() == 'no':
        print("Thank you for using the shipping system. Goodbye!")
        exit()
    else:
        print("Invalid choice. Returning to the main menu.")
        return

shipping_system()