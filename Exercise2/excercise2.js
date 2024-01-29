let user = {
    balance: 1000
}

let exchangeRate = {
    "USD": 1,
    "EUR": 0.92,
    "CLP": 924,
    "ARS": 818,
    "TRY": 30.11,
    "GBP": 0.79
}

let currencyConverter = (fromCurrency, moneyAmount, toCurrency) => {

    let conversionToUsd = moneyAmount / exchangeRate[fromCurrency];
    let convertedCurrency = 0;

    if (conversionToUsd > 100) {
        console.log("Max amount is 100 USD or the equivalent in " + fromCurrency)
    } else if (conversionToUsd < 10) {
        console.log("Min amount is 10 USD or the equivalent in " + fromCurrency)
    } else {
        convertedCurrency = conversionToUsd * exchangeRate[toCurrency]
    }

    return convertedCurrency
};


console.log(currencyConverter("GBP", 15, "CLP"))

let withdraw = (withdrawalAmount) => {
    let amountPlusFee = withdrawalAmount + (withdrawalAmount / 100);
    let result = user["balance"] - amountPlusFee;
    return result
}

console.log(withdraw(10))