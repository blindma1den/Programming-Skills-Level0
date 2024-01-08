import os, json
from flask import session, url_for, render_template, redirect, request
from . import universityenrollment
from .users import UNIVERSITY_USERS
from .campus_slots import CAMPUS_SLOTS


@universityenrollment.route('/')
def hello():

    if 'university_login_counter' not in session:
        session['university_login_counter'] = 0

    if 'university_login' not in session:
        session['university_login'] = False

    if request.args.get('error') and session['university_login'] is False:
        error = { 'error': request.args.get('error') }
        return render_template('university_enrollment/login.html', **error)
    elif session['university_login'] is False:
        return render_template('university_enrollment/login.html')
    else:
        return redirect(url_for('universityenrollment.enrollment'))


@universityenrollment.route('/login', methods=['POST'])
def login():

    if 'university_login_counter' not in session:
        session['university_login_counter'] = 0
    
    session['university_login_counter'] += 1

    user_submitted = request.form.get('university_username')
    password_submitted = request.form.get('university_password')

    if session['university_login_counter'] > 3:
        error = { 'error': 'too many login attempts' }
        return redirect(url_for('universityenrollment.hello', **error))
    
    # find and validate user
    matched_user = next((user for user in UNIVERSITY_USERS\
                         if user['username'] == user_submitted\
                        and user['password'] == password_submitted), None)
    
    print(matched_user)
    print(type(matched_user))

    if matched_user is None:
        print('invalid credentials')
        error = { 'error': 'invalid credentials' }
        return redirect(url_for('universityenrollment.hello', **error))
    else:

        session['university_login'] = True
        session['university_login_counter'] = 0

        session['university_username'] = user_submitted
        session['university_name'] = matched_user['name']
        session['university_last_name'] = matched_user['last_name']

        context = {
            'username': session['university_username'],
            'name': session['university_name'],
            'last_name': session['university_last_name'], }
        return redirect(url_for('universityenrollment.program', **context))
    



@universityenrollment.route('/program', methods=['GET', 'POST'])
def program():

    if 'university_login' not in session or session['university_login'] is False:

        return redirect(url_for('universityenrollment.hello'))


    if request.method == 'GET':
    
        context = {
            'username': session['university_username'],
            'name': session['university_name'],
            'last_name': session['university_last_name'], }

        return render_template('university_enrollment/programs.html', **context)
    

@universityenrollment.route('/campus', methods=['GET', 'POST'])
def campus():

    if 'university_login' not in session or session['university_login'] is False:

        return redirect(url_for('universityenrollment.hello'))
    
    if 'university_campus_slots' not in session:
        session['university_campus_slots'] = CAMPUS_SLOTS
    
    if request.method == 'POST':

        session['university_selected_program'] = request.form.get('university_program')
        return redirect(url_for('universityenrollment.campus')) 

    if request.method == 'GET':
        
        available_slots_validation = [{
                'campus': campus['campus'],
                'slots': [
                    {'program': program['program'], 'slots': program['slots'], 'available': False} if program['slots'] == 0 else program
                    for program in campus['slots']
                    if program['program'] == session['university_selected_program']
                ]}
            for campus in session['university_campus_slots']]

        print(json.dumps(available_slots_validation, indent=4))
        print(f'debudebug: {session["university_name"]}')
        context = {
            'username': session['university_username'],
            'name': session['university_name'],
            'last_name': session['university_last_name'],
            'program': session['university_selected_program'],
            'campus_slots': available_slots_validation, }

        return render_template('university_enrollment/campus.html', **context)
    

@universityenrollment.route('/enrollment', methods=['GET', 'POST'])
def enrollment():

    if 'university_login' not in session or session['university_login'] is False:

        return redirect(url_for('universityenrollment.hello'))
    
    if 'university_campus_slots' not in session:
        session['university_campus_slots'] = CAMPUS_SLOTS
    
    if request.method == 'POST':
        
        campus_selected = request.form.get('university_campus')
        program_selected = request.form.get('university_program')

        # find campus
        campus = next((campus for campus in session['university_campus_slots']\
                       if campus['campus'] == campus_selected), None)
        
        # find program
        program = next((program for program in campus['slots']\
                        if program['program'] == program_selected), None)

        program['slots'] -= 1

        # update session
        session['university_campus_slots'] = session['university_campus_slots']

        if 'enrollment_history' not in session:
            session['enrollment_history'] = []

        enrollment_details = {
            'username': session['university_username'],
            'name': session['university_name'],
            'last_name': session['university_last_name'],
            'program': session['university_selected_program'],
            'campus': campus_selected,}

        enrollment_history = session['enrollment_history']
        enrollment_history.append(enrollment_details)
        
        session['enrollment_history'] = enrollment_history

        print("\nenrollment history\n")
        print(json.dumps(session['enrollment_history'], indent=4))


        return redirect(url_for('universityenrollment.enrollment', **enrollment_details))

    if request.method == 'GET':


        

        context = {
            'username': request.args.get('username'),
            'name': request.args.get('name'),
            'last_name': request.args.get('last_name'),
            'program': request.args.get('program'),
            'campus': request.args.get('campus') }
        
        return render_template('university_enrollment/enrollment.html', **context)
    

@universityenrollment.route('/logout')
def logout():

    session['university_login'] = False
    session['university_login_counter'] = 0
    session['university_username'] = None
    session['university_name'] = None
    session['university_last_name'] = None
    session['university_selected_program'] = None

    return redirect(url_for('universityenrollment.hello'))


@universityenrollment.route('/reset')
def reset():
    for key in list(session.keys()):
        if key.startswith('university_'):
            session.pop(key)
    return redirect(url_for('universityenrollment.hello'))

