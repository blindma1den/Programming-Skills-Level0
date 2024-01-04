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


class InputTypes(Enum):
    # Enum for input types and messages
    REGISTER_ACCOUNT = f'Register a {BANK_NAME} account with username and password'
    LOGIN = f'Log in your {BANK_NAME} account with username and password'


class Bank:
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
        pass

    def __withdraw_money(self):
        pass

    def __read__money(self):
        pass

    def __deposit_money(self):
        pass

    def __show_menu(self):
        pass

    def main(self):
        pass

        
def run():
    bank = Bank()
    bank.main()


if __name__ == '__main__':
    run()


