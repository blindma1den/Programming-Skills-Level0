user_info = {
  'income': 0
  }

categories = {
  'medical expenses': 0,
  'household expenses': 0,
  'leisure': 0,
  'savings': 0,
  'education': 0
  }

def income():
  enter_income = float(input('Enter your income: '))
  user_info['income'] = enter_income

def show_categories():
  for category, amount in categories.items():
    print(f'{category.capitalize()}: ${round(amount, 2)}')

def main_menu():

  total = sum(categories.values())
  options = [
    '1. Medical expenses',
    '2. Household expenses',
    '3. Leisure expenses',
    '4. Educational expenses',
    '5. Savings',
    '6. Total',
    '0. Exit'
    ]

  print('')
  for option in options :
    print(f'{option}')
  print('')

  choose_option = input('\nEnter your option with a number: ')

  match choose_option:
    case '1':
      medical_expenses = float(input('\nEnter your medical expenses: '))
      categories['medical expenses'] += medical_expenses
      main_menu()
    case '2':
      household_expenses = float(input('\nEnter your household expenses: '))
      categories['household expenses'] += household_expenses
      main_menu()
    case '3':
      leisure_expenses = float(input('\nEnter your leisure expenses: '))
      categories['leisure'] += leisure_expenses
      main_menu()
    case '4':
      educational_expenses = float(input('\nEnter your educational expenses: '))
      categories['education'] += educational_expenses
      main_menu()
    case '5':
      savings = float(input('\nEnter your savings: '))
      categories['savings'] += savings
      main_menu()
    case '6':
      print('')
      show_categories()
      print(f'Your total expenses are: ${total}')
      if total > user_info['income']:
        print('You have to be careful because you are spending more than what you earn.')
      elif total < user_info['income']:
        print('Congrats! You know how to manage your economy.')
      elif total == user_info['income']:
        print(f'We suggest you that you reduce your expenses because you have spent ${max(categories.values())}')
    case _:
      print('That option does not exist. Try again.\n')
      main_menu()

def run_app():
  print('** Welcome to MO-MONEY **\n')
  income()
  main_menu()

run_app()