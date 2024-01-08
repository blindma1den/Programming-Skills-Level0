import sys
import currency_exchange.exchange_db as exchange
import currency_exchange.menu as menu

exchange.load_csv_db()
while True:
  print('----------------------------')
  print('Currency Exchange Calculator')
  print('----------------------------')
  option = menu.menu_options(['Calculate Exchange', 'Exit Program'], 'Select an option')
  if option == 1:
    currencies = exchange.available_currencies()
    #select currency from
    cur_from = currencies[menu.menu_options(exchange.available_currencies(), 'Select base currency') - 1]
    
    #select currency to
    filtered_cur_list = list(filter(lambda c: c != cur_from, exchange.available_currencies()))
    cur_to = currencies[menu.menu_options(filtered_cur_list, 'Select currency to convert') - 1]
    
    # input amount
    amount = menu.read_amount('Write the amount in %s' % (cur_from))
    exchanged_amount = amount * exchange.csv_exchange_table()[cur_from][cur_to]
    
    # print result
    print("%s %f is equivalent to %s %f" % (cur_from, amount, cur_to, exchanged_amount))
    print('')
  else:
    print("Bye...")
    exit()
