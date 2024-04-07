import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)
MIN_VALUE = 20.0
MAX_VALUE = 3000.0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'convert':
            return redirect(url_for('convert'))
        elif action == 'exit':
            return "Goodbye!"
    return render_template('index.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']
        response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
        data = response.json()
        if 'rates' in data and to_currency in data['rates']:
            if float(amount) < MIN_VALUE or float(amount) > MAX_VALUE:
                error_message = "Amount should be between 20 and 3000."
                return render_template('convert.html', error=error_message)
            converted = data['rates'][to_currency] 
            if request.form.get('withdraw'):
                converted = converted - (converted * 0.01)
            return render_template('convert.html', converted=converted)
        else:
            error_message = "Could not get conversion rate from API."
            return render_template('convert.html', error=error_message)
    return render_template('convert.html')


if __name__ == '__main__':
    app.run(debug=False)