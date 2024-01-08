# operations for login proccess
import bank_system.data as d
MAX_LOGIN_ATTEMPS = 3

# load user from database
def get_user(login):
  if not user_exists(login):
    return None
  else:
    return d.CUSTOMERS_DICT[login]

# verify if user exists in database
def user_exists(login):
  return login in d.CUSTOMERS_DICT

# verify if user is locked
def user_is_locked(login):
  user = get_user(login)
  if user is None:
    return True
  else:
    return user['locked']

# verify if login/password credentials are valid
def verify_credentials(login, password):
  return user_exists(login) and get_user(login)['password'] == password

# increments invalid login attemps
def increment_login_attemps(login):
  user = get_user(login)
  user['login_attemps'] = user['login_attemps'] + 1
  # if there are mor than max attemps user is locked
  if user['login_attemps'] >= MAX_LOGIN_ATTEMPS:
    lock_user(login)

# blocks user
def lock_user(login):
  get_user(login)['locked'] = True
  
# init session
def init_session(login):
  d.LOGGED_IN_USER = get_user(login)

# finish session
def finish_session():
  d.LOGGED_IN_USER = None

# Verify if session is started
def is_init_session():
  return not d.LOGGED_IN_USER is None

# returns session user
def session_user():
  return d.LOGGED_IN_USER
