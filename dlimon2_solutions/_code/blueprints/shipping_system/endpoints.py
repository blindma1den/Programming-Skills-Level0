import os, json, uuid
from . import shippingsystem
from flask import session, render_template, request, redirect, url_for

USER = os.getenv('SHIPPING_USER')
PASSWORD = os.getenv('SHIPPING_PASSWORD')

@shippingsystem.route('/')
def hello():

    if 'shipping_login_counter' not in session:
        session['shipping_login_counter'] = 0
    
    if 'shipping_login' not in session or session['shipping_login'] == False:
        session['shipping_login'] = False
        return render_template('shipping_system/login.html')
    elif 'shipping_login' in session and session['shipping_login'] == True:
        return redirect(url_for('shippingsystem.dashboard'))

    
    return redirect(url_for('shippingsystem.login'))


@shippingsystem.route('/login', methods=['POST'])
def login():

    session['shipping_login_counter'] += 1

    user_submitted = request.form.get('shipping_username')
    password_submitted = request.form.get('shipping_password')


    if session['shipping_login_counter'] > 3:
        return 'error: too many login attempts'
    
    if user_submitted != USER or password_submitted != PASSWORD:
        return 'error. bad data'
    
    if user_submitted == USER and password_submitted == PASSWORD:
        session['shipping_login'] = True
        return redirect(url_for('shippingsystem.dashboard'))
    


@shippingsystem.route('/dashboard')
def dashboard():

    if session['shipping_login'] == False:
        return redirect(url_for('shippingsystem.hello'))

    context = {
        'login': session['shipping_login'],
        'username': USER,
        'shipping_history': '' }

    if 'shipping_history' not in session:
        session['shipping_history'] = []


    context['shipping_history'] = session['shipping_history']
        

    return render_template('shipping_system/dashboard.html', **context)


@shippingsystem.route('/send', methods=['POST', 'GET'])
def send():

    if session['shipping_login'] == False:
        return redirect(url_for('shippingsystem.hello'))
    
    if request.method == 'POST':
        sender = request.form.get('shipping_sender')
        receiver = request.form.get('shipping_receiver')
        weight = request.form.get('shipping_package_weight')

        total_price = int(weight) * 2

        shipping_info = {
            'sender': sender,
            'receiver': receiver,
            'weight': weight,
            'total_price': total_price }
        
        return redirect(url_for('shippingsystem.send_confirmation', **shipping_info))
    
    if request.method == 'GET':
        return render_template('shipping_system/send.html', sender=USER)
    

@shippingsystem.route('/send_confirmation', methods=['POST', 'GET'])
def send_confirmation():

    if session['shipping_login'] == False:
        return redirect(url_for('shippingsystem.hello'))
    
    if request.method == 'POST':

        shipping_info = {
            'sender': request.form.get('shipping_sender'),
            'receiver': request.form.get('shipping_receiver'),
            'weight': request.form.get('shipping_package_weight'),
            'total_price': request.form.get('shipping_total_price'),
            'shipping_id': request.form.get('shipping_id') }

        shipping_history = session['shipping_history']
        shipping_history.append(shipping_info)
        session['shipping_history'] = shipping_history
        print (session['shipping_history'])

        return redirect(url_for('shippingsystem.dashboard'))
    
    if request.method == 'GET':
        shipping_info = {
        'sender': request.args.get('sender'),
        'receiver': request.args.get('receiver'),
        'weight': request.args.get('weight'),
        'total_price': request.args.get('total_price'),
        'shipping_id': uuid.uuid4() }
    
        return render_template('shipping_system/send_confirmation.html', **shipping_info)
    


@shippingsystem.route('/logout')
def logout():

    session['shipping_login'] = False
    session['shipping_login_counter'] = 0
    return redirect(url_for('shippingsystem.hello'))


@shippingsystem.route('/reset')
def reset():
    
    for key in list(session.keys()):
        if key.startswith('shipping_'):
            session.pop(key)

    return redirect(url_for('shippingsystem.hello'))