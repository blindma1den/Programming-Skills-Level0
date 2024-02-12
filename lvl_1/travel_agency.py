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

activities = ['skiing', 'tour', 'hiking', 'extreme sports', 'activities',]

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

spain_list = countries['Spain']
belgium_list = countries['Belgium']

def test():
  traveler_preferences = input('Enter: ')
  if traveler_preferences in countries.values():
    print('NICE!')
  elif traveler_preferences in spain_list or traveler_preferences in belgium_list:
    print('NICE! x2')


def run_app():
  print('Running!')
  test()

run_app()