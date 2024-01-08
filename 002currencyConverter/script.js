/*Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice.
* 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.*/

let usdToClp = 903.83;
let usdToArs = 813.91;
let usdToEur = 0.91;
let usdToTry = 29.90;
let usdToGbp = 0.78;
let usdToUsd = 1;

/*let clpFirst = document.getElementById("clpFirst");
let arsFirst = document.getElementById("arsFirst");
let usdFirst = document.getElementById("usdFirst");
let eurFirst = document.getElementById("eurFirst");
let tryFirst = document.getElementById("tryFirst");
let gbpFirst = document.getElementById("gbpFirst");*/

let clpSelected = document.getElementById("clpSelected");
let arsSelected = document.getElementById("arsSelected");
let usdSelected = document.getElementById("usdSelected");
let eurSelected = document.getElementById("eurSelected");
let trySelected = document.getElementById("trySelected");
let gbpSelected = document.getElementById("gbpSelected");

clpSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToClp;
    document.getElementById("total").innerText = result;
});

arsSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToArs;
    document.getElementById("total").innerText = result;
});

usdSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToUsd;
    document.getElementById("total").innerText = result;
});

eurSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToEur;
    document.getElementById("total").innerText = result;
});

trySelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToTry;
    document.getElementById("total").innerText = result;
});

gbpSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToGbp;
    document.getElementById("total").innerText = result;
});

function firstCoinRate() {
    let firstCoin = document.querySelector('input[name="firstCoin"]:checked').id;
    let rate;

    if (firstCoin === "clpFirst") {
        rate = 0.0011;
    } else if (firstCoin === "arsFirst") {
        rate = 0.0012;
    } else if (firstCoin === "eurFirst") {
        rate = 1.10;
    } else if (firstCoin === "tryFirst") {
        rate = 0.033;
    } else if (firstCoin === "gbpFirst") {
        rate = 1.27;
    } else if (firstCoin === "usdFirst") {
        rate = 1;
    }

    return rate;
}



