players = {
  '8': {
    'name': 'Bruno Fernandes',
    'goals': 5,
    'speed': 6,
    'assists': 9,
    'passing_accuracy': 10,
    'defensive_involvements': 3,
    },
  '11': {
    'name': 'Rasmus Hojlund',
    'goals': 12,
    'speed': 8,
    'assists': 2,
    'passing accuracy': 6,
    'defensive involvements': 2,
    },
  '5': {
    'name': 'Harry Maguire',
    'goals': 1,
    'speed': 5,
    'assists': 1,
    'passing accuracy': 7,
    'defensive involvements': 9,
    },
  '17': {
    'name': 'Alejandro Garnacho',
    'goals': 8,
    'speed': 7,
    'assists': 8,
    'passing accuracy': 6,
    'defensive involvements': 0,
    },
  '7': {
    'name': 'Mason Mount',
    'goals': 2,
    'speed': 6,
    'assists': 4,
    'passing accuracy': 8,
    'defensive involvements': 1,
    },
  }

def player_review():
  print('** PLAYER REVIEW **\n')

  check_player = input('Enter the player\'s jersey number: \n')
  while not check_player:
    print('You did not input the number. Try again.')
    check_player = input('Enter the player\'s jersey number: \n')
  while not check_player in players:
    print('That player does not exist. Try again.')
    check_player = input('Enter the player\'s jersey number to review: \n')
  player_stats = players[check_player]

  for stats_keys, stats in player_stats.items():
    print(f'{stats_keys.capitalize()} - {stats}')

  repeat = input('Do you want to review another player? Y/N')
  repeat = repeat.upper().strip()

  if repeat == 'Y':
    player_review()
  elif repeat == 'N':
    main_menu()
  else:
    print('Type Y for "Yes" or N for "No"')

  return True

def fastest_player():
  print('** COMPARE PLAYERS\' SPEED **\n')

  check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player:
    print('You did not input the number. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player in players:
    print('That player does not exist. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  speed_first_player = players[check_first_player]['speed']

  check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player:
    print('You did not input the number. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player in players:
    print('That player does not exist. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  speed_second_player = players[check_second_player]['speed']

  if speed_first_player > speed_second_player:
    print('\nThe fastest player is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'His speed is: {speed_first_player}.\n')
    print('The other player is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'His speed is: {speed_second_player}.')
  else:
    print('The fastest player is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'His speed is: {speed_second_player}.\n')
    print('The other player is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'His speed is: {speed_first_player}.')

  repeat = input('Do you want to compare the player\'s speed again? Y/N')
  repeat = repeat.upper().strip()

  if repeat == 'Y':
    player_review()
  elif repeat == 'N':
    main_menu()
  else:
    print('Type Y for "Yes" or N for "No"')

  return True

def top_goal_scorer():
  print('** COMPARE PLAYERS\' GOALS **\n')

  check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player:
    print('You did not input the number. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player in players:
    print('That player does not exist. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  goals_first_player = players[check_first_player]['goals']

  check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player:
    print('You did not input the number. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player in players:
    print('That player does not exist. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  goals_second_player = players[check_second_player]['goals']

  if goals_first_player > goals_second_player:
    print('\nThe top goal scorer is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'He has scored: {goals_first_player} goals.\n')
    print('The other scorer is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'He has scored: {goals_second_player} goals.')
  else:
    print('\nThe top goal scorer is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'He has scored: {goals_second_player} goals.\n')
    print('The other scorer is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'He has scored: {goals_first_player} goals.')

  repeat = input('Do you want to compare the player\'s goals again? Y/N')
  repeat = repeat.upper().strip()

  if repeat == 'Y':
    top_goal_scorer()
  elif repeat == 'N':
    main_menu()
  else:
    print('Type Y for "Yes" or N for "No"')

  return True

def most_assists():
  print('** COMPARE PLAYERS\' ASSISTS **\n')

  check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player:
    print('You did not input the number. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player in players:
    print('That player does not exist. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  assists_first_player = players[check_first_player]['assists']

  check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player:
    print('You did not input the number. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player in players:
    print('That player does not exist. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  assists_second_player = players[check_second_player]['assists']

  if assists_first_player > assists_second_player:
    print('\nThe player with the most points assists is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'He has done: {assists_first_player} assists.\n')
    print('The other player is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'He has done: {assists_second_player} assists.')
  else:
    print('\nThe player with the most points assists is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'He has done: {assists_second_player} assists.\n')
    print('The other player is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'He has done: {assists_first_player} assists.')

  repeat = input('Do you want to compare the player\'s assists again? Y/N')
  repeat = repeat.upper().strip()

  if repeat == 'Y':
    most_assists()
  elif repeat == 'N':
    main_menu()
  else:
    print('Type Y for "Yes" or N for "No"')

  return True

def passing_accuracy():
  print('** COMPARE PLAYERS\' PASSING ACCURACY **\n')

  check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player:
    print('You did not input the number. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player in players:
    print('That player does not exist. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  passes_first_player = players[check_first_player]['passing_accuracy']

  check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player:
    print('You did not input the number. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player in players:
    print('That player does not exist. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  passes_second_player = players[check_second_player]['passing_accuracy']

  if passes_first_player > passes_second_player:
    print('\nThe player with the highest passing accuracy is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'His passing accuracy is: {passes_first_player}\n')
    print('The other player is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'His passing accuracy is: {passes_second_player}')
  else:
    print('\nThe player with the highest passing accuracy is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'His passing accuracy is: {passes_second_player}\n')
    print('The other player is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'His passing accuracy is: {passes_first_player}')

  repeat = input('Do you want to compare the player\'s passes again? Y/N')
  repeat = repeat.upper().strip()

  if repeat == 'Y':
    passing_accuracy()
  elif repeat == 'N':
    main_menu()
  else:
    print('Type Y for "Yes" or N for "No"')

  return True

def defensive_involvements():
  print('** COMPARE PLAYERS\' DEFENSIVE INVOLVEMENTS **\n')

  check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player:
    print('You did not input the number. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  while not check_first_player in players:
    print('That player does not exist. Try again.')
    check_first_player = input('Enter the first player\'s jersey number: \n')
  defense_first_player = players[check_first_player]['defensive_involvements']

  check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player:
    print('You did not input the number. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  while not check_second_player in players:
    print('That player does not exist. Try again.')
    check_second_player = input('Enter the second player\'s jersey number: \n')
  defense_second_player = players[check_second_player]['defensive_involvements']

  if defense_first_player > defense_second_player:
    print('\nThe player with the most defensive involvements is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'His defensive involvements points are: {defense_first_player}\n')
    print('The other player is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'His defensive involvements points are: {defense_second_player}')
  else:
    print('\nThe player with the most defensive involvements is:')
    print(f'{players[check_second_player]["name"]}')
    print(f'His defensive involvements points are: {defense_second_player}\n')
    print('The other player is:')
    print(f'{players[check_first_player]["name"]}')
    print(f'His defensive involvements points are: {defense_first_player}')

  repeat = input('Do you want to compare the player\'s defensive again? Y/N')
  repeat = repeat.upper().strip()

  if repeat == 'Y':
    defensive_involvements()
  elif repeat == 'N':
    main_menu()
  else:
    print('Type Y for "Yes" or N for "No"')

  return True

def compare_players():

  options = ['Speed', 'Goals', 'Assists', 'Passes', 'Defense', 'Back']

  for option in options:
    print(f'- {option}')

  choose_option = input('Type an option: ')
  choose_option = choose_option.lower().strip()

  while not choose_option:
    print('You did not input any option. Try again.')
    main_menu()

  match choose_option:
    case 'speed':
      fastest_player()
      print()
      main_menu()
    case 'goals':
      top_goal_scorer()
      print()
      main_menu()
    case 'assists':
      most_assists()
      print()
      main_menu()
    case 'assists':
      passing_accuracy()
      print()
      main_menu()
    case 'passes':
      passing_accuracy()
      print()
      main_menu()
    case 'defense':
      defensive_involvements()
      print()
      main_menu()
    case 'back':
      main_menu()
    case _:
      print('That option does not exist. Try again.')
      main_menu()

def main_menu():

  options = ['Review', 'Compare', 'Exit']

  print('** MAN UTD MANAGEMENT **\n')

  for option in options:
      print(f'- {option}')

  choose_option = input('Type an option: ')
  choose_option = choose_option.lower().strip()

  while not choose_option:
    print('You did not input any option. Try again.')
    main_menu()

  match choose_option:
    case 'review':
      player_review()
      print()
      main_menu()
    case 'compare':
      compare_players()
      print()
      main_menu()
    case 'exit':
      print('Forged in industry, striving for glory.')
      exit()
    case _:
      print('That option does not exist. Try again.')
      main_menu()

def run_app():
  main_menu()

run_app()