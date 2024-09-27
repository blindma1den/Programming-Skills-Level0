import random, time, getpass

account_info = {
  'username': '',
  'password': '',
  'balance': 2000,
}
suggested_accounts = []


# => LOGIN

def validate_username(username):
  empty_field = 0
  min_username_length = 6
  max_username_length = 10

  if len(username) == empty_field:
    print(f'You did not input any character.')
    return False
  elif len(username) < min_username_length:
    print(f'The minimum character allowed is: {min_username_length}')
    return False
  elif len(username) > max_username_length:
    print(f'The minimum character allowed is: {min_username_length}')
    return False

  print('CHECKED!\n')

  return True

def validate_password(password):
    empty_field = 0
    min_password_length = 8
    max_password_length = 14

    if len(password) == empty_field:
        print(f'You did not input any character.')
        return False
    elif len(password) < min_password_length:
        print(f'The minimum character allowed is: {min_password_length}')
        return False
    elif len(password) > max_password_length:
        print(f'The minimum character allowed is: {min_password_length}')
        return False

    print('CHECKED!\n')

    return True

def login():
    username = input('Enter your username: ')
    while not validate_username(username):
        username = input('Please, try again. Enter your username: ')
    account_info['username'] += username

    password = getpass.getpass('Enter your password: ')
    while not validate_password(password):
        password = getpass.getpass('Please, try again. Enter your password: ')
    account_info['password'] += password

    return username, password


# => SECURITY ACCESS

def generate_code():
    code = random.randint(100000, 999999)
    return code

def show_verification_code(code):
    verification_code = f'To get access, enter the code we are showing you: {code}'
    print(verification_code)
    return True

def verify_code(code):
    enter_code = int(input('ENTER THE CODE\n=> '))
    time_starts = time.time()
    time_ends = time.time()
    final_time = time_ends - time_starts
    limit_time = 15

    if final_time > limit_time and enter_code == code:
        print('You ran out of time!')
        exit()
    elif enter_code == code:
        return enter_code

def security_access():
    attempts = 0
    attempts_limit = 3
    code = generate_code()

    show_verification_code(code)

    while attempts < attempts_limit:
        if verify_code(code):
            print('\n** ACCESS GRANTED **\n')
            break
        else:
            print('** ACCESS DENIED **\n')
            attempts += 1

    if attempts == attempts_limit:
        print('YOU HAVE REACHED THE LIMIT OF ATTEMPTS. TRY LATER.')
        exit()

    return True


# => MAIN MENU

def balance():
    print(f'Your current balance is: ${account_info["balance"]}')
    return True

def deposit():
    quantity = int(input('\nHow much money do you want to deposit?\n=> '))
    account_info['balance'] += quantity
    print(f'YOU HAVE DEPOSITED: ${quantity}. Your current balance is: ${account_info["balance"]}')
    return True

def withdraw():
    quantity = int(input('\nHow much money do you want to withdraw?\n=> '))
    account_info['balance'] -= quantity
    print(f'YOU HAVE WITHDRAWN: ${quantity}. Your current balance is: ${account_info["balance"]}')
    return True

def transfer():
    if not suggested_accounts:
      print('\nYou have not saved any account to transfer.')
    else:
      str_suggested_accounts = ', '.join(map(str, suggested_accounts))
      print(f'\nSuggested accounts to transfer: {str_suggested_accounts}')

    contact = input('Enter the username you want to transfer: ')
    quantity = int(input(f'How much money do you want to transfer to "{contact}"?\n=> '))
    account_info['balance'] -= quantity
    print(f'\nYOU TRANSFERED ${quantity} TO "{contact}". Your current balance is: ${account_info["balance"]}')

    if not contact in suggested_accounts:
      save_contact = input('Do you want to save this contact? Y/N\n=> ')
      save_contact = save_contact.upper().strip()
      if save_contact == 'Y':
        suggested_accounts.append(contact)
        print(f'{contact} has been saved.')
      elif save_contact == 'N' or save_contact == 'n':
        main_menu()
    else:
      main_menu()

    return True

def info():
  options = ['username', 'password']

  print(f'\nYour username is: {(account_info["username"])}\nYour password is: {"*" * len(account_info["password"])}')

  change_info = input('\nDo you want to change your username or password? Y/N\n=> ')
  change_info = change_info.upper().strip()

  if change_info == 'Y':
    select_option = input('Type the option (username/password): ')
    if select_option == options[0]:
      new_username = input('Enter your new username: ')
      check_new_username = input('Enter your new username again: ')
      if new_username == check_new_username:
        account_info['username'] = new_username
        print('You changed your username successfuly\n')
        return True
      elif new_username != check_new_username:
        while new_username != check_new_username:
          print('Both usernames did not match\n')
          new_username = input('Enter your new username: ')
          check_new_username = input('Enter your new username again: ')
          if new_username == check_new_username:
            account_info['username'] = new_username
            print('You changed your username successfuly\n')
        return True
    elif select_option == options[1]:
      new_password = getpass.getpass('Enter your new password: ')
      check_new_password = getpass.getpass('Enter your new password again: ')
      if new_password == check_new_password:
        account_info['password'] = new_password
        print('You changed your password successfuly')
        return True
      elif new_password != check_new_password:
        while new_password != check_new_password:
          print('Both passwords did not match\n')
          new_password = getpass.getpass('Enter your new password: ')
          check_new_password = getpass.getpass('Enter your new password again: ')
          if new_password == check_new_password:
            account_info['password'] = new_password
            print('You changed your password successfuly\n')
        return True
  elif change_info == 'N':
        main_menu()

  return True


def main_menu():
    welcome_message = f'Hello {account_info["username"]}!'
    print(welcome_message.upper())
    type_option = (input('\nType an option:\n- Deposit\n- Withdraw\n- Transfer\n- Balance\n- Info\n- Exit\n=> '))
    type_option = type_option.lower().strip()

    while not type_option:
        print('TYPE AN OPTION!\n')
        type_option = (input('Type an option:\n- Deposit\n- Withdraw\n- Transfer\n- Balance\n- Info\n- Exit\n=> '))
        type_option = type_option.lower().strip()

    match type_option:
      case 'deposit':
        deposit()
        main_menu()
      case 'withdraw':
        withdraw()
        main_menu()
      case 'transfer':
        transfer()
        main_menu()
      case 'balance':
        balance()
        main_menu()
      case 'info':
        info()
      case 'exit':
        print('SEE YOU LATER AND HAVE A NICE DAY! :)')
        exit()
      case _:
        print('That option does not exist. Try again.\n')
        main_menu()

    return True

def run_app():
  print('* * * WELCOME TO PIGGYBANK * * *')
  login()
  security_access()
  main_menu()

run_app()