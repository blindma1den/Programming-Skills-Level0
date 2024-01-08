#!/bin/bash
declare -A currencyToDollar=( ["ARS"]="0.0012" ["CLP"]="0.0011" ["EUR"]="0.85" ["TRY"]="12" ["GBP"]="0.72" )
declare -A dollarToDesireCurrency=( ["ARS"]="810.91" ["CLP"]="890.08" ["EUR"]="0.91" ["TRY"]="29.83" ["GBP"]="0.79" )
declare -A dataUser


echo "************************* Currency converter *************************"

echo "What is your name? "
read userName
dataUser=( ["$userName"]="0" )
balance="0"

keepConverting="true"

echo "$keepConverting"

while [ "$keepConverting" == "true" ]; do

    echo "Avalible currencies CLP"
    
    echo "Enter your currency: For example => CLP"
    read fromCurrency

    echo "Enter the currency you want to exchange"
    read  toCurrency

    echo "************************************************************"
    
    echo "Enter the amount to convert"
    read amount 

    # Convert user currency to dollar
    rateCurrencyDollar="${currencyToDollar["$fromCurrency"]}"
    dollar=$(bc -l <<< "$amount * $rateCurrencyDollar")

    #convert dollar to requested currency
    requestedCurrency="${dollarToDesireCurrency["$toCurrency"]}"
    result=$(bc -l <<< "$dollar * $requestedCurrency + $balance")

    balance=$result
    dataUser["$userName"]="$result"

    echo "Do you want to withdraw your funds?"
    echo "Type 1 to withdraw"
    echo "Type 2 to keep adding funds to your current balance"

    read response

    if [ "$response" == "1" ]; then
        echo "Processing withdrawal..."
        echo "Charging commission..."
        echo "Money withdrawn: ${dataUser["$userName"]}" | awk -F'.' '{print $1}'
        echo "Current Balance: 0"
        echo "Withdrawal successful"

        echo "Do you want to exit the program?"
        echo "Type 'x' to exit"
        read option

        if [ "$option" == "x" ]; then
            keepConverting="false"
        fi

    elif [ "$response" == "2" ]; then
        continue
    else
        keepConverting="false"
    fi


done