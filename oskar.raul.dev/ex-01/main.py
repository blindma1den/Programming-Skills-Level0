import sys
import bank_system.menu as menu
import bank_system.accounts_operations as acc
import bank_system.login_operations as login

# Infinite loop for main program
while True:
  print("BANK SYSTEM")
  print("-----------")
  # verify if session is started or not
  if not login.is_init_session():
    # no session, login process
    option = menu.menu_options(['Log In', 'Exit Program'], 'You must login into the system')
    if option == 1:
      #ask for login
      user_login = menu.read_login('Login') 
      password = menu.read_password('Password')
      #verify if user exists
      if not login.user_exists(user_login):
        print('Error: Incorrect user credentials')
      elif login.user_is_locked(user_login):
        print('Error: Your user ' + user_login + ' is locked. Call to your Bank Agent')
      elif not login.verify_credentials(user_login, password):
        login.increment_login_attemps(user_login)
        print('Error: Incorrect user credentials')
      else:
        login.init_session(user_login)
        print('')
        print('Welcome %s. Access for services are granted.' % (login.session_user()['name']) )
    else:
      # finish program
      print('Bye, thank you for using our services')
      exit()
  else:
    # Main menu for logged user
    user = login.session_user()
    # verify if the user has at least one account
    if len(user['accounts']) == 0:
      print('You don\'t have any account registered! Call to your Bank Agent')
      continue
    option =  menu.menu_options([
        'View your accounts', 
        'Deposit',
        'Withdrawal', 
        'Transfer',
        'Log Out',
        'Exit Program'], 'You must login into the system')
    if option == 1:
      # View account information
      # Select account
      option = menu.menu_options(user['accounts'], 'Select your account to view information')
      account = acc.get_account(user['accounts'][option - 1])
      print('------------------------')
      print('YOUR ACCOUNT INFORMATION')
      print('------------------------')
      print('- Number: %s' % (account['number']))
      print('- Owner: %s' % (user['name']))
      print('- Type: %s' % (account['type']))
      print('- Balance: $%.2f' % (account['balance']))
    elif option == 2:
      #deposit
      print('------------------------')
      print('        DEPOSIT         ')
      print('------------------------')
      account_number = menu.read_account("Select account to deposit")
      # verify if account exists
      if not acc.account_exists(account_number):
        print("Error: account %s does not exist" % (account_number))
        continue
      account = acc.get_account(account_number)
      amount = menu.read_amount("Amount to deposit")
      acc.deposit_in_account(account_number, amount)
      print("Deposited $%.2f into account %s, owner %s" % (amount, account['number'], login.get_user(account['owner'])['name']))
    elif option == 3:
      #withdrawal
      print('------------------------')
      print('      WITHDRAWAL        ')
      print('------------------------')
      option = menu.menu_options(user['accounts'], 'Select your account to withdrawal')
      account = acc.get_account(user['accounts'][option - 1])
      amount = menu.read_amount("Amount to withdraw")
      # validate balance
      if (account['balance'] < amount):
        print('Can\'t complete withdrawal. Insufficient balance')
        continue
      acc.withdrawal_from_account(account['number'], amount)
      print("Withdrawed $%.2f from account %s, your balance is now %.2f" % (amount, account['number'], account['balance']))
    elif option == 4:
      #transfer
      print('------------------------')
      print('        TRANSFER        ')
      print('------------------------')
      option = menu.menu_options(user['accounts'], 'Select your origin account for transfer')
      account_from = acc.get_account(user['accounts'][option - 1])
      account_to_number = menu.read_account("Select desitnation account for transfer")
      # verify if account exists
      if not acc.account_exists(account_to_number):
        print("Error: account %s does not exist" % (account_to_number))
        continue
      account_to = acc.get_account(account_to_number)
      if account_from['number'] == account_to['number']:
        print('Error: Origin account can\'t be the same that destination account')
        continue
      amount = menu.read_amount("Amount to transfer")
      if (account_from['balance'] < amount):
        print('Can\'t complete withdrawal. Insufficient balance')
        continue
      acc.transfer_between_accounts(account_from['number'], account_to['number'], amount)
      print("Transfered $%.2f from account %s to account %s owned by %s, your balance is now %.2f" % (amount, account_from['number'], account_to['number'], login.get_user(account_to['owner'])['name'],account_from['balance']))
    elif option == 5:
      print("Session finised for user %s"  % (login.session_user()['name']))
      login.finish_session()
    else:
      # finish program
      print('Bye, thank you for using our services')
      exit()
