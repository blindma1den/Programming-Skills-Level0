import os, json, uuid
from . import currencyexchange
from flask import session, render_template, request, redirect, url_for

# using USD as the base currency
#     (rate,   min,   max)
USD = (1.0, 10, 19_000)
CLP = (0.0011, 8_900, 16_900_000)
ARS = (0.0012, 8_200, 15_400_000)
EUR = (1.09, 10, 19_000)
TRY = (0.034, 300, 550_000)
GBP = (1.27, 10, 19_000)

@currencyexchange.route('/')    
def hello():

    if request.args.get('error'):
        error = { 'error': request.args.get('error') }
        
        return render_template('currency_exchange/index.html', **error)
    
    if 'exchange_history' in session:
        context = {
            'exchange_history': session['exchange_history'] }
        return render_template('currency_exchange/index.html', **context)
    
    return render_template('currency_exchange/index.html')


@currencyexchange.route('/exchange_preview', methods=['POST'])
def exchange_preview():
    
    # get data from form
    currency_from = request.form.get('origin_currency')
    currency_to = request.form.get('destination_currency')
    amount = request.form.get('amount')
    
    # convert amount to float
    amount = float(amount)
    
    # convert currency to float
    if currency_from == 'USD':
        currency_from = USD
    elif currency_from == 'CLP':
        currency_from = CLP
    elif currency_from == 'ARS':
        currency_from = ARS
    elif currency_from == 'EUR':
        currency_from = EUR
    elif currency_from == 'GBP':
        currency_from = GBP

    if currency_to == 'USD':
        currency_to = USD
    elif currency_to == 'CLP':
        currency_to = CLP
    elif currency_to == 'ARS':
        currency_to = ARS
    elif currency_to == 'EUR':
        currency_to = EUR
    elif currency_to == 'TRY':
        currency_to = TRY
    elif currency_to == 'GBP':
        currency_to = GBP

    # min and max amount validation
    if not currency_from[1] <= amount <= currency_from[2]:
        # raise error message
        error = {
            'error': f'Amount must be between {currency_from[1]} and {currency_from[2]}'
        }
        return redirect(url_for('currencyexchange.hello', **error))

    # selected currency to usd
    currency_from_to_usd = amount * currency_from[0]
    # usd to selected currency
    prev_exchange = round(currency_from_to_usd / currency_to[0], 2)
    # 1% fee
    fee = round(prev_exchange * 0.01, 2)
    # subtract fee from exchange
    exchange = round(prev_exchange - fee, 2)

    # return data to template
    context = {
        'origin_currency': request.form.get('origin_currency'),
        'destination_currency': request.form.get('destination_currency'),
        'amount': amount,
        'exchange': prev_exchange,  
        'fee': fee,
        'final_exchange': exchange
    }

    return render_template('currency_exchange/exchange_preview.html', **context)


@currencyexchange.route('/exchange_confirm', methods=['POST'])
def exchange_confirm():
    
        currency_from = request.form.get('origin_currency')
        currency_to = request.form.get('destination_currency')
        amount = request.form.get('amount')
        exchange = request.form.get('exchange')
        fee = request.form.get('fee')
        final_exchange = request.form.get('final_exchange')

        # add to session
        if 'exchange_history' not in session:
            session['exchange_history'] = []

        exchange_history = session['exchange_history']
        
        exchange_history.append({
            'id': str(uuid.uuid4())[:8],
            'origin_currency': currency_from,
            'destination_currency': currency_to,
            'amount': amount,
            'exchange': exchange,
            'fee': fee,
            'final_exchange': final_exchange
        })
        session['exchange_history'] = exchange_history

        return redirect(url_for('currencyexchange.hello'))


@currencyexchange.route('/reset')
def reset():
    session.pop('exchange_history', None)
    return redirect(url_for('currencyexchange.hello'))
