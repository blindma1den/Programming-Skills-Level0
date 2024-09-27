from datetime import datetime
import getpass, random

account_info = {
   'username': "",
   'password': "",
   'name': "",
   'surname': "",
   'ID': "",
   'passport': "",
   'chosen_room_types': [],
   'chosen_country': '',
   'chosen_city': '',
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
def register():
  min_username_length = 8
  max_username_length = 12
  min_password_length = 10
  max_password_length = 14

  name_register = input('Enter your name: ')
  account_info['name'] = name_register.capitalize()
  surname_register = input('Enter your surname: ')
  account_info['surname'] = surname_register.capitalize()

  while True:
    register_username = input('Enter the username you want to use: ')
    if len(register_username) < min_username_length or len(register_username) > max_username_length:
      print('** Username input should be between 8 and 12 characters. **\n')
    else:
      account_info['username'] = register_username.lower()
      break

  while True:
    register_password = getpass.getpass('Enter the password you want to use: ')
    if len(register_password) < min_password_length or len(register_password) > max_password_length:
      print('\n** Password input should be between 10 and 14 characters. **\n')
    else:
      confirm_password = getpass.getpass('Re-enter the password to confirm: ')
      if confirm_password != register_password:
        print('\n** Passwords are not the same. **\n')
      else:
        print('\n** CONGRATULATIONS! Your account has been successfully created. **\n')
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

def booking():
  time = datetime.now()
  company_name = 'RH Hotels'
  current_date = time.strftime('%x')
  current_time = time.strftime('%H:%M')
  greetings = ['Hello,', 'Welcome,', 'Hey there,', 'Hi,']

  print(f'\n** {greetings[random.randint(0,3)]} {account_info["name"]} to {company_name}!')
  print(f'Date: {current_date} - Time: {current_time} **\n')

  def choose_country():

    print('Our best hotels are in these countries:')
    i = 0
    for country in countries:
      i += 1
      print(f'{i}. {country}')

    ask_country = int(input('\nWhat country are you traveling to?\nEnter a number: '))

    match ask_country:
      case 1:
        account_info['chosen_country'] = countries[0]
      case 2:
        account_info['chosen_country'] = countries[1]
      case 3:
        account_info['chosen_country'] = countries[2]
      case 4:
        account_info['chosen_country'] = countries[3]
      case 5:
        account_info['chosen_country'] = countries[4]
      case _:
        print('This option does not exist. Try again\n')
        choose_country()

  def choose_city():
    print(f'\nYou selected: {account_info["chosen_country"]}')
    print('Now, choose a city:')

    if account_info['chosen_country'] == countries[0]:
      i = 0
      for city in spanish_hotels:
        i += 1
        print(f'{i}. {city}')

      ask_city = int(input('\nWhat city would you like to stay?\nEnter a number: '))
      match ask_city:
        case 1:
          account_info['chosen_city'] = spanish_hotels[0]
        case 2:
          account_info['chosen_city'] = spanish_hotels[1]
        case 3:
          account_info['chosen_city'] = spanish_hotels[2]
        case _:
          print('This option does not exist. Try again')
          choose_city()

    elif account_info['chosen_country'] == countries[1]:
      i = 0
      for city in german_hotels:
        i += 1
        print(f'{i}. {city}')

      ask_city = int(input('\nWhat city would you like to stay?\nEnter a number: '))
      match ask_city:
        case 1:
          account_info['chosen_city'] = german_hotels[0]
        case 2:
          account_info['chosen_city'] = german_hotels[1]
        case 3:
          account_info['chosen_city'] = german_hotels[2]
        case _:
          print('This option does not exist. Try again')
          choose_city()

    elif account_info['chosen_country'] == countries[2]:
      i = 0
      for city in italian_hotels:
        i += 1
        print(f'{i}. {city}')

      ask_city = int(input('\nWhat city would you like to stay?\nEnter a number: '))
      match ask_city:
        case 1:
          account_info['chosen_city'] = italian_hotels[0]
        case 2:
          account_info['chosen_city'] = italian_hotels[1]
        case 3:
          account_info['chosen_city'] = italian_hotels[2]
        case _:
          print('This option does not exist. Try again')
          choose_city()

    elif account_info['chosen_country'] == countries[3]:
      i = 0
      for city in french_hotels:
        i += 1
        print(f'{i}. {city}')

      ask_city = int(input('\nWhat city would you like to stay?\nEnter a number: '))
      match ask_city:
        case 1:
          account_info['chosen_city'] = french_hotels[0]
        case 2:
          account_info['chosen_city'] = french_hotels[1]
        case 3:
          account_info['chosen_city'] = french_hotels[2]
        case _:
          print('This option does not exist. Try again')
          choose_city()

    elif account_info['chosen_country'] == countries[4]:
      i = 0
      for city in portuguese_hotels:
        i += 1
        print(f'{i}. {city}')

      ask_city = int(input('\nWhat city would you like to stay?\nEnter a number: '))
      match ask_city:
        case 1:
          account_info['chosen_city'] = portuguese_hotels[0]
        case 2:
          account_info['chosen_city'] = portuguese_hotels[1]
        case 3:
          account_info['chosen_city'] = portuguese_hotels[2]
        case _:
          print('This option does not exist. Try again')
          choose_city()

  choose_country()
  choose_city()

  #def choose_room_type():

  #def number_of_nights():

  #def collect_data():


def login():
  validate_username()
  validate_password()

def login_menu():
  farewells = ['Goodbye', 'See you soon', 'Take care']
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
      print(f'{farewells[random.randint(0,2)]}!')
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

  #login_menu()
  booking()

run_app()