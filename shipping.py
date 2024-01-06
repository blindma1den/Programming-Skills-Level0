import sys
import uuid


class Account:
    wrong_login_details_counter = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def price(weight):
        price = weight * 2
        return price

    @staticmethod
    def package_uuid():
        return uuid.uuid4()


account1 = Account("online", "shipping")

print("Welcome to the Online Shipping System")
print("Please login to your account")
print("---------------------------------")
while True:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username != account1.username or entered_password != account1.password:
        account1.wrong_login_details_counter += 1
        if account1.wrong_login_details_counter == 3:
            sys.exit(0)

    print("You have logged in")
    break

while True:
    print("To ship a package, enter 1")
    print("To exit, enter 2")
    choice = input("Please enter the action you want to perform: ")

    if choice == "2":
        sys.exit(0)

    print("Requesting shipper details.")
    name = input("Enter your name: ")
    package_weight = int(input("Enter your package weight: "))

    print("Requesting recipient details.")
    recipient_name = input("Enter your recipient name: ")
    recipient_address = input("Enter your recipient address: ")

    print(f"The shipping price is {account1.price(package_weight)}")

    print("This is the information in your shipping label:")
    print(f"Sender: {name}")
    print(f"Receiver: {recipient_name}")
    print(f"Address: {recipient_address}")
    print(f"Package Weight: {package_weight}")
    print(f"Tracking number: {account1.package_uuid()}")

    input("Press any key to continue...")