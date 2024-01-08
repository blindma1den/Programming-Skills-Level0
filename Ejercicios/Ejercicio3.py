# 3. Create an university enrollment system with the following characteristics:
# * 		(listo)The system has a login with a username and password.
# * 		(listo)Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
# * 		The user must input their first name, last name, and chosen program.
# * 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
# * 		(listo)If login information is incorrect three times, the system should be locked.
# * 		The user must choose a campus from three cities: London, Manchester, Liverpool.
# * 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
# * 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
import sys

class account:    
    def __init__(self):
        self.user = "a"
        self.password = "1"
        self.students ={}
        self.programs = {
            "Computer Science": {"London": 1, "Manchester": 3, "Liverpool": 1},
            "Medicine": {"London": 1, "Manchester": 3, "Liverpool": 1},
            "Marketing": {"London": 1, "Manchester": 3, "Liverpool": 1},
            "Arts": {"London": 1, "Manchester": 3, "Liverpool": 1}
        }
    


class login(account):
    def __init__(self):
        super().__init__()
        self.failed_attempts = 0
    
    def verify_user(self, input_user, input_password):
        if input_user == self.user and input_password == self.password:
            print("Successful Login!!")

            return True
            
        else:
            print("Incorrect Password!")
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                print("error number 3. The program will close")
                sys.exit()
            return False
        

class menu(account):
    def select(self):
        

        
        print("possible available programs!!!")
        print("-------------------------------")
        print("1. Computer science")
        print("2. Medicine")
        print("3. Marketing")
        print("4. Arts")
        print("5. Exit")
        print("--------------------------------")
    
    
        self.opcion = int(input(f"Enter option: "))
        return self.opcion



class actions(menu):
    
    def register(self, program):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        campus = input ("Choose a campus (London, Manchester, Liverpool): ")
        if self.programs[program][campus]>0:
            self.programs[program][campus] -= 1
            self.students[first_name + " " + last_name] = {"program": program, "campus": campus}
            print("Registration successful!")
        else:
            print("No available slots in this program at the chosen campus. Please choose another campus or program.")
    
    def computer_science(self):
        self.register("Computer Science")        
        print("Computer Science")
        
    def medicine(self):
        self.register("Medicine")    
        print("Medicine")
   
    def marketing(self):
        self.register("Marketing")    
        print("Marketing ")
        
   
    def arts(self):
        self.register("Arts")    
        print("Arts")
   
    def exit(self):
        print("exit")
        sys.exit()

    def numbers(self, opcion):
        if opcion == 1:
            self.computer_science()
        elif opcion == 2:
            self.medicine()
        elif opcion == 3:
            self.marketing()
        elif opcion == 4:
            self.arts()
        elif opcion == 5:
            self.exit()
        else:
           print("Invalid option")






if __name__ == "__main__":
    login_instance = login()

    logging = False
    while not logging:
        input_user = input("Enter your username: ")
        input_password = input("Enter your password: ")
        logging = login_instance.verify_user(input_user, input_password)
    menu_instance = menu()
    actions_instance = actions()
    while True:
        opcion = menu_instance.select()
        actions_instance.numbers(opcion)