# operations for accounts from database
import bank_system.data as d

# load account from database
def get_account(account):
  if not account_exists(account):
    return None
  else:
    return d.ACCOUNTS_DICT[account]

# verify if account number exists in database
def account_exists(account):
  return account in d.ACCOUNTS_DICT

# verify if account is owned to user by login
def account_owned_by_user(login, account):
  return account in d.CUSTOMERS_DICT[login]['accounts']

# Verify if some account has enough balance to a withdrawal
def enough_balance_in_account(account, amount):
  current_balance = d.ACCOUNTS_DICT[account]['balance']
  return current_balance >= amount

# Perform a deposit into an account
def deposit_in_account(account, amount):
  current_balance = d.ACCOUNTS_DICT[account]['balance']
  d.ACCOUNTS_DICT[account]['balance'] = current_balance + amount

# Perform a withdrawal from account given the account 
# has enough balance
def withdrawal_from_account(account, amount):
  current_balance = d.ACCOUNTS_DICT[account]['balance']
  d.ACCOUNTS_DICT[account]['balance'] = current_balance - amount

# Perform a transfer from account_from to account_to given that account_from
# has enough balance
def transfer_between_accounts(account_from, account_to, amount):
  withdrawal_from_account(account_from, amount)
  deposit_in_account(account_to, amount)
