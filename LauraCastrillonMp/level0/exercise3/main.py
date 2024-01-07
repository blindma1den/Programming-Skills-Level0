import csv

# Initialize the available program slots
program_slots = {
    'Computer Science': 5,
    'Medicine': 5,
    'Marketing': 5,
    'Arts': 5
}

# Initialize the campus slots
campus_slots = {
    'London': 1,
    'Manchester': 3,
    'Liverpool': 1
}

# Initialize the login attempts counter
login_attempts = 0

# Main function for the enrollment system
def enrollment_system():
    global login_attempts
    # Check if the user is locked out
    if login_attempts >= 3:
        print("You have exceeded the maximum number of login attempts. The system is locked.")
        return
    
    # Prompt for username and password
    username = input("Username: ")
    password = input("Password: ")
    
    # Validate the username and password
    if validate_login(username, password):
        # Display the available programs
        print("Available Programs:")
        for program in program_slots.keys():
            print(program)
        
        # Prompt for program choice
        program_choice = input("Choose your program: ")
        
        # Prompt for personal information
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        
        # Prompt for campus choice
        campus_choice = input("Choose your campus (London, Manchester, Liverpool): ")
        
        # Check if the chosen program is available at the selected campus
        if program_slots[program_choice] > 0 and campus_slots[campus_choice] > 0:
            # Decrease the available slots for the program and campus
            program_slots[program_choice] -= 1
            campus_slots[campus_choice] -= 1
            
            # Store the user data in a CSV file
            with open('enrollment_data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name, last_name, program_choice, campus_choice])
            
            print("Enrollment successful!")
        else:
            # Display the option to enroll in the program at another campus
            print("The chosen program is not available at the selected campus.")
            print("Would you like to enroll in the program at another campus?")
            print("1. Yes")
            print("2. No")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                # Prompt for another campus choice
                campus_choice = input("Choose another campus (London, Manchester, Liverpool): ")
                
                # Check if the chosen program is available at the new campus
                if program_slots[program_choice] > 0 and campus_slots[campus_choice] > 0:
                    # Decrease the available slots for the program and campus
                    program_slots[program_choice] -= 1
                    campus_slots[campus_choice] -= 1
                    
                    # Store the user data in a CSV file
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
        enrollment_system()

# Function to validate the login credentials
def validate_login(username, password):
    # Replace with your own logic to validate login credentials
    if username == 'admin' and password == 'password':
        return True
    else:
        return False

# Run the enrollment system
enrollment_system()