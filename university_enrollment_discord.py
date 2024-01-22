# 3.Create an university enrollment system with the following characteristics:

dict_auth = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6"   
}

computer_science_program = "Computer Science"
medicine_program = "Medicine"
marketing_program = "Marketing"
arts_program = "Arts"

london = "London"
manchester = "Manchester"
liverpool = "Liverpool"

programs_registration = {
    computer_science_program: {
        london: [],
        manchester: [],
        liverpool: []
    },
    medicine_program: {
        london: [],
        manchester: [],
        liverpool: []
    },
    marketing_program : {
        london: [],
        manchester: [],
        liverpool: []
    },
    arts_program: {
        london: [],
        manchester: [],
        liverpool: []
    }
}

# In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
campus_slots = {
    london: 1,
    manchester: 3,
    liverpool: 1    
}

def login():
    count_pwd = 0
    auth = False
    
    # The system has a login with a username and password.
    while True:
        user = input("Enter username: ")
        password = input("Enter password: ")
        if user in dict_auth and password == dict_auth.get(user):
            print("Valid login")
            auth = True
            # Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
            # The user must input their first name, last name, and chosen program.
            while True:
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                
                print("See the menu program and chooose one of them: ")
                print("a. Computer Science") 
                print("b. Medicine")     
                print("c. Marketing")     
                print("d. Arts")
                option_program = input()
                
                if option_program == "a":
                    program = computer_science_program
                elif option_program == "b":
                    program = medicine_program
                elif option_program == "c":
                    program = marketing_program
                elif option_program == "d":
                    program = arts_program                
                
                # The user must choose a campus from three cities: London, Manchester, Liverpool.
                print("Choose the campus: ")
                print("1. London") 
                print("2. Manchester")     
                print("3. Liverpool")
                option_campus = input()
                    
                if option_campus == "1":
                    campus = london
                elif option_campus == "2":
                    campus = manchester
                elif option_campus == "3":
                    campus = liverpool
                    
                    
                # Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, 
                # it should display a message indicating the program is unavailable.
            
            
                if len(programs_registration[program][campus]) < campus_slots[campus]:
                    programs_registration[program][campus].append("{0}, {1}".format(last_name, first_name))
                    print("Registration Succesful")
                    break
                else:
                    print("The campus", campus, "is complete")
                    # If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
                    for key in programs_registration[program]:
                        if key != campus:
                            if len(programs_registration[program][key]) < campus_slots[key]:
                                print("There is availability in", key)
                                print("Do you want to register?")
                                print("Yes")
                                print("No")
                                option = input()
                                if option =="Yes":
                                    programs_registration[program][campus].append("{0}, {1}".format(last_name, first_name))
                                    print("Registration Succesful")
                                    break
                                else:
                                    print("Bye")
                                    break
                                    
                                    
        else:
            # If login information is incorrect three times, the system should be locked.
            count_pwd = count_pwd + 1
            if count_pwd < 3:
                print("Try again")
            else:
                print("User blocked")
                break           

login()