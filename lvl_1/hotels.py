from datetime import datetime
import getpass

account_info = {
   'username': "",
   'password': "",
   'name': "",
   'surname': "",
   'ID': "",
   'passport': "",
   'chosen_room_type': [],
   'chosen_countries': [],
   'chosen_cities': [],
   'date': ""
   }

hotels = {
  'Spain': ['Madrid','Barcelona','Valencia'],
  'Germany': ['Munich', 'Berlin'],
  'Italy': ['Rome','Milan'],
  'France':['Paris', 'Marseille'],
  'Portugal':['Madeira','Lisbon','Porto']
  }

# Rooms of each hotel
rooms = {
  'Luxury_suites': 3,
  'Vip_suites': 6,
  'Single_rooms': 3,
  'Double_rooms': 6,
  'Group_rooms': 6,
  'total_rooms': 24
  }

# Prices of each type of room
rooms_price = {
  'Luxury_suites': 550,
  'Vip_suites': 450,
  'Single_rooms': 100,
  'Double_rooms': 200,
  'Group_rooms': 350
  }

countries = list(hotels.keys())
spanish_hotels = list(hotels['Spain'])
german_hotels = list(hotels['Germany'])
italian_hotels = list(hotels['Italy'])
french_hotels = list(hotels['France'])
portuguese_hotels = list(hotels['Portugal'])

rooms_list = list(rooms.keys())
prices_list = list(rooms_price.values())

# Login / Register
# ! Update register function. Ask name and surname.
def register():
  min_username_length = 8
  max_username_length = 12
  min_password_length = 10
  max_password_length = 14

  while True:
    register_username = input('Enter the username you want to use: ')
    if len(register_username) < min_username_length or len(register_username) > max_username_length:
      print('** Username input should be between 8 and 12 characters. **\n')
    else:
      account_info['username'] = register_username
      break

  while True:
    register_password = getpass.getpass('Enter the password you want to use: ')
    if len(register_password) < min_password_length or len(register_password) > max_password_length:
      print('** Password input should be between 10 and 14 characters. **')
    else:
      confirm_password = getpass.getpass('Re-enter the password to confirm: ')
      if confirm_password != register_password:
        print('** Passwords are not the same. **')
      else:
        print('** CONGRATULATIONS! Your account has been successfully created. **')
        account_info['password'] = register_password
        break

def validate_username():
  min_username_length = 8
  max_username_length = 12

  while True:
    username_input = input('Enter your username: ')
    if len(username_input) < min_username_length or len(username_input) > max_username_length:
      print('Username input should be between 8 and 12 characters.\n')
    elif username_input != account_info['username']:
      print(f'"{username_input}" does not exist. Try again.\n')
    else:
      break

def validate_password():
  min_password_length = 10
  max_password_length = 14
  attempts = 0
  attempts_limit = 3

  while attempts < attempts_limit:
    password_input = getpass.getpass('Enter your password: ')
    if len(password_input) < min_password_length or len(password_input) > max_password_length:
      attempts += 1
      print('Password input should be between 10 and 14 characters.')
    elif password_input != account_info['password']:
      print(f'Your password is incorrect. Try again.')
      attempts += 1
    else:
      print('\n** ACCESS GRANTED **')
      break

  if attempts == attempts_limit and not password_input:
    print('You input your credentials wrong. System is locked. Try again later.')
    exit()
  elif attempts == attempts_limit:
    print('You did not input your credentials correctly. System is locked. Try again later.')
    exit()

def login():
  validate_username()
  validate_password()

def login_menu():
  options = ['1. Register', '2. Login', '0. Exit']

  for option in options:
    print(f'- {option}')

  choose_option = input('Enter a number: ')

  match choose_option:
    case '1':
      register()
      login_menu()
    case '2':
      login()
    case '0':
      print('Have a nice day!')
      exit()
    case _:
      print('That option does not exist.')
      login_menu()

"""
# TODO
- Show countries
- Show cities
- Show rooms and their prices
- Ask the number of nights
- Ask date and time
- Ask ID/Passport
"""

def run_app():

  login_menu()

run_app()