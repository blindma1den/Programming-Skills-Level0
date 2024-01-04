'''Create an university enrollment system with the following characteristics:
* 		The system has a login with a username and password.
* 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
* 		The user must input their first name, last name, and chosen program.
* 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 		If login information is incorrect three times, the system should be locked.
* 		The user must choose a campus from three cities: London, Manchester, Liverpool.
* 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
* 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.'''
from banking_system import login

available_programs = {
    "Computer science": {"London": 1, "Manchester": 3, "Liverpool": 1},
    "Medicine": {"London": 1, "Manchester": 3, "Liverpool": 1},
    "Marketing": {"London": 1, "Manchester": 3, "Liverpool": 1},
    "Arts": {"London": 0, "Manchester": 0, "Liverpool": 0}
}
limit=3

registered_users =[]

def main():
    userid = input("type your ID: ")
    password = input("type your contraseña: ")
    limit = 2
    control = 'Y'

    while not login(userid, password)and limit >0:
        print("wrong credentials!")
        limit -=1
        userid = input("type your ID: ")
        password = input("type your contraseña: ")
    if limit == 0:
        print("sorry, you're suspended")
    else:
        print("welcome to the enrollment system.\n")      
        name = input("type your name\n").capitalize()
        last_name= input("type you last name\n").capitalize()
        program_list = [key for key in available_programs.keys()]
        while control == 'Y':
            program = input(f"Choose your program of preference.\n {program_list} ").capitalize()
            if not availavility(program): 
                print("There's no quota for this program")
            else:
                campus_list = [key for key in available_programs[program].keys()]
                campus = input(f"Choose campus.\n {campus_list} ").capitalize()
                if not enrollment(name, last_name, program,campus):
                    print("sorry, the quota is Full for this campus, you may try another one.")
                print(f"Success! You are enrrolled in {program}")
                break
            control= input("do you want to continue? Y/N").upper()
                

def enrollment(name:str, last_name:str, program:str, campus:str)->bool:
    
    if available_programs[program][campus] == 0:
        return False
    else:
        registered_users.append({name+last_name:{program:campus}})
        available_programs[program][campus] -= 1
        return True
    
def availavility(program)->bool:
    a = sum(available_programs[program].values())
    if a==0:
        return False
    return True


    
if __name__ == "__main__":
    main()   






