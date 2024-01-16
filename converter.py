# 2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
# * 		The user must choose their initial currency and the currency they want to exchange to.
# * 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
# * 		If the user decides to withdraw the funds, the system will charge a 1% commission.
# * 		Set a minimum and maximum amount for each currency, it can be of your choice.
# * 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.


#Variables iniciales: 

balance_init = 2000
transfer_user = ''
account = int

while True:
    print('1. CLP - Pesos Chilenos')
    print('2. ARS - Pesos Argentinos')
    print('3. USD - Dólares Americanos ')
    print('4. EUR - Euros')
    print('5. TRY - Liras Turcas')
    print('6. GBP - Libras Esterlinas')

opcion = int(input('Ingrese la divisa que tiene: '))



while True:
    print('Convertidor de divisas')
    print('1. CLP - Pesos Chilenos')
    print('2. ARS - Pesos Argentinos')
    print('3. USD - Dólares Americanos ')
    print('4. EUR - Euros')
    print('5. TRY - Liras Turcas')
    print('6. GBP - Libras Esterlinas')