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

let withdraw = (withdrawalAmount) => {
    let amountPlusFee = withdrawalAmount + (withdrawalAmount / 100);
    let amountLessFee = withdrawalAmount - (withdrawalAmount / 100);
    let result = user["balance"] - amountPlusFee;
    console.log('You will withdraw ' + amountLessFee + ". Your remaining balance is: " + result)
}

let subMenu = () => {

    let subMenuOption = 0
    let menuOption = 0

    while (subMenuOption != 2) {
        console.log(`
        BlindMaiden Currency Converter
        1. Yes
        2. No
        `)
    
    subMenuOption = prompt("Do you want to perform another operation?")

    switch (subMenuOption) {
        case "1":
            subMenuOption = 2
            break;
        case "2":
            menuOption = 3
            subMenuOption = 2
            break;
        }
    }

    return menuOption

}

let menu = () => {

    let menuOption = 0;

    while (menuOption != 3) {
        console.log(`
    BlindMaiden Currency Converter
    1. Currency Converter
    2. Withdraw
    3. Quit
    `)

    menuOption = prompt("Select an option");
    switch(menuOption) {
        case "1":
            fromCurrency = prompt("Select initial currency")
            moneyAmount = Number(prompt("How much you want to convert?"))
            toCurrency = prompt("Select the currency you want to exchange to")
            amountConverted = currencyConverter(fromCurrency, moneyAmount, toCurrency)
            console.log("You have successfully converted: " + amountConverted + " " +  toCurrency)
            menuOption = subMenu()
            break;
        case "2":
            amountToWithdraw = Number(prompt("How much do you want to Withdraw?"))
            withdraw(amountToWithdraw);
            menuOption = subMenu()
            break;
        case "3":
            break;
        }
    }
}

menu()
console.log(currencyConverter("GBP", 15, "CLP"))
