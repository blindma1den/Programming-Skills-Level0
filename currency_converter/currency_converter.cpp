#include <iostream>
using namespace std;

int showMenu();

class Currency {
    public:
        Currency(string name, double usdRate );
        string getName();
        double getUSDRate();
    private:
        string _name; 
        double _usdRate; 
};

double convertToUsd(Currency currency, double value);
double convertFromUsd(Currency currency, double value);
double convertCurrency(Currency inputCurrency, Currency outputCurrency, double value);
Currency getCurrencyFromName(string name);

int main (int argc, char *argv[]){

    double money;
    double moneyConverted;
    string inputCurrency, outputCurrency;

    int option = showMenu();
    if( option == 1){
        cout << "Choose your input currency from the following list" << endl;
        cout << "CLP, ARS, USD, EUR, TRY, GBP" << endl;
        cout << "Currency: ";
        cin >> inputCurrency;
        cout << "Value: ";
        cin >> money;
        cout << "Choose your output currency" << endl;
        cin >> outputCurrency;
        cout << "Input Currency was " << inputCurrency << endl;
        moneyConverted = convertCurrency(getCurrencyFromName(inputCurrency),getCurrencyFromName(outputCurrency),money);
        cout << outputCurrency << ": "<< moneyConverted;

    }
    return 0;
}

int showMenu(){

    int menuOption = 0;

    cout<<"CURRENCY CONVERTER MENU"<<endl;
    cout<<"1. CONVERT CURRENCY"<<endl;
    
    cout<<"Select option: ";
    cin >> menuOption;

    return menuOption;
}


Currency::Currency(std::string name, double usdRate){
    _name = name;
    _usdRate = usdRate;
}

std::string Currency::getName(){
    return _name;
}

double Currency::getUSDRate(){
    return _usdRate;
}

double convertToUsd(Currency currency, double value){
    return value/currency.getUSDRate();
}

double convertFromUsd(Currency currency, double value) {
    return value*currency.getUSDRate();
}

double convertCurrency(Currency inputCurrency, Currency outputCurrency, double value) {
    return convertFromUsd(outputCurrency,convertToUsd(inputCurrency,value));
}

Currency getCurrencyFromName(string name){

    Currency USD("USD",1.0);
    Currency COP("COP", 3893.45);
    Currency CLP("CLP", 889.95);
    Currency ARS("ARS",811.20);
    Currency EUR("EUR",0.91);
    Currency TRY("TRY",29.82);
    Currency GBP("GBP",0.79);

    if (name.compare(USD.getName()) == 0) return USD;
    if (name.compare(COP.getName()) == 0) return COP;
    if (name.compare(CLP.getName()) == 0) return CLP;
    if (name.compare(ARS.getName()) == 0) return ARS;
    if (name.compare(EUR.getName()) == 0) return EUR;
    if (name.compare(TRY.getName()) == 0) return TRY;
    if (name.compare(GBP.getName()) == 0) return GBP;

    cout << "Not available currency taking USD as Default";
    return USD;

}