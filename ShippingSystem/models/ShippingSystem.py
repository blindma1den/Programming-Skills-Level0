from random import randint


class ShippingSystem:

    price_per_kg: float

    def __init__(self, price_per_kg: float):
        self.price_per_kg = price_per_kg

    def send_package(self, sender_name: str):
        package_id = randint(1,1000000000)
        print("Package incoming ...")
        weight = float(input("Package weight: "))
        recipient = input("Recipient: ")

        total_price = weight * self.price_per_kg

        print(f"------PACKAGE {package_id}------------")
        print(f"Sender: {sender_name}")
        print(f"Weight: {weight}")
        print(f"Recipient: {recipient}")
        print(f"Total price: ${total_price}")

