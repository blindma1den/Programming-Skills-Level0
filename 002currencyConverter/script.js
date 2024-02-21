/*Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice.
* 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.*/

let usdToClp = 918.30;
let usdToArs = 814.40;
let usdToEur = 0.92;
let usdToTry = 29.94;
let usdToGbp = 0.79;
let usdToUsd = 1;

let clpSelected = document.getElementById("clpSelected");
let arsSelected = document.getElementById("arsSelected");
let usdSelected = document.getElementById("usdSelected");
let eurSelected = document.getElementById("eurSelected");
let trySelected = document.getElementById("trySelected");
let gbpSelected = document.getElementById("gbpSelected");


clpSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);

    if (amount <10 || amount > 1000) {
        let principalContainer = document.getElementById("principalContainer");
        let error = document.createElement("p");
        error.classList.add("error");
        error.innerText = "You should write an amount between 10 and 1000";
        principalContainer.append(error);
    } else {
        let firstCoinRateValue = firstCoinRate(); 
        let dollars = amount * firstCoinRateValue;
        let result = dollars * usdToClp;
        document.getElementById("total").innerText = result.toFixed(2);
    }
});

arsSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    if (amount <10 || amount > 1000) {
        let principalContainer = document.getElementById("principalContainer");
        let error = document.createElement("p");
        error.classList.add("error");
        error.innerText = "You should write an amount between 10 and 1000";
        principalContainer.append(error);
    } else {

    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToArs;
    document.getElementById("total").innerText = result.toFixed(2);
}
});

usdSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    
    if (amount <10 || amount > 1000) {
        let principalContainer = document.getElementById("principalContainer");
        let error = document.createElement("p");
        error.classList.add("error");
        error.innerText = "You should write an amount between 10 and 1000";
        principalContainer.append(error);
    } else {

    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToUsd;
    document.getElementById("total").innerText = result.toFixed(2);
}
});

eurSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    if (amount <10 || amount > 1000) {
        let principalContainer = document.getElementById("principalContainer");
        let error = document.createElement("p");
        error.classList.add("error");
        error.innerText = "You should write an amount between 10 and 1000";
        principalContainer.append(error);
    } else {
    
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToEur;
    document.getElementById("total").innerText = result.toFixed(2);
}
});

trySelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    if (amount <10 || amount > 1000) {
        let principalContainer = document.getElementById("principalContainer");
        let error = document.createElement("p");
        error.classList.add("error");
        error.innerText = "You should write an amount between 10 and 1000";
        principalContainer.append(error);
    } else {
    
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToTry;
    document.getElementById("total").innerText = result.toFixed(2);
}
});

gbpSelected.addEventListener("click", function() {
    let amount = parseInt(document.getElementById("amount").value);
    if (amount <10 || amount > 1000) {
        let principalContainer = document.getElementById("principalContainer");
        let error = document.createElement("p");
        error.classList.add("error");
        error.innerText = "You should write an amount between 10 and 1000";
        principalContainer.append(error);
    } else {
    
    let firstCoinRateValue = firstCoinRate(); 
    let dollars = amount * firstCoinRateValue;
    let result = dollars * usdToGbp;
    document.getElementById("total").innerText = result.toFixed(2);
}
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
let parrafo;

let withdrawButton = document.getElementById("withdrawButton");
withdrawButton.addEventListener("click", function() {
    let amount = parseFloat(document.getElementById("total").innerText);
    let commission = amount * 0.01; 
    let totalAfterCommission = amount - commission;
    
    let withdraw = document.querySelector(".withdraw");
    let parrafo = document.createElement("p");
    parrafo.classList.add("texto");
    parrafo.innerText = "You have withdraw: $" + totalAfterCommission.toFixed(2);
    withdraw.append(parrafo);
    
    let textComission = document.createElement("p");
    textComission.classList.add("textComission");
    textComission.innerText = "The commision has been the 1%, which is: " + commission.toFixed(2);
    withdraw.append(textComission);

    let question = document.createElement("p");
    question.classList.add("question");
    question.innerText = "Do you want to perform another operation?";
    withdraw.append(question);
    
    let answerYes = document.createElement("button");
    answerYes.classList.add("button");
    answerYes.innerText = "Yes"
    withdraw.append(answerYes);

    let answerNo = document.createElement("button");
    answerNo.classList.add("button");
    answerNo.innerText = "No"
    withdraw.append(answerNo);

    answerYes.addEventListener("click", function() {
        parrafo.innerText = "";
        textComission.innerText = "";
        question.innerText = "";
        let radioButtons = document.querySelectorAll('input[name="firstCoin"]');
        radioButtons.forEach(button => button.checked = false);
        let radioButtonsSecond = document.querySelectorAll('input[name="secondCoin"]');
        radioButtonsSecond.forEach(button => button.checked = false);
        document.getElementById("amount").value = "0";
        document.getElementById("total").innerText= "0";
        answerYes.remove();
        answerNo.remove();

    });

    answerNo.addEventListener("click", function() {
        document.getElementById("principalContainer").style.display = "none";
    });
});

let notWithdrawButton = document.getElementById("notWithdrawButton");
notWithdrawButton.addEventListener("click", function() {
        let radioButtons = document.querySelectorAll('input[name="firstCoin"]');
        radioButtons.forEach(button => button.checked = false);
        let radioButtonsSecond = document.querySelectorAll('input[name="secondCoin"]');
        radioButtonsSecond.forEach(button => button.checked = false);
        document.getElementById("amount").value = "0";
        document.getElementById("total").innerText= "0";
});


