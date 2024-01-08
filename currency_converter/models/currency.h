#include <iostream>
using namespace std;
#pragma once

class Currency {
    public:
        Currency(string name, float usdRate );
        string getName();
    private:
        string name; 
        float usdRate; 
};