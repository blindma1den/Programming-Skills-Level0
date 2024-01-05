import sys
import uuid
from enum import Enum


# CONSTANTS
INITIAL_ACCOUNTS = {
    'anita23': '123456789',
    'jaimito12': 'crazyjaimito41',
    'maria413': 'unabuenapassword',
    'juancito14': '987654321'
}
SYSTEM_NAME = 'CappaShipping'
WELCOME_MENU = f"""
########## Welcome to {SYSTEM_NAME} ##########
Select an option to procceed
1.- Log in your {SYSTEM_NAME} account
2.- Exit
"""
MAIN_MENU = """
########## Welcome to {SYSTEM_NAME}, {user} ##########
Select an option to procceed
1.- Send a package
2.- See sent packages
3.- Exit system
"""
DISPLAY_SENT_PACKAGES_MSG = """
Package number: {package_number}
Sender: {sender}
Receiver: {receiver}
Target location: {target_location}
Price: {price}
Weight: {weight}
"""


class InputTypes(Enum):
    # Enum for input types and messages
    LOGIN = f'Log in your {SYSTEM_NAME} account with username and password'
    SEND_PACKAGE = F'You will send a package, we need some data before we can send it'


class WelcomeMenuOption(Enum):
    LOGIN = 1
    EXIT = 2


class MainMenuOption(Enum):
    SEND_PACKAGE = 1
    SEE_SENT_PACKAGES = 2
    LOGOUT = 3


class ShippingSystem:
    sent_packages = {}
    __exit_menu_loop = False    
    __exit_main_loop = False    

    def __user_input(self, input_type: InputTypes):
        if input_type == InputTypes.LOGIN:
            print(f'\n{InputTypes.LOGIN.value}')
            logged_user = False
            for i in range(3):
                username = input('Type your username: ')
                password = input('Type your password: ')
                if username in INITIAL_ACCOUNTS.keys():
                    if INITIAL_ACCOUNTS[username] == password:
                        logged_user = True
                        break
                    else:
                        print(f'Username or password does not match, you have {2-i} tries left')
                        continue
                else:
                    print(f'Username or password does not match, you have {2-i} tries left')
                    continue

            if not logged_user:
                print(f"{'*'*20} WARNING {'*'*20}")
                print(f'You failed to log in 3 times, try again later, thanks for using {SYSTEM_NAME}')
                sys.exit()
            else:
                print(f'Welcome back, {username}!')
                return username
        elif input_type == InputTypes.SEND_PACKAGE:
            print(f'\n{InputTypes.SEND_PACKAGE.value}')
            self.__receiver = input('Type the name of the receiver: ')
            self.__target_location = input('Type the location of the receiver: ')
            while True:
                weight = input('Type the weight of the package: ')
                try:
                    weight = float(weight)
                except Exception:
                    print('Wrong input, try again.')
                    continue
                if weight <= 0.0:
                    print('You have to type a positive number')
                    continue
                else:
                    self.__weight = weight
                    break

    def __login(self):
        username = self.__user_input(InputTypes.LOGIN)
        self.current_user = username

    def __send_package(self):
        package_number = uuid.uuid4()
        self.__user_input(InputTypes.SEND_PACKAGE)
        self.sent_packages[package_number] = {
            "sender": self.current_user,
            "receiver": self.__receiver,
            "target_location": self.__target_location,
            "price": self.__weight * 2,
            "weight": self.__weight,
        }

    def __see_sent_packages(self):
        if len(self.sent_packages) == 0:
            print('\nYou have not sent any packages yet')
        else:
            print('\nYou have sent these packages')
            for package in self.sent_packages.keys():
                print()
                print(DISPLAY_SENT_PACKAGES_MSG.format(
                    package_number=package,
                    sender=self.sent_packages[package]['sender'],
                    receiver=self.sent_packages[package]['receiver'],
                    target_location=self.sent_packages[package]['target_location'],
                    price=self.sent_packages[package]['price'],
                    weight=self.sent_packages[package]['weight'],
                ))

    def __menu_input(self, options: dict):
        while True:
            user_option = input('Type the number of the option you want to select: ')
            
            try:
                user_option = int(user_option)
            except Exception:
                print('Wrong input, try again.')
                continue
            
            if not user_option in options.keys():
                print('Wrong input, try again.')
                continue

            break
        return user_option

    def __show_welcome_menu(self) -> WelcomeMenuOption:
        options = {
            1: WelcomeMenuOption.LOGIN,
            2: WelcomeMenuOption.EXIT
        }
        
        print(f'\n{WELCOME_MENU}')

        user_option = self.__menu_input(options)

        return options[user_option]
    
    def __show_main_menu(self) -> MainMenuOption:
        options = {
            1: MainMenuOption.SEND_PACKAGE,
            2: MainMenuOption.SEE_SENT_PACKAGES,
            3: MainMenuOption.LOGOUT
        }
        
        print()
        print(MAIN_MENU.format(SYSTEM_NAME=SYSTEM_NAME, user=self.current_user))
        user_option = self.__menu_input(options)

        return options[user_option]
    
    def __exit(self):
        print(f'\nThanks for your trust in {SYSTEM_NAME}, come back soon!')
        self.__exit_menu_loop = True

    def __logout(self):
        print(f'\nThanks for your trust in {SYSTEM_NAME}, come back soon, {self.current_user}!')
        self.__exit_main_loop = True

    def main(self):
        welcome_menu_options = {
            WelcomeMenuOption.LOGIN: self.__login,
            WelcomeMenuOption.EXIT: self.__exit
        }

        main_menu_options = {
            MainMenuOption.SEND_PACKAGE: self.__send_package,
            MainMenuOption.SEE_SENT_PACKAGES: self.__see_sent_packages,
            MainMenuOption.LOGOUT: self.__logout
        }

        while not self.__exit_menu_loop:
            self.__exit_main_loop = False
            welcome_menu_user_option = self.__show_welcome_menu()
            welcome_menu_options[welcome_menu_user_option]()
            if welcome_menu_user_option != WelcomeMenuOption.EXIT:
                while not self.__exit_main_loop:
                    self.__exit_menu_loop = False
                    main_menu_user_option = self.__show_main_menu()
                    main_menu_options[main_menu_user_option]()


def run():
    shipping_system = ShippingSystem()
    shipping_system.main()


if __name__ == '__main__':
    run()