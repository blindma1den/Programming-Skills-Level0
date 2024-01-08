# Dictionary that implements customers database
# the dictionary is indexed by user login
# Each entry of customers' database is a Dictionary with following keys
# login: user login
# name: user name
# password: user password (plain text by know ;) )
# login_attemps: total failed login attemps
# locked: boolean value for account is locked
# accounts: list of accounts numbers owned by user
CUSTOMERS_DICT = {
  "johndoe": {
      'login': 'johndoe',
      'name': 'John Doe',
      'password': '123',
      'login_attemps': 0,
      'locked': False,
      'accounts': ['000123'],
  },
  "janedoe": {
      'login': 'janedoe',
      'name': 'Jane Doe',
      'password': '999',
      'login_attemps': 0,
      'locked': False,
      'accounts': ['000999', '111555'],
  },
  "petterblogg": {
      'login': 'petterblogg',
      'name': 'Peter Blogg',
      'password': 'qwerty',
      'login_attemps': 0,
      'locked': False,
      'accounts': ['222666', '111693'],
  },
  "dylansmith": {
      'login': 'dylansmith',
      'name': 'Dylan Smith',
      'password': 'qwerty',
      'login_attemps': 0,
      'locked': False,
      'accounts': ['000456'],
  },
  "annaodonnel": {
      'login': 'annaodonnel',
      'name': 'Anna O\'Donnel',
      'password': 'qwerty',
      'login_attemps': 0,
      'locked': False,
      'accounts': ['777444', '333444'],
  },
  "alicemendez": {
      'login': 'alicemendez',
      'name': 'Alice Méndez',
      'password': '123',
      'login_attemps': 0,
      'locked': False,
      'accounts': [],
  },
}

# Dictionary that implements accounts database
# the dictionary is indexed by account number (only digits)
# Each entry of accounts' database is a Dictionary with following keys
# number: account number
# owner: login of account's owner
# type: 'savings' or 'check'
# balance: number with available balance
ACCOUNTS_DICT = {
  '000123': {
    'number': '000123',
    'owner': 'johndoe',
    'type': 'savings',
    'balance': 2000.00
  },
  '000999': {
    'number': '000999',
    'owner': 'janedoe',
    'type': 'savings',
    'balance': 2000.00
  },
  '111555': {
    'number': '111555',
    'owner': 'janedoe',
    'type': 'checks',
    'balance': 2000.00
  },
  '222666': {
    'number': '222666',
    'owner': 'petterblogg',
    'type': 'savings',
    'balance': 2000.00
  },
  '111693': {
    'number': '111693',
    'owner': 'petterblogg',
    'type': 'checks',
    'balance': 2000.00
  },
  '000456': {
    'number': '000456',
    'owner': 'dylansmith',
    'type': 'savings',
    'balance': 2000.00
  },
  '777444': {
    'number': '777444',
    'owner': 'annaodonnel',
    'type': 'savings',
    'balance': 2000.00
  },
  '333444': {
    'number': '333444',
    'owner': 'annaodonnel',
    'type': 'checks',
    'balance': 2000.00
  },
}

# Variable for simulation session with logged user
# if user is nil there are not session 
LOGGED_IN_USER = None
