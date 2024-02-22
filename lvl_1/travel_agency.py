"""
2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

Clue: You could consider the user's budget.
"""

user_info = {
  'budget': 0,
  'season': '',
  'interests': [],
  }

activities = [
  'skiing',
  'tour',
  'hiking',
  'extreme sports',
  'beach activities',
  'cultural and historical tour',
  'cultural and historical activities'
  ]

seasons = ['spring', 'summer', 'autumn', 'winter']

countries = {
  'Andorra': 'skiing',
  'Switzerland': 'tour',
  'Spain': ['hiking', 'extreme sports'],
  'Portugal': 'beach activities',
  'France': 'extreme sports',
  'Italy': 'cultural and historical tour',
  'Belgium': ['hiking', 'extreme sports'],
  'Austria': 'cultural and historical activities'
  }

prices = {
  'spring': 300,
  'summer': 400,
  'autumn': 200,
  'winter': 100
  }

countries_list = list(countries)
prices_list = list(prices.values())
spain_list = countries['Spain']
belgium_list = countries['Belgium']

"""
- Ask budget (DONE!)
- Ask preferences/interests (DONE!)
- Show what it is affordable to the user
"""

def budget_requirement(ask_budget):
  min_budget = 100
  ask_budget = int(input('How much budget do you have?\n=> $'))
  user_budget = ask_budget
  user_info['budget'] = user_budget

  if user_budget < min_budget:
    print('😢 Your budget is too low to take a trip.')
    exit()
  else:
    print(f'Your budget is: ${user_budget}')

  def request_season():
    i = 0

    print('\n** CHOOSE THE SEASON YOU WANT TO TRAVEL **\n')
    for season in seasons:
      i += 1
      print(f'{i}. {season.capitalize()}')

    ask_season = int(input('\nWhat season do you want to travel?\n=> '))
    match ask_season:
      case 1:
        if user_budget < prices_list[0]:
          print('\nYou cannot afford it.\n')
          request_season()
        else:
          print(f'You chose "{seasons[0].capitalize()}".')
          print(f'Available countries to travel in {seasons[0]}:')
          print(f'{countries_list[0]} - {countries_list[1]}')
          user_info['season'] = seasons[0]
      case 2:
        if user_budget < prices_list[1]:
          print('\nYou cannot afford it.\n')
          request_season()
        else:
          print(f'You chose "{seasons[1].capitalize()}".')
          print(f'Available countries to travel in {seasons[1]}:')
          print(f'{countries_list[4]} - {countries_list[5]}')
          user_info['season'] = seasons[1]
      case 3:
        if user_budget < prices_list[2]:
          print('\nYou cannot afford it.\n')
          request_season()
        else:
          print(f'You chose "{seasons[2].capitalize()}".')
          print(f'Available countries to travel in {seasons[2]}:')
          print(f'{countries_list[4]} - {countries_list[5]}')
          user_info['season'] = seasons[2]
      case 4:
        print(f'You chose "{seasons[3].capitalize()}".')
        print(f'Available countries to travel in {seasons[3]}:')
        print(f'{countries_list[6]} - {countries_list[7]}')
        user_info['season'] = seasons[3]
      case _:
        print('That option does not exist.')
        request_season()

  request_season()

  while True:
    confirm_season = input('\nDo you confirm? Y/N\n=> ')
    if confirm_season.upper() == 'Y':
      break
    elif confirm_season.upper() == 'N':
      request_season()
    else:
      print('That option does not exist.')
      confirm_season = input('\nDo you confirm? Y/N\n=> ')


def ask_activities():
  i = 0

  print('Activities that you can do in your trip:')
  for activity in activities:
    i += 1
    print(f'{i}. {activity.capitalize()}')

  if len(user_info['interests']) > 0:
    print('\nThese are the activities that you are interested:')
    for interesting_activity in user_info['interests']:
      print(f'- {interesting_activity.capitalize()}')

  try:
    traveler_preferences = int(input('\nEnter the number: '))
    match traveler_preferences:
      case 1:
        if activities[0] in user_info['interests']:
          print(f'\n** You already chose "{activities[0].capitalize()}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[0])
          print(f'\n"{activities[0].capitalize()}" added to your interests.\n')
      case 2:
        if activities[1] in user_info['interests']:
          print(f'\n** You already chose "{activities[1].capitalize()}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[1])
          print(f'\n"{activities[1].capitalize()}" added to your interests.\n')
      case 3:
        if activities[2] in user_info['interests']:
          print(f'\n** You already chose "{activities[2].capitalize()}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[2])
          print(f'\n"{activities[2].capitalize()}" added to your interests.\n')
      case 4:
        if activities[3] in user_info['interests']:
          print(f'\n** You already chose "{activities[3].capitalize()}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[3])
          print(f'\n"{activities[3].capitalize()}" added to your interests.\n')
      case 5:
        if activities[4] in user_info['interests']:
          print(f'\n** You already chose "{activities[4].capitalize()}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[4])
          print(f'\n"{activities[4].capitalize()}" added to your interests.\n')
      case 6:
        if activities[5] in user_info['interests']:
          print(f'\n** You already chose "{activities[5].capitalize()}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[5])
          print(f'\n"{activities[5].capitalize()}" added to your interests.\n')
      case 7:
        if activities[6] in user_info['interests']:
          print(f'\n** You already chose "{activities[6].capitalize()}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[6])
          print(f'\n"{activities[6].capitalize()}" added to your interests.\n')
      case _:
        print('\n** That activity does not exist. **\n')
        ask_activities()

  except ValueError:
    print('\n** Type numbers. Not letters. **\n')
    ask_activities()

  while True:
    try_again = input('Do you want to add another interest? Y/N: ')
    try_again = try_again.upper().strip()
    if try_again == 'Y':
      print()
      ask_activities()
    elif try_again == 'N':
      exit()
    else:
      print('That option does not exist.')

def run_app():
  budget_requirement(ask_budget=int())
  ask_activities()

run_app()