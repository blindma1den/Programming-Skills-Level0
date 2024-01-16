/*
2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice.
* 		The system should ask the user if they want to per15form another operation. If they choose to do so, it should restart the process; otherwise, the system should close.

*/

#include <iostream>

using namespace std;

int base_currency = 0, conv_currency = 0;
float value = 0, v_cop = 0, withdraw_c = 0;
char withdraw_flag = ' ';
bool repeat_flag = false;

const float CLP_RATE = 4.38;
const float ARS_RATE = 4.81;
const float USD_RATE = 3910;
const float EUR_RATE = 4298.26;
const float TRY_RATE = 131.01;
const float GBP_RATE = 4990.26;

void menu()
{

    cout << "Welcome to the Currency Converter\n";
    cout << "Our currencys are: \n";
    cout << "1. Chilean Peso (CLP). \n";
    cout << "2. Argentine Peso (ARS). \n";
    cout << "3. United State Dollar (USD). \n";
    cout << "4. Euro (EUR). \n";
    cout << "5. Turkish Lira (TRY). \n";
    cout << "6. Pound Sterling (GBP). \n";
    cout << "Select the base currency (enter 1 - 6): \n";
}

void storing()
{

    cin >> base_currency;
    cout << "Select the currency to exchange(enter 1 - 6): \n";
    cin >> conv_currency;
    cout << "Enter the value of the base currency: \n";
    cin >> value;
}

void base_convert()
{
    switch (base_currency)
    {
    case 1:
        
        v_cop = value * CLP_RATE;
        break;

    case 2:
        v_cop = value * ARS_RATE;
        break;

    case 3:
        v_cop = value * USD_RATE;
        break;

    case 4:
        v_cop = value * EUR_RATE;
        break;

    case 5:
        v_cop = value * TRY_RATE;
        break;

    case 6:
        v_cop = value * GBP_RATE;
        break;

    
    default:
        cout<<"Incorrect input, closing the software...";
        exit(0);
    break;
    }
}

void exchange()
{

    switch (conv_currency)
    {
    case 1:
        value = v_cop / CLP_RATE;
        break;

    case 2:
        value = v_cop / ARS_RATE;
        break;

    case 3:
        value = v_cop / USD_RATE;
        break;

    case 4:
        value = v_cop / EUR_RATE;
        break;

    case 5:
        value = v_cop / TRY_RATE;
        break;

    case 6:
        value = v_cop / GBP_RATE;
        break;

    default:
        cout<<"Incorrect input, closing the software...";
        exit(0);
    break;
    }

    cout << "The convertion between " << base_currency << " and " << conv_currency << " is: ";
    cout << value << endl;
}

void withdraw()
{
    cout<<"Do you want to withdraw your founds? (Y/N): ";
    cin>>withdraw_flag;
    if(withdraw_flag == 'Y'||withdraw_flag == 'y'){
        withdraw_c = value * 0.01;
        cout<<"Thanks! We are getting the 1% percent of the value that is " << withdraw_c <<endl;
        cout<<"Your withdraw without the commission is: " << (value * 0.99) <<endl;        
    }   
    cout<<"Do you make another operation? (Y/N): ";
    cin>>withdraw_flag;
    if(withdraw_flag == 'Y'||withdraw_flag == 'y'){
        repeat_flag = true;
    }
    else{
        cout<<"Thanks for using our services";
        exit(0);
    }
  
}

int main()
{

   
    do
    {
        menu();
        storing();
        base_convert();
        exchange();
        withdraw();
    } while (repeat_flag = true);
    
}