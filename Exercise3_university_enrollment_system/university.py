import time


def login(university_user):
    login_counter = 0

    while login_counter < 3:
        option = int(input("1. Sign in  2. Create an account "))
        if option == 1:
            username = input("Enter username: ")
            entered_password = input("Enter password: ")

            found_user = False  # Indicate if a valid user was found

            for user in university_user:
                # Compare input of user with data each tuple
                if user[0] == username and user[1] == entered_password:
                    print("Welcome!")
                    found_user = True  # User found
                    display_program()
                    break  # exit for
            if found_user:
                break
            if not found_user:  # if found_user is False, means there not user
                login_counter += 1
                print("Invalid username or password.")

                if login_counter == 3:
                    print("You've exceeded login attempts. You're block, you need to wait for 10 seconds")
                    time.sleep(10)
                    login_counter = 0  # Reset login attempts after the wait time

        elif option == 2:
            # Create new account
            username = input("Enter username: ")
            entered_password = input("Enter password: ")
            university_user.append((username, entered_password))
            print("Account created successfully.")
            break
    else:
        print("Invalid option.")

def display_program():
    print("Available programs")
    print("1.- Computer Science 2.- Medicine 3.- Marketing 4.- Arts")
    choose_program = int(input("What program do you want?"))
    user_name = input("Enter your first name")
    user_lastname = input("Enter your last name")

    if choose_program < 5:
        choose_program += 1
        choose_campus()
    else:
        print("The program is unavailable")

def choose_campus():
    print("Choose one campus")

#To be continue...
university_user = [('Jose', '1234'), ('Maria', '12345'), ('Marcos', '4568')]
login(university_user)
