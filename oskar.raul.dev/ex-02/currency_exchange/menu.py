import re


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
