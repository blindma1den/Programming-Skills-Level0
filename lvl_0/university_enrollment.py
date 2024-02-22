import getpass

user_info = {
   'username': '',
   'password': '',
   'first_name': '',
   'last_name': '',
   'full_name': '',
   'chosen_program': '',
   'chosen_campus': '',
   }

university_name = 'south harmon institute of technology'

available_programs = ['Computer Science', 'Medicine', 'Marketing', 'Arts']

program_slots = {
  'computer science': ['student', 'student', 'student', 'student'],
  'medicine': ['student', 'student', 'student', 'student', 'student'],
  'marketing': ['student', 'student'],
  'arts': ['student', 'student', 'student']
  }

cities = {
  'manchester': ['student', 'student'],
  'liverpool': ['student'],
  'london': []
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
    else:
      user_info['password'] = password_input
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

def personal_info():
  first_name = input('Enter your first name: ')
  while not first_name:
    first_name = input('\nEnter your first name: ')
  last_name = input('\nEnter your last name: ')
  while not last_name:
    last_name = input('\nEnter your last name: ')
  user_info['first_name'] = first_name.capitalize().strip()
  user_info['last_name'] = last_name.capitalize().strip()
  user_info['full_name'] = f'{first_name.capitalize().strip()} {last_name.capitalize().strip()}'

def program_enrollment():

  choose_program = input('Choose the program that you want to enroll: ')
  choose_program = choose_program.lower().strip()

  while not choose_program:
    print('You did not input any program. Try again.')
    choose_program = input('Choose the program that you want to enroll: ')
    choose_program = choose_program.lower().strip()

  match choose_program:
    case 'computer science':
      #program_slots[choose_program].append(user_info['full_name'])
      user_info['chosen_program'] = choose_program
    case 'medicine':
      #program_slots[choose_program].append(user_info['full_name'])
      user_info['chosen_program'] = choose_program
    case 'marketing':
      #program_slots[choose_program].append(user_info['full_name'])
      user_info['chosen_program'] = choose_program
    case 'arts':
      #program_slots[choose_program].append(user_info['full_name'])
      user_info['chosen_program'] = choose_program
    case _:
      print('The program you input does not exist. Try again.')
      program_enrollment()

  while len(program_slots[choose_program]) >= 5:
    print('There is no space for this program.')
    choose_program = input('Choose the program that you want to enroll: ')
    choose_program = choose_program.lower().strip()





def campus_enrollment():

  select_campus = input('Select the campus where you want to study: ')
  select_campus = select_campus.lower().strip()

  while not select_campus:
    print('You did not input the campus where you want to study.')
    select_campus = input('Select the campus where you want to study: ')


  match select_campus:
    case 'manchester':
      user_info['chosen_campus'] = select_campus
    case 'liverpool':
      user_info['chosen_campus'] = select_campus
    case 'london':
      user_info['chosen_campus'] = select_campus
    case _:
      print('That campus does not exist. Try again.')
      campus_enrollment()

  while len(cities[select_campus]) == 3 or len(cities[select_campus]) == 1:
    print('There is no space for this campus')
    print(f'{cities[select_campus]}')
    select_campus = input('Select the campus where you want to study: ')
  else:
    cities[select_campus].append(user_info['full_name'])


  print('\nENROLLMENT DETAILS:')
  print(f'{user_info["full_name"]}')
  print(f'{user_info["chosen_program"].capitalize()} - {user_info["chosen_campus"].capitalize()}')
  print(f'Good luck {user_info["first_name"]}! We will see you next month.')

def main_menu():
  print('These are the available programs for you:')
  print(f"{' - '.join(map(str, available_programs))}\n")


def run_app():
  print(f'WELCOME TO {university_name.upper()}\n')
  #login()
  main_menu()
  personal_info()
  program_enrollment()
  campus_enrollment()

run_app()