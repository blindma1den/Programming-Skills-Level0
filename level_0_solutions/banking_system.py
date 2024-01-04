import json
from enum import Enum


# Constants
INITIAL_USER_AVAILABLE_MONEY = 2000.0
INITIAL_ACCOUNTS = {
    'anita23': {
        'password': '123456789',
        'money': 1420.4
    },
    'jaimito12': {
        'password': 'crazyjaimito41',
        'money': 420.0
    }
}
JSON_FILE = 'users.json'
BANK_NAME = 'CappaBank'
WELCOME_MENU = f"""
########## Welcome to {BANK_NAME} ##########
Select an option to procceed
1.- Register a new account
2.- Log in your {BANK_NAME} account
3.- Exit
"""
MAIN_MENU = """
########## Welcome to {BANK_NAME}, {user} ##########
Select an option to procceed
1.- Transfer money to another account
2.- Withdraw money from your account
3.- Show your available money
4.- Deposit money into your account
5.- Log out from your account
"""


class InputTypes(Enum):
    # Enum for input types and messages
    REGISTER_ACCOUNT = f'Register a {BANK_NAME} account with username and password'
    LOGIN = f'Log in your {BANK_NAME} account with username and password'
    TRANSFER = f'Transfer money to another account'
    WITHDRAW = f'Transfer money to another account'
    READ = f'Transfer money to another account'
    DEPOSIT = f'Transfer money to another account'


class WelcomeMenuOption(Enum):
    REGISTER = 1
    LOGIN = 2
    EXIT = 3


class MainMenuOption(Enum):
    TRANSFER = 1
    WITHDRAW = 2
    READ = 3
    DEPOSIT = 4
    LOGOUT = 5


class Bank:
    __exit_menu_loop = False    
    __exit_main_loop = False    
    def __init__(self):
        # Initialize the bank should take the json with the accounts and the users if they exist
        self.__users = self.__load_data()
    
    @staticmethod
    def __load_data():
        # Method to load the data from past sessions if it exists, otherwise it returns an empty dictionary
        try:
            with open(JSON_FILE, 'r') as f:
                accounts_data = json.load(f)
        except Exception:
            # Loading initial data so user could transfer if there are not any other user-created user
            accounts_data = INITIAL_ACCOUNTS
        finally:
            return accounts_data
        
    def __user_input(self, input_type: InputTypes):
        while True:
            if input_type == InputTypes.REGISTER_ACCOUNT:
                print(f'\n{InputTypes.REGISTER_ACCOUNT.value}')
                while True:
                    username = input('Type your username (at least 6 characters and less than 20 characters): ')
                    if username in self.__users.keys():
                        print('That username is already in use, try another one')
                        continue
                    elif len(username) < 6 or len(username) > 20:
                        print('The characters must be at least 6 and maximum 20')
                        continue
                    else:
                        break
                while True:
                    password = input('Type your password (at least 8 characters and less than 30 characters): ')
                    if len(username) < 8 or len(username) > 30:
                        print('The characters must be at least 8 and maximum 30')
                        continue
                    else:
                        break
                return username, password
            elif input_type == InputTypes.LOGIN:
                print(f'\n{InputTypes.LOGIN.value}')
                logged_user = False
                for i in range(3):
                    username = input('Type your username: ')
                    password = input('Type your password: ')
                    if username in self.__users.keys():
                        if self.__users[username]['password'] == password:
                            logged_user = True
                        else:
                            print(f'Username or password does not match, you have {2-i} tries left')
                            continue
                    else:
                        print(f'Username or password does not match, you have {2-i} tries left')
                        continue

                if not logged_user:
                    print(f"{'*'*20} WARNING {'*'*20}")
                    print(f'You failed to log in 3 times, try again later, thanks for using {BANK_NAME}')
                    exit
                else:
                    print(f'Welcome back, {username}!')
                    return username
            elif input_type == InputTypes.TRANSFER:
                print(f'\n{InputTypes.TRANSFER.value}')
                while True:
                    objective_account = input('Type the username of the objective account: ')
                    if objective_account == self.current_user:
                        print('You cannot transfer yourself, type another account username')
                        continue
                    if objective_account not in self.__users.keys():
                        print('That username does not belong to any account, try another one')
                        continue
                    else:
                        break
                while True:
                    quantity_to_transfer = input('Type the money quantity to transfer: ')
                    try:
                        quantity_to_transfer = float(quantity_to_transfer)
                    except Exception:
                        print('Wrong input, try again.')
                        continue
                    if quantity_to_transfer < self.__users[self.current_user]['money']:
                        print('You do not have that quantity available in your account, try again.')
                        continue
                    else:
                        break
                return objective_account, quantity_to_transfer
                

    def __register_account(self):
        username, password = self.__user_input(InputTypes.REGISTER_ACCOUNT)

        self.__users[username] = {
            'password': password,
            'money': 2000.0
        }
        self.__save_data()
        self.current_user = username

    def __login(self):
        username = self.__user_input(InputTypes.LOGIN)
        self.current_user = username

    def __save_data(self):
        # Method that will save the data in json format so it can be persistent
        with open(JSON_FILE, 'w') as f:
            json.dump(self.__users, f, indent=4)

    def __transfer_money(self):
        objective_user, quantity_to_transfer = self.__user_input(InputTypes.TRANSFER)
        print(f"\n{'*'*5} Transfer done! {'*'*5}")
        self.__users[self.current_user]['money'] -= quantity_to_transfer
        self.__users[objective_user]['money'] += quantity_to_transfer
        self.__save_data()

    def __withdraw_money(self):
        quantity_to_withdraw = self.__user_input(InputTypes.WITHDRAW)
        self.__users[self.current_user]['money'] -= quantity_to_withdraw
        self.__save_data()

    def __read__money(self):
        print(f"You have {self.__users[self.current_user]['money']} available in your account")

    def __deposit_money(self):
        quantity_to_deposit = self.__user_input(InputTypes.DEPOSIT)
        self.__users[self.current_user]['money'] += quantity_to_deposit
        self.__save_data()

    def __logout(self):
        print(f'\nThanks for your trust in {BANK_NAME}, come back soon, {self.current_user}!')
        self.__exit_menu_loop = True

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
            1: WelcomeMenuOption.REGISTER,
            2: WelcomeMenuOption.LOGIN,
            3: WelcomeMenuOption.EXIT
        }
        
        print(f'\n{WELCOME_MENU}')

        user_option = self.__menu_input(options)

        return options[user_option]

    def __show_main_menu(self) -> MainMenuOption:
        options = {
            1: MainMenuOption.TRANSFER,
            2: MainMenuOption.WITHDRAW,
            3: MainMenuOption.READ,
            4: MainMenuOption.DEPOSIT,
            5: MainMenuOption.LOGOUT
        }
        
        print()
        print(MAIN_MENU.format(BANK_NAME=BANK_NAME, user=self.current_user))
        user_option = self.__menu_input(options)

        return options[user_option]

    def __exit(self):
        print(f'\nThanks for your trust in {BANK_NAME}, come back soon!')
        self.__exit_menu_loop = True

    def main(self):
        # Here lives the control flow of the bank and the stuff that users can do in the bank
        welcome_menu_options = {
            WelcomeMenuOption.REGISTER: self.__register_account,
            WelcomeMenuOption.LOGIN: self.__login,
            WelcomeMenuOption.EXIT: self.__exit
        }

        main_menu_options = {
            MainMenuOption.TRANSFER: self.__transfer_money,
            MainMenuOption.WITHDRAW: self.__withdraw_money,
            MainMenuOption.READ: self.__read__money,
            MainMenuOption.DEPOSIT: self.__deposit_money,
            MainMenuOption.LOGOUT: self.__logout
        }

        while not self.__exit_menu_loop:
            welcome_menu_user_option = self.__show_welcome_menu()
            welcome_menu_options[welcome_menu_user_option]()
            if welcome_menu_user_option != WelcomeMenuOption.EXIT:
                while not self.__exit_main_loop:
                    main_menu_user_option = self.__show_main_menu()
                    main_menu_options[main_menu_user_option]()

        
def run():
    bank = Bank()
    bank.main()


if __name__ == '__main__':
    run()


