from enum import Enum

# I use constants and ENUM to avoid the use of hardcoded strings and magic numbers inside the code structure, avoiding possible errors
GET_INIT_CURRENCY_MSG = 'Type initial currency'
GET_OBJECTIVE_CURRENCY_MSG = 'Type objective currency'
GET_VALUE_MSG = 'Type the amount of money to convert'
GET_WITHDRAW_CONFIRMATION = 'Do you want to withdraw your converted money?'
ASK_TO_RESTART_PROGRAM = 'Do you want to perform another conversion?'
WITHDRAW_STRING = """
{decor}
Current currency: {objective_currency}
Amount of money: {result}
Commission (1%): {commission}
Total (- commission): {total} 
{decor}
"""


# Obvius upgrade would be consume an API for this, it will be done
# if I have more time
class Currencies(Enum):
    USD = 1.0
    CLP = 885.33
    ARS = 808.45
    EUR = 0.91
    TRY = 29.71
    GBP = 0.79


class Converter:
    minimum_value = 15.0
    maximum_value = 999.9
    def __init__(self):
        self._currencies = [
            Currencies.USD.name, Currencies.CLP.name, Currencies.ARS.name, Currencies.EUR.name, Currencies.TRY.name, Currencies.GBP.name
        ]
        self._currencies_str = ', '.join(self._currencies)

    def __user_input(self, message: str) -> str | float | bool:
        # The most important method of the program, it manages the user input, getting strings and float numbers from the user and managing
        # Errors
        while True:
            if message == GET_VALUE_MSG:
                string = message.replace('money', self.initial_currency)
                user_input = input(f'\n{string}, the minimum value is {self.minimum_value} and the maximum value is {self.maximum_value}: ')
                try:
                    user_input = float(user_input)
                except Exception:
                    print('Wrong input, the value must be a number')
                    continue
                finally:
                    if user_input < self.minimum_value or user_input > self.maximum_value:
                        print('The amount is not between the permited minumum and maximum values to convert, try again.')
                        continue
                    else:
                        return user_input
            elif message == GET_WITHDRAW_CONFIRMATION:
                commission = self.result * 0.01
                total = self.result - commission
                string = WITHDRAW_STRING.format(
                    decor='*'*15, 
                    objective_currency=self.objective_currency,
                    result=self.result,
                    commission=commission,
                    total=total
                    )
                print(string)
                user_input = input(f'{GET_WITHDRAW_CONFIRMATION} (Y/N): ').upper()
                if user_input not in ['Y', 'N']:
                    print('Wrong input, try again')
                    continue
                else:
                    return True if user_input == 'Y' else False
            elif message == ASK_TO_RESTART_PROGRAM:
                user_input = input(f'\n{message} (Y/N): ').upper()
                if user_input not in ['Y', 'N']:
                    print('Wrong input, try again')
                    continue
                else:
                    return True if user_input == 'Y' else False
            elif message == GET_INIT_CURRENCY_MSG:
                print('\nAvailable currencies: ')
                print(self._currencies_str)
                user_input = input(message + ': ').upper()
                if user_input not in self._currencies:
                    print('Wrong currency, try again.')
                    continue
                else:
                    return user_input
            elif message == GET_OBJECTIVE_CURRENCY_MSG:
                print('\nAvailable currencies: ')
                print(self._currencies_str)
                user_input = input(message + ': ').upper()
                if user_input not in self._currencies or user_input == self.initial_currency:
                    print('Wrong currency or currency is the same as initial currency, try again.')
                    continue
                else:
                    return user_input
                
    def __convert_from_usd(self) -> float:
        return self.money_amount * getattr(Currencies, self.objective_currency).value
    
    def __convert_currency(self) -> float:
        self.money_amount = self.money_amount / getattr(Currencies, self.initial_currency).value
        return self.__convert_from_usd()

    def main(self):
        while True:
            # Getting initial values
            print(f"\n\n\n{'#'*10} CURRENCY CONVERTER {'#'*10}")
            self.initial_currency = self.__user_input(GET_INIT_CURRENCY_MSG)
            self.objective_currency = self.__user_input(GET_OBJECTIVE_CURRENCY_MSG)

            self.money_amount = self.__user_input(GET_VALUE_MSG)

            # Converting the currencies
            if self.initial_currency == Currencies.USD.name:
                self.result = self.__convert_from_usd()
            else:
                self.result = self.__convert_currency()

            # Showing the results to the user and asking if the user will withdraw the money
            self.ask_to_withdraw = self.__user_input(GET_WITHDRAW_CONFIRMATION)

            if self.ask_to_withdraw:
                print('Thank you, you will receive your converted currency in your bank account.')
            else:
                print('Ok, no money will be discounted from your bank account.')

            # Getting user input to know if the program should restart or not
            restart_program = self.__user_input(ASK_TO_RESTART_PROGRAM)

            if not restart_program:
                print('See you next time!')
                break


def run():
    converter = Converter()
    converter.main()


if __name__ == '__main__':
    run()