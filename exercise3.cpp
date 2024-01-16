/*The system has a login with a username and password.
 * 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
 * 		The user must input their first name, last name, and chosen program.
 * 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
 * 		If login information is incorrect three times, the system should be locked.
 * 		The user must choose a campus from three cities: London, Manchester, Liverpool.
 * 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
 * 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
 */

#include <iostream>

using namespace std;

const string fix_user = "admin";
const string fix_pass = "1234";

string get_user = "";
string get_pass = "";
int tries = 3;
bool access_flag = false; 

int select_program = 0;
int select_campus = 0;
bool fail = false;

struct CAMPUS
{
    string name;
    int cs_slots;
    int med_slots;
    int mark_slots;
    int arts_slots;
};

struct PROGRAM
{
    string name;
    CAMPUS campus;
};

struct USER
{
    string first_name;
    string last_name;
    PROGRAM program;
};

int main()
{
    CAMPUS london;
    london.name = "London";
    london.cs_slots = 1;
    london.med_slots = 1;
    london.mark_slots = 1;
    london.arts_slots = 1;

    CAMPUS manchester;
    manchester.name = "Manchester";
    manchester.cs_slots = 3;
    manchester.med_slots = 3;
    manchester.mark_slots = 3;
    manchester.arts_slots = 3;

    CAMPUS liverpool;
    liverpool.name = "Liverpool";
    liverpool.cs_slots = 1;
    liverpool.med_slots = 1;
    liverpool.mark_slots = 1;
    liverpool.arts_slots = 1;

    PROGRAM computer_science;
    computer_science.name = "Computer Science";

    PROGRAM medicine;
    medicine.name = "Medicine";

    PROGRAM marketing;
    marketing.name = "Marketing";

    PROGRAM arts;
    arts.name = "Arts";

    USER user;


    do
    {   
        cout << "Welcome to the registration system for educational programs.  \n";
        cout << "Please put your user and password.\n";
        cout << "User: \n";
        cin >> get_user;
        cout << "Password: \n";
        cin >> get_pass;
        if (get_user == fix_user && get_pass == fix_pass)
        {
            cout << "Access granted \n";
            access_flag = true;
        }
        else
        {
            tries--;
            cout << "Wrong Data, " << tries << " left.\n";
            if (tries == 0)
            {
                cout << "Closing registration system...";
                exit(0);
            }
        }
    } while (access_flag = false);
    

    do
    {
        fail = false;
        cout << "Welcome to the registration system for educational programs.  \n";
        cout << "These are the programs alvailable: \n";
        cout << "1. Computer Science. \n";
        cout << "2. Medicine. \n";
        cout << "3. Marketing. \n";
        cout << "4. Arts \n";
        cout << "Please type your first name: \n";
        cin >> user.first_name;
        cout << "Please type your last name: \n";
        cin >> user.last_name;
        cout << "Please type the program you wish to enroll it: \n";
        cin >> select_program;

        switch (select_program)
        {
        case 1:
            cout << "You've selected Computer Science. \n";
            user.program = computer_science;
            break;

        case 2:
            cout << "You've selected Medicine. \n";
            user.program = medicine;
            break;

        case 3:
            cout << "You've selected Marketing. \n";
            user.program = marketing;
            break;

        case 4:
            cout << "You've selected Arts. \n";
            user.program = arts;
            break;

        default:
            cout << "Wrong input, try again please. \n";
            break;
        }

        cout << "These are the campus alvailable: \n";
        cout << "1. London. \n";
        cout << "2. Manchester. \n";
        cout << "3. Liverpool. \n";
        cout << "Please type the program you wish to enroll it: \n";
        cin >> select_campus;

        switch (select_campus)
        {
        case 1:
            cout << "You've selected London. \n";
            user.program.campus = london;
            if (user.program.name == "Computer Science" && london.cs_slots > 0)
            {
                london.cs_slots--;
            }
            else if (user.program.name == "Medicine" && user.program.campus.med_slots > 0)
            {
                london.med_slots--;
            }
            else if (user.program.name == "Marketing" && user.program.campus.mark_slots > 0)
            {
                london.mark_slots--;
            }
            else if (user.program.name == "Arts" && user.program.campus.arts_slots > 0)
            {
                london.arts_slots--;
            }
            else
            {
                cout << "The program don't have alvailable slots. please try again \n . \n . \n . \n";
                fail = true;
            }
            break;

        case 2:
            cout << "You've selected Manchester. \n";
            user.program.campus = manchester;
            if (user.program.name == "Computer Science" && user.program.campus.cs_slots > 0)
            {
                manchester.cs_slots--;
            }
            else if (user.program.name == "Medicine" && user.program.campus.med_slots > 0)
            {
                manchester.med_slots--;
            }
            else if (user.program.name == "Marketing" && user.program.campus.mark_slots > 0)
            {
                manchester.mark_slots--;
            }
            else if (user.program.name == "Arts" && user.program.campus.arts_slots > 0)
            {
                manchester.arts_slots--;
            }
            else
            {
                cout << "The program don't have alvailable slots. please try again \n . \n . \n . \n";
                fail = true;
            }
            break;

        case 3:
            cout << "You've selected Liverpool. \n";
            user.program.campus = liverpool;
            if (user.program.name == "Computer Science" && user.program.campus.cs_slots > 0)
            {
                liverpool.cs_slots--;
            }
            else if (user.program.name == "Medicine" && user.program.campus.med_slots > 0)
            {
                liverpool.med_slots--;
            }
            else if (user.program.name == "Marketing" && user.program.campus.mark_slots > 0)
            {
                liverpool.mark_slots--;
            }
            else if (user.program.name == "Arts" && user.program.campus.arts_slots > 0)
            {
                liverpool.arts_slots--;
            }
            else
            {
                cout << "The program don't have alvailable slots. please try again \n . \n . \n . \n";
                fail = true;
            }
            break;

        default:
            cout << "Wrong type of data, please try again. \n . \n . \n . \n ";
            break;
        }

        if (!fail)
        {
            cout << "Congratz! Your final data is here: \n";
            cout << "First name: " << user.first_name << endl;
            cout << "Last name: " << user.last_name << endl;
            cout << "Program: " << user.program.name << endl;
            cout << "Campus: " << user.program.campus.name << endl;
            cout << "See you in class!\n";
        }

    } while (1);
}