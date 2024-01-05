#Exercise 3#
#!Create an university enrollment system!#
#|The system has a login with a username and password.
#|Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
#|The user must input their first name, last name, and chosen program.
#?Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
#|If login information is incorrect three times, the system should be locked.
#?The user must choose a campus from three cities: London, Manchester, Liverpool.
#?In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
#?If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.

users = {"admin": "12345", "admin2":"67890"}

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

def programs(firts_name, last_name):
    print(f"{firts_name} {last_name}, welcome to the university enrollment system")
    print("1.Computer Sciencie\n2.Medicine\n3.Marketing\n4.Arts")
    selection = input("Which program would you like to enroll?: ")

def main(attempts):
    if(attempts > 0):
        print(f"You have {attempts} attempt(s) left")
        login_screen_user(attempts)
        firts_name, last_name = enter_student_name()
        programs(firts_name, last_name)
    else:
        print("To many failed attempts. The system will be locked.")

main(3)