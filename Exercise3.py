#Exercise 3#
#!Create an university enrollment system!#
#|The system has a login with a username and password.
#|Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
#|The user must input their first name, last name, and chosen program.
#|Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
#|If login information is incorrect three times, the system should be locked.
#|The user must choose a campus from three cities: London, Manchester, Liverpool.
#|In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
#|If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.

users = {"admin": "12345", "admin2":"67890"}
programs_index = {
    1:"Computer Science",
    2:"Medicine",
    3:"Marketing",
    4:"Arts"
}
campus_index = {
    1:"London",
    2:"Manchester",
    3:"Liverpool"
}
campus_availability = {
    1: [1,1,1,1],
    2: [3,3,3,3],
    3: [0,1,1,1]
}

def login_screen_user(attempts):
    user_input = input("user: ")
    if (validate_user(user_input)):
        password_input = input("password: ")
        if(validate_password(user_input, password_input)):
            return user_input, password_input
        else:
            return main(attempts - 1)
    else:
        print("User not found. Try again.")
        login_screen_user(attempts)

def validate_user(credential):
    if (credential in users):
        print("User found!")
        return True
    else:
        return False

def validate_password(user, password):
    if (password == users[user]):
        print("Access Granted")
        return True
    else:
        print("Incorrect password")
        return False

def enter_student_name():
    f_name = input("Please enter your first name: ").strip(" ")
    s_name = input("Please enter your last name: ").strip(" ")
    return f_name, s_name

def select_program():
    print("1.Computer Sciencie\n2.Medicine\n3.Marketing\n4.Arts")
    selection = input("Which program would you like to enroll?: ")
    if(selection.isnumeric() and int(selection) in range(1,5)):
        #print(f"You're trying to enroll to the {programs_index[int(selection)]} program")
        return selection, select_campus(selection)
    else:
        print("The input is not valid. Try again.")
        return select_program()

def select_campus(program):
    print(f"1.London [{campus_availability[1][int(program)-1]} slot(s) available]\n2.Manchester [{campus_availability[2][int(program)-1]} slot(s) available]\n3.Liverpool [{campus_availability[3][int(program)-1]} slot(s) available]")
    selection = input("In which campus would you like to enroll?: ")
    if(selection.isnumeric() and int(selection) in range(1,4)):
        return selection
    else:
        print("The input is not valid. Try again.")
        return select_campus(program)

def check_availability(program, campus):
    program_selected = programs_index[int(program)]
    campus_selected = campus_index[int(campus)]
    availability = campus_availability[int(campus)][int(program)-1]
    print(f"You're trying to enroll to the {program_selected} program in {campus_selected}.")
    if(availability > 0):
        print(f"There are {availability} slots availables")
        enroll_decision = input("Do you want to enroll? (y/n): ")
        if enroll_decision.lower() == 'y':
            print("You are now enrolled!")
            print("Thank you for your participation")
            campus_availability[int(campus)][int(program)-1] = campus_availability[int(campus)][int(program)-1] - 1
            main(3)
            # Puedes hacer más acciones aquí si es necesario
        else:
            print("You chose not to enroll.")
            program, campus = select_program()
            check_availability(program, campus)
    else:
        print(f"We are sorry. {program_selected} program is full. Please select another campus.")
        campus = select_campus(program)
        return check_availability(program, campus)

def main(attempts):
    if(attempts > 0):
        print(f"You have {attempts} attempt(s) left")
        login_screen_user(attempts)
        first_name, last_name = enter_student_name()
        print(f"{first_name}, welcome to the university enrollment system")
        program, campus = select_program()
        check_availability(program, campus)
        #print(programs_index[int(program)], campus_index[int(campus)])

    else:
        print("To many failed attempts. The system will be locked.")

main(3)