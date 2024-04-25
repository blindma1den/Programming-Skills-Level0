import random

def exchange_to_dollars(exchange_input:str, exchange_output:str, exchange_size:float, exchange_dictionary:dict)-> float:
    
    rate = round(random.uniform(0.5, 2.5),2) # Comisión por cambio de moneda
    exchange_input_to_dollars = exchange_dictionary[exchange_input]
    exchange_output_to_dollars = exchange_dictionary[exchange_output]

    exchange = round((exchange_size * exchange_input_to_dollars) / exchange_output_to_dollars, 2)
    exchange_rate = round((exchange * rate/100), 2)


    return exchange, rate, exchange_rate