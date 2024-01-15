import getpass, random

user_info = {
  'username': '',
  'password': '',
  'full_name': '',
  'phone_number': ''

}

receiver_info = {
  'full_name': '',
  'phone_number': ''
  }


def validate_username():
  min_username_length = 8
  max_username_length = 12
  attempts = 0
  attempts_limit = 3

  while attempts < attempts_limit:
    username_input = input('Enter your username: ')
    if len(username_input) < min_username_length or len(username_input) > max_username_length:
      attempts += 1
      print('Username input should be between 8 and 12 characters')
    else:
      user_info['username'] = username_input
      break

  if attempts == attempts_limit and not username_input:
    print('You did not input your credentials correctly. System is locked. Try again later.')
    exit()
  elif attempts == attempts_limit:
    print('You input your credentials wrong. System is locked. Try again later.')
    exit()

  return True

def validate_password():
  min_password_length = 10
  max_password_length = 14
  attempts = 0
  attempts_limit = 3

  while attempts < attempts_limit:
    password_input = getpass.getpass('Enter your password: ')
    if len(password_input) < min_password_length or len(password_input) > max_password_length:
      attempts += 1
      print('Password input should be between 10 and 14 characters')
    else:
      user_info['password'] = password_input
      print('\n** ACCESS GRANTED **')
      break

  if attempts == attempts_limit and not password_input:
    print('You did not input your credentials correctly. System is locked. Try again later.')
    exit()
  elif attempts == attempts_limit:
    print('You input your credentials wrong. System is locked. Try again later.')
    exit()

  return True

def login():
  validate_username()
  validate_password()

def shipper_process():
  attempts = 0
  attempts_limit = 3
  phone_length = 11

  while attempts < attempts_limit:
    shipper_full_name = input('Enter your full name: ')
    if not shipper_full_name:
      print('Please, enter your personal information for sending the package.')
      attempts += 1
    else:
      user_info['full_name'] = shipper_full_name
      break

  if attempts == attempts_limit and not shipper_full_name:
    print('You did not input your full name. System is locked. Try again later.')
    exit()

  attempts = 0

  while attempts < attempts_limit:
    shipper_phone_number = input('Enter your phone number: ')
    if len(shipper_phone_number) < phone_length or len(shipper_phone_number) > phone_length:
      print(f'Phone number length is {phone_length}')
      attempts += 1
    else:
      user_info['phone_number'] = shipper_phone_number
      break

  if attempts == attempts_limit and not shipper_phone_number:
    print('You did not input your phone number. System is locked. Try again later.')
    exit()
  elif attempts == attempts_limit:
    print('You did not input your phone number correctly. System is locked. Try again later.')
    exit()

  return True

def receiver_process():
  phone_length = 11
  attempts = 0
  attempts_limit = 3

  while attempts < attempts_limit:
    receiver_full_name = input('Enter receiver\'s full name: ')
    if not receiver_full_name:
      print('Please, enter your personal information for sending the package.')
      attempts += 1
    else:
      receiver_info['full_name'] = receiver_full_name
      break

  if attempts == attempts_limit and not receiver_full_name:
    print('You did not input receiver\'s full name. System is locked. Try again later.')
    exit()

  attempts = 0

  while attempts < attempts_limit:
    receiver_phone_number = input('Enter receiver\'s phone number: ')
    if len(receiver_phone_number) < phone_length or len(receiver_phone_number) > phone_length:
      print(f'Phone number length is: {phone_length}')
      attempts += 1
    else:
      receiver_info['phone_number'] = receiver_phone_number
      break

  if attempts == attempts_limit and not receiver_phone_number:
    print('You did not input receiver\'s phone number. System is locked. Try again later.')
    exit()
  elif attempts == attempts_limit:
    print('You did not input receiver\'s phone number correctly. System is locked. Try again later.')
    exit()

  return True

def calculate_price():
  initial_price = 1
  kilo = 1
  charge_per_kilo = 2
  price_increase = 0
  ticket = random.randint(100000, 999999)

  package_weight = float(input('Please, input the weight of the package with numbers and point. Example: 3.7\n=> '))

  if package_weight < kilo:
    price_increase = 0
  else:
    price_increase = package_weight * charge_per_kilo

  total_price = initial_price + price_increase

  print('**SHIPMENT DETAILS**')
  print(f'Shipper: {user_info["full_name"]} - {user_info["phone_number"]}')
  print(f'Receiver: {receiver_info["full_name"]} - {receiver_info["phone_number"]}')
  print(f'Weight: {package_weight}KG - Total price: ${total_price} - Ticket tracker: {ticket}')

  return True

def try_again():
  repeat = input('Do you want to send another package? Y/N: ')
  repeat = repeat.upper().strip()

  match repeat:
    case 'Y':
      main_menu()
    case 'N':
      print('We let you know when your package has arrived. Take care!')
      exit()
    case _:
      print('Please, enter Y for "Yes" or N for "No"')

def send():
  shipper_process()
  receiver_process()
  calculate_price()
  try_again()

  return True

def main_menu():
  type_option = input('Type an option:\n- Send\n- Exit\n=> ')
  type_option = type_option.lower().strip()

  while not type_option:
    print('TYPE AN OPTION!\n')
    type_option = (input('Type an option:\n- Send\n- Exit\n=> '))
    type_option = type_option.lower().strip()

  match type_option:
    case 'send':
      send()
    case 'exit':
      print('HAVE A NICE DAY!')
      exit()
    case _:
      print('That option does not exist. Try again.')
      main_menu()

def run_app():
  print('WELCOME TO DELIVAIR. Your shipping is safe with us :D\n')
  login()
  main_menu()

run_app()