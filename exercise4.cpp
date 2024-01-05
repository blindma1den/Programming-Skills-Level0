/*
4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt.
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.
* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.

*/

#include <iostream>
#include <string>
using namespace std;

const string fix_user = "admin";
const string fix_pass = "1234";

string user = "";
string pass = "";
string sender = "";
string addressee = "";
string city = "";

char deliver = ' ';

int tries = 3, menu = 0, weight = 0;

bool access_flag = false, repeat_flag = false;

int main()
{

    cout << "Welcome to the Shipping System\n";
    do
    {
        cout << "Please put your user and password.\n";
        cout << "User: \n";
        cin >> user;
        cout << "Password: \n";
        cin >> pass;
        if (user == fix_user && pass == fix_pass)
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
                cout << "Closing Shipping System...";
                exit(0);
            }
        }
    } while (access_flag = false);

    do
    {
        repeat_flag = false;
        cout << "Main Menu: \n";
        cout << "1. Send a Package: \n";
        cout << "2. Exit: \n";
        cout << "Please select one option: ";
        cin >> menu;

        switch (menu)
        {
        case 1:
            cout << "Please specify the sender of the package: \n";
            cin >> sender;
            cout << "Please specify the addressee of the package: \n";
            cin >> addressee;
            cout << "Please specify the city of delivery of the package: \n";
            cin >> city;
            cout << "Please specify the total weight (in Kg) of the package: \n";
            cin >> weight;
            cout << "Your delivery will cost: $" << (weight * 2) << " USD \n";
            cout << "Do you agree? (Y/N): ";
            cin >> deliver;
            if (deliver == 'Y' || deliver == 'y')
            {
                cout << "Thanks! Your shipping details are this: \n";
                cout << "Shippin number: " << (rand()) << endl;
                cout << "Sender: " << sender << endl;
                cout << "Addressee: " << addressee << endl;
                cout << "City: " << city << endl;
                cout << "Weight: " << weight << endl;
                cout << "Final Cost: $" << (weight * 2) << "USD \n";
                cout << " \n";
                cout << "Do you want to perform another operation? \n";
                cin >> deliver;
                if (deliver == 'Y' || deliver == 'y')
                {
                    repeat_flag = true;
                }
                else
                {
                    cout << "Thanks for using our services.\n";
                    cout << "Closing Shipping System...";
                    exit(0);
                }
            }
            else
            {
                repeat_flag = true;
            }
            break;

        case 2:
            cout << "Closing Shipping System...";
            exit(0);
            break;

        default:
            cout << "Please select a valid option \n";
            repeat_flag = true;
            break;
        }
    } while (repeat_flag = true);
}