# 3. Create an university enrollment system with the following characteristics:
# * 	The system has a login with a username and password.
# * 	Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
# * 	The user must input their first name, last name, and chosen program.
# * 	Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
# * 	If login information is incorrect three times, the system should be locked.
# * 	The user must choose a campus from three cities: London, Manchester, Liverpool.
# * 	In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
# * 	If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.

STUDENTS_DATA = {
        'student1': {'username': 'elyriven',
                  'password': 'devtraining123'
                 },
        'student2': {'username': 'shadowrun',
                  'password': 'devtraining321',
                 },
}

Available_Program_Slots = {
    'london': {
        'cs': 1,
        'medicine': 1,
        'marketing': 1,
        'arts': 0,
    },
    'manchester': {
        'cs': 3,
        'medicine': 3,
        'marketing': 3,
        'arts': 3,
    },
    'liverpool': {
        'cs': 1,
        'medicine': 1,
        'marketing': 1,
        'arts': 1,
    },
}

def main():
    attempts = 3
    end = 1
    csProgram = Program('cs')
    medProgram = Program('medicine')
    markProgram = Program('marketing')
    artsProgram = Program('arts')
    print('\t\t\tTraining University Campus\n\nLogin to Continue\n')
    while attempts != 0:
        username,password = login()
        loggedStudent = Student(username,password)
        if loggedStudent.checkStudent(loggedStudent.username,loggedStudent.password):
            print(f'\t\t\tWelcome to the Campus {loggedStudent.username}\n\n')
            break
        else:
            attempts -= 1
            print(f'Attempts left: {attempts}\n')
    else:
        print('System Locked Out')
        exit()

    while end != 0:
        print('Available Programs:\tComputer Science [cs] - Medicine [md] - Marketing [mk] - Arts [ar] - Logout [0]\n')
        print('Select an option: ')
        selectedOption = str(input('>> ')).lower()
        if selectedOption == '0':
            print('Logged Out')
            exit()
        else:
            selectedProgram = checkInput(selectedOption)
            if selectedProgram != None:
                try:
                    print('\nAvailable Campuses:\tLondon [lo] - Manchester [ma] - Liverpool [li]\n')
                    campusInput = str(input('>> ')).lower()
                    selectedCampus = checkCampus(campusInput)
                    if selectedCampus != None:
                        print('\nEnter your personal information\n')
                        fName = str(input('First Name: '))
                        lName = str(input('Last Name: '))
                        loggedStudent.name = fName
                        loggedStudent.lastName = lName
                        if selectedProgram == 'cs':
                            if csProgram.checkProgram(selectedCampus):
                                csProgram.signUp(selectedCampus)
                                print(f'You have successfully signed up for {selectedProgram} program at {selectedCampus} campus')
                            else:
                                print(f'There are no slots available in {selectedCampus} for the selected program')
                                continue
                        elif selectedProgram == 'medicine':
                            if medProgram.checkProgram(selectedCampus):
                                medProgram.signUp(selectedCampus)
                                print(f'You have successfully signed up for {selectedProgram} program at {selectedCampus} campus')
                            else:
                                print(f'There are no slots available in {selectedCampus} for the selected program')
                                continue
                        elif selectedProgram == 'marketing':
                            if markProgram.checkProgram(selectedCampus):
                                medProgram.signUp(selectedCampus)
                                print(f'You have successfully signed up for {selectedProgram} program at {selectedCampus} campus')
                            else:
                                print(f'There are no slots available in {selectedCampus} for the selected program')
                                continue
                        elif selectedProgram == 'arts':
                            if artsProgram.checkProgram(selectedCampus):
                                artsProgram.signUp(selectedCampus)
                                print(f'You have successfully signed up for {selectedProgram} program at {selectedCampus} campus')
                            else:
                                print(f'There are no slots available in {selectedCampus} for the selected program')
                                continue
                    else:
                        print('Invalid Campus')
                except:
                    print('Invalid Input')
            else:
                print('Invalid Program')
                continue

def checkInput(name):
    if name == 'cs':
        return 'cs'
    if name == 'md':
        return 'medicine'
    if name == 'mk':
        return 'marketing'
    if name == 'ar':
        return 'arts'
    
def checkCampus(name):
    if name == 'lo':
        return 'london'
    if name == 'ma':
        return 'manchester'
    if name == 'li':
        return 'liverpool'

def login():
    user = str(input('Username: ')).lower()
    password = str(input('Password: ')).lower()
    return user, password

class Student:
    def __init__(self, username, password, name = '', lastName = '', programs = {}):
        self.username = username
        self.password = password
        self.name = name
        self.lastName = lastName
        self.programs = programs

    def checkStudent(self,user,passw):
        x = 0
        userFlag = False
        while x < len(STUDENTS_DATA):
            if user == STUDENTS_DATA[f'student{x+1}']['username']:
                userFlag = True
                break
            else:
                x += 1
        else:
            print('Wrong Username\n')
            return False
        if userFlag == True:
            if passw == STUDENTS_DATA[f'student{x+1}']['password']:
                return True
            else:
                print('Wrong Password\n')
                return False

class Program():
    def __init__(self, name):
        self.name = name

    def checkProgram(self, city):
        if Available_Program_Slots[city][self.name] > 0:
            return True
        else:
            return False
    
    def signUp(self, city):
        Available_Program_Slots[city][self.name] -= 1


if __name__ == '__main__':
    main()