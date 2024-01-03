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


class InputTypes(Enum):
    # Enum for input types and messages
    REGISTER_ACCOUNT = 1
    REGISTER_ACCOUNT_MSG = 'Register with username and password'


class Bank:
    def __init__(self):
        # Initialize the bank should take the json with the accounts and the users if they exist
        self.users = self.__load_data()
    
    @staticmethod
    def __load_data():
        # Method to load the data from past sessions if it exists, otherwise it returns an empty dictionary
        try:
            with open('users.json', 'r') as f:
                accounts_data = json.load(f)
                f.close
        except Exception as e:
            # Loading initial data so user could transfer if there are not any other user-created user
            accounts_data = INITIAL_ACCOUNTS
        finally:
            return accounts_data
        
    def __register_account(self):
        username, password = self.__user_input(InputTypes.REGISTER_ACCOUNT.value)

        self.users[username] = {
            'password': password,
            'money': 2000.0
        }

    def __login(self):
        pass

    def __save_data(self):
        # Method that will save the data in json format so it can be persistent
        pass

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


