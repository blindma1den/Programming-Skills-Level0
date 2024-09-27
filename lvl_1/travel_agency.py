
user_info = {
  'budget': 0,
  'season': '',
  'interests': [],
  }

countries = {
  'Andorra': 'Skiing',
  'Switzerland': 'Tour of the Swiss Alps',
  'Spain': ['Hiking', 'Extreme sports'],
  'Portugal': 'Beach activities',
  'France': 'Extreme sports',
  'Italy': 'Cultural and historical tour',
  'Belgium': ['Hiking', 'Extreme sports'],
  'Austria': 'Cultural and historical activities'
  }

seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

activities = [
  'Skiing',
  'Tour of the Swiss Alps',
  'Hiking',
  'Extreme sports',
  'Beach activities',
  'Cultural and historical tour',
  'Cultural and historical activities'
  ]

prices = {
  'Spring': 300,
  'Summer': 400,
  'Autumn': 200,
  'Winter': 100
  }

countries_list = list(countries)
spain_list = countries['Spain']
belgium_list = countries['Belgium']
prices_list = list(prices.values())

# This function asks how much money the users can spend and what season they want to travel
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
      print(f'{i}. {season}')

    ask_season = int(input('\nWhat season do you want to travel?\n=> '))
    match ask_season:
      case 1:
        if user_budget < prices_list[0]:
          print('\nYou cannot afford it.')
          request_season()
        else:
          print(f'You chose "{seasons[0]}".')
          print(f'Available countries to travel in {seasons[0]}:')
          print(f'{countries_list[4]} - {countries_list[5]}')
          user_info['season'] = seasons[0]
      case 2:
        if user_budget < prices_list[1]:
          print('\nYou cannot afford it.')
          request_season()
        else:
          print(f'You chose "{seasons[1]}".')
          print(f'Available countries to travel in {seasons[1]}:')
          print(f'{countries_list[2]} - {countries_list[3 ]}')
          user_info['season'] = seasons[1]
      case 3:
        if user_budget < prices_list[2]:
          print('\nYou cannot afford it.')
          request_season()
        else:
          print(f'You chose "{seasons[2]}".')
          print(f'Available countries to travel in {seasons[2]}:')
          print(f'{countries_list[6]} - {countries_list[7]}')
          user_info['season'] = seasons[2]
      case 4:
        print(f'You chose "{seasons[3]}".')
        print(f'Available countries to travel in {seasons[3]}:')
        print(f'{countries_list[0]} - {countries_list[1]}')
        user_info['season'] = seasons[3]
      case _:
        print('That option does not exist.')
        request_season()

  request_season()

  while True:
    confirm_season = input('\nDo you confirm? Y/N\n=> ')
    if confirm_season.upper().strip() == 'Y':
      break
    elif confirm_season.upper().strip() == 'N':
      request_season()
    else:
      print('That option does not exist.')
      confirm_season = input('\nDo you confirm? Y/N\n=> ')

# This function prints where the users can travel with their budget and interests
def show_budgets():

  def show_winter_budget():
      print(f'** {seasons[3].upper()} **')
      print(f'Countries: {countries_list[0]} - {countries_list[1]}')
      print(f'Activities:')
      print(f'- {activities[0]} in {countries_list[0]}')
      print(f'- {activities[1]} in {countries_list[1]}')
      print(f'Budget: ${prices_list[3]}')

  def show_autumn_budget():
      print(f'** {seasons[2].upper()} **')
      print(f'Countries: {countries_list[6]} - {countries_list[7]}')
      print(f'Activities:')
      print(f'- {" and ".join(belgium_list)} in {countries_list[6]}')
      print(f'- {activities[6]} in {countries_list[7]}')
      print(f'Budget: ${prices_list[2]}')

  def show_spring_budget():
      print(f'** {seasons[0].upper()} **')
      print(f'Countries: {countries_list[4]} - {countries_list[5]}')
      print(f'Activities:')
      print(f'- {activities[3]} in {countries_list[4]}')
      print(f'- {activities[5]} in {countries_list[5]}')
      print(f'Budget: ${prices_list[0]}')

  def show_summer_budget():
      print(f'** {seasons[1].upper()} **')
      print(f'Countries: {countries_list[2]} - {countries_list[3]}')
      print(f'Activities:')
      print(f'- {" and ".join(spain_list)} in {countries_list[2]}')
      print(f'- {activities[4]} in {countries_list[3]}')
      print(f'Budget: ${prices_list[1]}')

  print('Based on the season you want to travel:\n')
  if user_info['budget'] >= prices_list[3] and user_info['budget'] < prices_list[2]:
    show_winter_budget()
  elif user_info['budget'] >= prices_list[2] and user_info['budget'] < prices_list[0]:
    show_winter_budget()
    print()
    show_autumn_budget()
  elif user_info['budget'] >= prices_list[0] and user_info['budget'] < prices_list[1]:
    show_winter_budget()
    print()
    show_autumn_budget()
    print()
    show_spring_budget()
  elif user_info['budget'] >= prices_list[1]:
    show_winter_budget()
    print()
    show_autumn_budget()
    print()
    show_spring_budget()
    print()
    show_summer_budget()

# This function asks which interests the users have, so they can do that in their travel
def ask_activities():
  i = 0

  print('\nActivities that you can do in your trip:')
  for activity in activities:
    i += 1
    print(f'{i}. {activity}')

  if len(user_info['interests']) > 0:
    print('\nThese are the activities that you are interested:')
    for interesting_activity in user_info['interests']:
      print(f'- {interesting_activity}')

  try:
    traveler_preferences = int(input('\nEnter the number: '))
    match traveler_preferences:
      case 1:
        if activities[0] in user_info['interests']:
          print(f'\n** You already chose "{activities[0]}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[0])
          print(f'\n"{activities[0]}" added to your interests.\n')
      case 2:
        if activities[1] in user_info['interests']:
          print(f'\n** You already chose "{activities[1]}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[1])
          print(f'\n"{activities[1]}" added to your interests.\n')
      case 3:
        if activities[2] in user_info['interests']:
          print(f'\n** You already chose "{activities[2]}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[2])
          print(f'\n"{activities[2]}" added to your interests.\n')
      case 4:
        if activities[3] in user_info['interests']:
          print(f'\n** You already chose "{activities[3]}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[3])
          print(f'\n"{activities[3]}" added to your interests.\n')
      case 5:
        if activities[4] in user_info['interests']:
          print(f'\n** You already chose "{activities[4]}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[4])
          print(f'\n"{activities[4]}" added to your interests.\n')
      case 6:
        if activities[5] in user_info['interests']:
          print(f'\n** You already chose "{activities[5]}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[5])
          print(f'\n"{activities[5]}" added to your interests.\n')
      case 7:
        if activities[6] in user_info['interests']:
          print(f'\n** You already chose "{activities[6]}". Try again. **\n')
          ask_activities()
        else:
          user_info['interests'].append(activities[6])
          print(f'\n"{activities[6]}" added to your interests.\n')
      case _:
        print('\n** That activity does not exist. **\n')
        ask_activities()

  except ValueError:
    print('\n** Type numbers. Not letters. **\n')
    ask_activities()

  while True:
    try_again = input('Do you want to add another interest? Y/N: ')
    if try_again.upper().strip() == 'Y':
      print()
      ask_activities()
    elif try_again.upper().strip() == 'N':
      show_budgets()
      exit()
    else:
      print('That option does not exist.')

def run_app():
  budget_requirement(ask_budget=int())
  ask_activities()

run_app()