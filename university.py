'''
3. Create a university enrollment system with the following characteristics:
* 		The system has a login with a username and password.
* 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
* 		The user must input their first name, last name, and chosen program.
* 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 		If login information is incorrect three times, the system should be locked.
* 		The user must choose a campus from three cities: London, Manchester, Liverpool.
* 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
* 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
'''

registrations = []
attempts = 0

def check_register():
    global attempts
    while attempts < 3:
        username = input('Enter username: ')
        if any(user['username'] == username for user in registrations):
            password = input('Enter password: ')
            if any(user['password'] == password for user in registrations):
                print('Welcome', username)
                return True
            else:
                print('Incorrect password, try again')
                attempts += 1
        else:
            print('Username does not exist')

    print('Too many incorrect attempts. System locked')
    return False

def slots(program, campus):
    slots_available = {'London': 1, 'Manchester': 3, 'Liverpool': 1}
    taken = sum(1 for user in registrations if user['program'] == program and user['campus'] == campus)
    return slots_available[campus] - taken

programs = {
    '1': 'Computer Science',
    '2': 'Medicine',
    '3': 'Marketing',
    '4': 'Arts'
}

campuses = {
    '1': 'London',
    '2': 'Manchester',
    '3': 'Liverpool'
}

def register():
    username = input('Enter username: ')
    if not any(user['username'] == username for user in registrations):
        password = input('Enter password: ')
        name = input('Enter name: ')
        surname = input('Enter surname: ')

        print("\nPrograms:")
        for key, value in programs.items():
            print(f"{key}. {value}")

        program_choice = input('Choose a program (type a number from the list): ')
        program = programs.get(program_choice)

        print("\nCampuses:")
        for key, value in campuses.items():
            print(f"{key}. {value}")

        campus_choice = input('Choose a campus (type a number from the list): ')
        campus = campuses.get(campus_choice)

        if program and campus:
            available_slots = slots(program, campus)

            if available_slots > 0:
                registrations.append({
                    'username': username,
                    'password': password,
                    'name': name,
                    'surname': surname,
                    'program': program,
                    'campus': campus
                })
                print('Registration successful')
            else:
                print(f'There are no available slots for {program} at {campus}. Try again.')
        else:
            print('Invalid program or campus choice.')
    else:
        print('Username already exists. Please choose another username.')

if __name__ == "__main__":
    register()
