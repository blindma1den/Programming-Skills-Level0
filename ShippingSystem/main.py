from models.User import User
from models.ShippingSystem import ShippingSystem


def load_initial_user():
    user = User(username="cval",password="pass")
    return user


def main():
    user = load_initial_user()
    system = ShippingSystem(price_per_kg=2.0)
    loop = True
    logged_in = False
    while loop:
        print("1. Log in user")
        print("2. Exit")
        option = int(input("Option: "))

        if option == 1:
            logged_in = user.login_user()
            loop = False
        else:
            loop = False

    while logged_in:
        print("1. Send package")
        print("2. Exit")
        option = int(input("Option: "))

        if option == 1:
            system.send_package(user.username)
        else:
            logged_in = False


if __name__ == "__main__":
    main()

