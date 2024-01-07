import csv

program_slots = {
    'Computer Science': 5,
    'Medicine': 5,
    'Marketing': 5,
    'Arts': 5
}

campus_slots = {
    'London': 1,
    'Manchester': 3,
    'Liverpool': 1
}

login_attempts = 0

def main3():
    global login_attempts
    if login_attempts >= 3:
        print("You have exceeded the maximum number of login attempts. The system is locked.")
        return
    
    username = input("Username: ")
    password = input("Password: ")
    
    if validate_login(username, password):
        print("Available Programs:")
        for program in program_slots.keys():
            print(program)
        
        program_choice = input("Choose your program: ")
        
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        
        campus_choice = input("Choose your campus (London, Manchester, Liverpool): ")
        
        if program_slots[program_choice] > 0 and campus_slots[campus_choice] > 0:
            program_slots[program_choice] -= 1
            campus_slots[campus_choice] -= 1
            
            with open('enrollment_data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name, last_name, program_choice, campus_choice])
            
            print("Enrollment successful!")
        else:
            print("The chosen program is not available at the selected campus.")
            print("Would you like to enroll in the program at another campus?")
            print("1. Yes")
            print("2. No")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                campus_choice = input("Choose another campus (London, Manchester, Liverpool): ")
                
                if program_slots[program_choice] > 0 and campus_slots[campus_choice] > 0:
                    program_slots[program_choice] -= 1
                    campus_slots[campus_choice] -= 1
                    
                    with open('enrollment_data.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([first_name, last_name, program_choice, campus_choice])
                    
                    print("Enrollment successful!")
                else:
                    print("The chosen program is not available at the selected campus.")
            else:
                print("Enrollment canceled.")
    else:
        login_attempts += 1
        print("Incorrect login credentials. Please try again.")
        main3()

def validate_login(username, password):
    if username == 'admin' and password == 'password':
        return True
    else:
        return False

main3()