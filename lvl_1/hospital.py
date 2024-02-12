'''
The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.
'''

from datetime import datetime
import getpass

user_info = {
   'username': '',
   'password': '',
   }

specialties = {
  'general medicine': ['Joseph Gregory Hernandez', 'James Wilson', 'Eric Foreman'],
  'emergency care': ['Simon Diaz', 'Wendy Sulca', 'Colibritany'],
  'clinical analysis': ['Logan Roy', 'Kendall Roy', 'Connor Roy'],
  'cardiology': ['Tuco Salamanca', 'Lalo Salamanca', 'Hector Salamanca'],
  'neurology': ['Robert Speedwagon', 'Ulrich Nielsen', 'Sun Bak'],
  'nutrition': ['Walter White Jr.', 'Carmen Berzatto', 'Joseph Joestar'],
  'physiotherapy': ['Joel Miller', 'Lily Allen', 'Ricky Martin'],
  'traumatology': ['Ted Mosby', 'Shiv Roy', 'Lois Wilkerson'],
  'internal medicine': ['Hugh House', 'Walter White', 'Monica Geller']
  }

specialties_list = list(specialties)
general_medicine_list = specialties['general medicine']
emergency_care_list = specialties['emergency care']
clinical_analysis_list = specialties['clinical analysis']
cardiology_list = specialties['cardiology']
neurology_list = specialties['neurology']
nutrition_list = specialties['nutrition']
physiotherapy_list = specialties['physiotherapy']
traumatology_list = specialties['traumatology']
internal_medicine_list = specialties['internal medicine']

# => login

def register():
  min_username_length = 8
  max_username_length = 12
  min_password_length = 10
  max_password_length = 14

  while True:
    register_username = input('Enter the username you want to use: ')
    if len(register_username) < min_username_length or len(register_username) > max_username_length:
      print('Username input should be between 8 and 12 characters')
      register_username = input('Enter the username you want to use: ')
    else:
      user_info['username'] = register_username
      break

  while True:
    register_password = getpass.getpass('Enter the password you want to use: ')
    if len(register_password) < min_password_length or len(register_password) > max_password_length:
      print('Password input should be between 10 and 14 characters')
      register_password = getpass.getpass('Enter the password you want to use: ')
    else:
      confirm_password = getpass.getpass('Re-enter the password to confirm: ')
      if confirm_password != register_password:
        print('Passwords are not the same')
        confirm_password = getpass.getpass('Re-enter the password to confirm: ')
      else:
        print('Registration successful!')
        user_info['password'] = register_password
      break

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
    elif username_input != user_info['username']:
      print(f'"{username_input}" does not exist. Try again.')
      attempts += 1
    else:
      break

  if attempts == attempts_limit and not username_input:
    print('You did not input your credentials. System is locked. Try again later.')
    exit()
  elif attempts == attempts_limit:
    print('You did not input your credentials correctly. System is locked. Try again later.')
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
    elif password_input != user_info['password']:
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

  return True

def login():
  validate_username()
  validate_password()

def login_menu():
  options = ['1. Register', '2. Login', '3. Exit']

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

def choose_general_medicine():
  i = 0

  if specialties_list[0] in user_info['chosen_specialties']:
    print(f'You cannot book another appointment for General Medicine.')
    choose_specialty()

  while i < len(specialties):
    for specialist in specialties['general medicine']:
      i += 1
      print(f'{i}. {specialist}')
    print('0. Back')
    break

  choose_specialist = input('Enter the number of the specialist: ')

  match choose_specialist:
    case'1':
      if general_medicine_list[0] in user_info['chosen_specialists']:
        print(f'You already booked an appointment with {general_medicine_list[0]}. Try again.\n')
        choose_specialty()
      else:
        user_info['chosen_specialties'].append(specialties_list[0])
        user_info['chosen_specialists'].append(general_medicine_list[0])
        print(f'Your appointment is booked with {general_medicine_list[0]}')
    case'2':
      if general_medicine_list[1] in user_info['chosen_specialists']:
        print(f'You already booked an appointment with {general_medicine_list[1]}. Try again.\n')
        choose_specialty()
      else:
        user_info['chosen_specialties'].append(specialties_list[0])
        user_info['chosen_specialists'].append(general_medicine_list[1])
        print(f'Your appointment is booked with {general_medicine_list[1]}')
    case'3':
      if general_medicine_list[2] in user_info['chosen_specialists']:
        print(f'You already booked an appointment with {general_medicine_list[2]}. Try again.\n')
        choose_specialty()
      else:
        user_info['chosen_specialties'].append(specialties_list[0])
        user_info['chosen_specialists'].append(general_medicine_list[2])
        print(f'Your appointment is booked with {general_medicine_list[2]}')
    case '0':
      choose_specialty()
    case _:
      print(f'\n** The option "{choose_specialist}" option does not exist. Try again. **\n')

  while True:
    book_again = input('Do you want to book another appointment? Y/N => ')
    book_again = book_again.upper().strip()
    if book_again == 'Y':
      choose_specialty()
    elif book_again == 'N':
      main_menu()
    else:
      print('You have to enter "Y" for Yes or "N" for No')

# => schedule

def choose_specialty():
  i = 0
  booking_limit = 3

  while i < len(specialties):
    for specialty in specialties:
      i += 1
      print(f'{i}. {specialty.capitalize()}')
    print('0. Back')
    break

  choice = input('Enter the number of the specialty you need: ')

  if len(user_info['chosen_specialties']) == booking_limit:
    print('You cannot book another appointment because you have reached the limit.')
    choose_specialty()
  

  match choice:
    case '1':
      choose_general_medicine()
    case '0':
      main_menu()
    case _:
      print(f'\n** The option "{choice}" option does not exist. Try again. **\n')
      choose_specialty()

# => main_menu

def main_menu():
  time = datetime.now()
  current_time = time.strftime('%H:%M')
  current_date = time.strftime('%x')
  print(f'** WELCOME {user_info["username"]}. Date: {current_date} - Time: {current_time}')

  options = ['1. Schedule an appointment', '0. Exit']
  for option in options:
    print(f'- {option}')

  choose_option = input('Enter a number: ')
  match choose_option:
    case '1':
      choose_specialty()
    case '0':
      print('Have a nice day!')
      exit()
    case _:
      print('That option does not exist. Try again.')
      main_menu()

def run_app():
  # login_menu()
  main_menu()

run_app()