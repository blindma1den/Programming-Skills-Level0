import os, json
from . import bankingsystem
from flask import session, render_template, request, redirect, url_for

USER = os.getenv('BANCADEV_USER')
PASSWORD = os.getenv('BANCADEV_PASSWORD')

@bankingsystem.route('/')
def hello():

    if 'login_counter' not in session:
        session['login_counter'] = 0

    if 'balance' not in session:
        session['balance'] = 2000
    
    if 'login' not in session or session['login'] == False:
        session['login'] = False
        return render_template('login.html')
    elif 'login' in session and session['login'] == True:
        return redirect(url_for('bankingsystem.dashboard'))

    
    return redirect(url_for('bankingsystem.login'))


@bankingsystem.route('/login', methods=['POST'])
def login():

    session['login_counter'] += 1

    user_submitted = request.form.get('bancadev_username')
    password_submitted = request.form.get('bancadev_password')

    print(user_submitted, password_submitted, type(user_submitted), type(password_submitted))
    print(USER, PASSWORD, type(USER), type(PASSWORD))

    if session['login_counter'] > 3:
        return 'error: too many login attempts'
    
    if user_submitted != USER or password_submitted != PASSWORD:
        return 'error. bad data'
    
    if user_submitted == USER and password_submitted == PASSWORD:
        session['login'] = True
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/dashboard')
def dashboard():

    if session['login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    context = {
        'balance': session['balance'],
        'login': session['login'],
        'username': USER }
    
    return render_template('dashboard.html', **context)


@bankingsystem.route('/deposit', methods=['GET', 'POST'])
def deposit():

    if session['login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    if request.method == 'GET':
        return render_template('deposit.html', balance=session['balance'])
    
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
        
        session['balance'] += deposit_amount
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/withdraw', methods=['GET', 'POST'])
def withdraw():

    if session['login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    if request.method == 'GET':
        return render_template('withdraw.html', balance=session['balance'])
    
    if request.method == 'POST':
        withdraw_amount = request.form.get('bancadev_withdraw_amount')
        
        #type check
        if not withdraw_amount.isdigit():
            return 'error: invalid withdraw amount'
        
        withdraw_amount = int(withdraw_amount)
        
        #value check
        if withdraw_amount < 0:
            return 'error: withdraw amount cannot be negative'
        if withdraw_amount > session['balance']:
            return 'error: withdraw amount exceeds the limit'
        
        session['balance'] -= withdraw_amount
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/transfer', methods=['GET', 'POST'])
def transfer():

    if session['login'] == False:
        return redirect(url_for('bankingsystem.hello'))
    
    if request.method == 'GET':
        return render_template('transfer.html', balance=session['balance'])
    
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
        if transfer_amount > session['balance']:
            return 'error: transfer amount exceeds the limit'
        
        #transfer to check
        if transfer_to == USER:
            return 'error: invalid transfer to'
        
        session['balance'] -= transfer_amount
        return redirect(url_for('bankingsystem.dashboard'))
    

@bankingsystem.route('/logout')
def logout():
    session['login'] = False
    session['login_counter'] = 0
    return redirect(url_for('bankingsystem.hello'))


@bankingsystem.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('bankingsystem.hello'))