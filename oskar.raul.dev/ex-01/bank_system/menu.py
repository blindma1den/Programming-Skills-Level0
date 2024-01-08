import re

LOGIN_REGEX = '[a-z][a-z0-9]{2,}'
ACCOUNT_REGEX = '\\d{4,}'

# show menu with options to be selecting by 
# input (1 ... N)
def menu_options(options=[], title="Choose an option"):
  if len(options) < 1:
    print('No menu options!')
    return 0
  # Print menu with options
  print('--' + title.upper() + '--')
  n = len(options)
  for i in range(n):
    # print each line of menu
    print('(%2d) - %s' % (i + 1, options[i]))
  # Loop to select option
  while True:
    try:
      option = int(input('Select your option (1 - %d): ' % (n)).strip())
      if not (option >=1 and option <= n):
        raise Exception('invalid range')
      return option
    except Exception:
      print('Invalid input, you must enter a number between 1 and %d' % (n))

# Read a login not empty value beginning by letter a-z
# must be lower case
def read_login(message = 'input login'):
  # loop to accept a valid login
  while True:
    login = input(message.upper().strip() + ": ").strip()
    if not re.fullmatch(LOGIN_REGEX, login):
       print('Invalid input, login must be lower case and at least 3 chars long')
    else:
      return login

# Read a password not empty value
def read_password(message = 'input password'):
  # loop to accept a valid login
  while True:
    password = input(message.upper().strip() + ": ").strip()
    if password.strip() == '':
       print('Invalid input, password must be not empty')
    else:
      return password

# Read account number 
# must be only digits at least 4 digits long
def read_account(message = 'input account number'):
  # loop to accept a valid login
  while True:
    account = input(message.upper().strip() + ": ").strip()
    if not re.fullmatch(ACCOUNT_REGEX, account):
       print('Invalid input, account must have only digits and at least 4 chars long')
    else:
      return account

# Read amount
# must be only positive non zero amount
def read_amount(message = 'input amount'):
  # loop to accept a valid amount
  while True:
    try:
      amount = float(input(message.upper().strip() + ": ").strip())
      if amount <= 0:
        print('Invalid input, amount must be greater than zero')
      else:
        return amount
    except Exception:
      print('Invalid input, amount must be a number greater than zero')
