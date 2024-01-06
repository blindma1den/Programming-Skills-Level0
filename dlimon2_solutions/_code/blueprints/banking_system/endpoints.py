import os, json
from . import bankingsystem
from flask import session, render_template, request, redirect, url_for

USER = os.getenv('BANCADEV_USER')
PASSWORD = os.getenv('BANCADEV_PASSWORD')

@bankingsystem.route('/')
def hello():

    if 'bancadev_login_counter' not in session:
        session['bancadev_login_counter'] = 0

    if 'bancadev_balance' not in session:
        session['bancadev_balance'] = 2000
    
    if 'bancadev_login' not in session or session['bancadev_login'] == False:
        session['bancadev_login'] = False
        return render_template('banking_system/login.html')
    elif 'bancadev_login' in session and session['bancadev_login'] == True:
        return redirect(url_for('bankingsystem.dashboard'))

    
    return redirect(url_for('bankingsystem.login'))


@bankingsystem.route('/login', methods=['POST'])
def login():

    session['bancadev_login_counter'] += 1

    user_submitted = request.form.get('bancadev_username')
    password_submitted = request.form.get('bancadev_password')

    print(user_submitted, password_submitted, type(user_submitted), type(password_submitted))
    print(USER, PASSWORD, type(USER), type(PASSWORD))

    if session['bancadev_login_counter'] > 3:
        return 'error: too many login attempts'
    
    if user_submitted != USER or password_submitted != PASSWORD:
        return 'error. bad data'
    
    if user_submitted == USER and password_submitted == PASSWORD:
        session['bancadev_login'] = True
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/dashboard')
def dashboard():

    if session['bancadev_login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    context = {
        'balance': session['bancadev_balance'],
        'login': session['bancadev_login'],
        'username': USER }
    
    return render_template('banking_system/dashboard.html', **context)


@bankingsystem.route('/deposit', methods=['GET', 'POST'])
def deposit():

    if session['bancadev_login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    if request.method == 'GET':
        return render_template('banking_system/deposit.html', balance=session['bancadev_balance'])
    
    if request.method == 'POST':
        deposit_amount = request.form.get('bancadev_deposit_amount')
        
        #type check
        if not deposit_amount.isdigit():
            return 'error: invalid deposit amount'
        
        deposit_amount = int(deposit_amount)
        
        #value check
        if deposit_amount < 0:
            return 'error: deposit amount cannot be negative'
        if deposit_amount > 9999:
            return 'error: deposit amount exceeds the limit'
        
        session['bancadev_balance'] += deposit_amount
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/withdraw', methods=['GET', 'POST'])
def withdraw():

    if session['bancadev_login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    if request.method == 'GET':
        return render_template('banking_system/withdraw.html', balance=session['bancadev_balance'])
    
    if request.method == 'POST':
        withdraw_amount = request.form.get('bancadev_withdraw_amount')
        
        #type check
        if not withdraw_amount.isdigit():
            return 'error: invalid withdraw amount'
        
        withdraw_amount = int(withdraw_amount)
        
        #value check
        if withdraw_amount < 0:
            return 'error: withdraw amount cannot be negative'
        if withdraw_amount > session['bancadev_balance']:
            return 'error: withdraw amount exceeds the limit'
        
        session['bancadev_balance'] -= withdraw_amount
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/transfer', methods=['GET', 'POST'])
def transfer():

    if session['bancadev_login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    if request.method == 'GET':
        return render_template('banking_system/transfer.html', balance=session['bancadev_balance'])
    
    if request.method == 'POST':
        transfer_amount = request.form.get('bancadev_transfer_amount')
        transfer_to = request.form.get('bancadev_transfer_user')
        
        #type check
        if not transfer_amount.isdigit():
            return 'error: invalid transfer amount'
        
        transfer_amount = int(transfer_amount)
        
        #value check
        if transfer_amount < 0:
            return 'error: transfer amount cannot be negative'
        if transfer_amount > session['bancadev_balance']:
            return 'error: transfer amount exceeds the limit'
        
        #transfer to check
        if transfer_to == USER:
            return 'error: invalid transfer to'
        
        session['bancadev_balance'] -= transfer_amount
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/logout')
def logout():
    
    session['bancadev_login'] = False
    session['bancadev_login_counter'] = 0
    return redirect(url_for('bankingsystem.hello'))


@bankingsystem.route('/reset')
def reset():

    for key in list(session.keys()):
        if key.startswith('bancadev_'):
            session.pop(key)
    return redirect(url_for('bankingsystem.hello'))