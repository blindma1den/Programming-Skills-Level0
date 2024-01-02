from collections import namedtuple


# Obvius upgrade would be consume an API for this, it will be done
# if I have more time
conversions = {
    'USD': 1,
    'CLP': 885.33,
    'ARS': 808.45,
    'EUR': 0.91,
    'TRY': 29.71,
    'GBP': 0.79
}


class Converter:
    def __init__(self):
        self._currencies = {name: value for name, value in conversions.items()}
        self._currencies_str = ', '.join(self._currencies.keys())

    def __user_input(self, message: str, type_of_input: str = 'str') -> str | int | float:
        while True:
            if type_of_input == 'str' and message == 'Choose initial currency':
                print('\nAvailable currencies: ')
                print(self._currencies_str)
                user_input = input(message + ': ').upper()
                if user_input not in self._currencies.keys():
                    print('Wrong currency, try again.')
                    continue
                else:
                    return user_input
            elif type_of_input == 'str' and message == 'Choose objective currency':
                print('\nAvailable currencies: ')
                print(self._currencies_str)
                user_input = input(message + ': ').upper()
                if user_input not in self._currencies.keys() or user_input == self.initial_currency:
                    print('Wrong currency or currency is the same as initial currency, try again.')
                    continue
                else:
                    return user_input

    def main(self):
        # Structure will go here

        # Asking initial currency
        self.initial_currency = self.__user_input('Choose initial currency', 'str')
        self.objective_currency = self.__user_input('Choose objective currency', 'str')


def run():
    converter = Converter()
    converter.main()


if __name__ == '__main__':
    run()