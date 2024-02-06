const maxLoginAttempts = 2;
let loginAttempts = 0;
let accountLocked = false;
total = 2000;


document.getElementById("loginButton").addEventListener("click", login);
document.getElementById("loginForm").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        login();
    }
});

function login() {
    if (accountLocked) {
        let blockedAccountMessageHide = document.getElementById("blockedAccountMessageHide");
        blockedAccountMessageHide.style.display = "block";
        invalidLoginHide.style.display = "none";
        return;
    }

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (username === "1" && password === "1") {
        let loginForm = document.getElementById("loginForm");
        loginForm.style.display = "none";
        let balanceContainer = document.getElementById("balanceContainer");
        balanceContainer.style.display = "flex";
        
    } else {
        let invalidLoginHide = document.getElementById("invalidLoginHide");
        invalidLoginHide.style.display = "block";
        loginAttempts++;

        if (loginAttempts >= maxLoginAttempts) {
            accountLocked = true;
        }
        
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";

    }
}


// deposit 

let deposit = document.getElementById("deposit");
deposit.addEventListener("click", showDepositMenu);

function showDepositMenu() {
    document.getElementById("depositContainer").style.display = "flex";
    document.getElementById("withdrawContainer").style.display = "none";
    document.getElementById("viewContainer").style.display = "none";
    document.getElementById("transferContainer").style.display = "none";
}

function addMoney() {
    let depositAmountInput = document.getElementById("depositAmountInput").value;
    let amount = parseFloat(depositAmountInput);

    if (!isNaN(amount) && amount > 0) {
        total += amount;
        updateBalance();
    }

    updateViewTotalAmount()

    document.getElementById("depositAmountInput").value = "0";
}

function updateBalance() {
    document.getElementById("total").innerText = total;
}

let sendButton = document.getElementById("send");
sendButton.addEventListener("click", addMoney);

// withdraw

let withdraw = document.getElementById("withdraw");
withdraw.addEventListener("click", showWithdrawMenu);

function showWithdrawMenu() {
    document.getElementById("withdrawContainer").style.display = "flex";
    document.getElementById("depositContainer").style.display = "none";
    document.getElementById("viewContainer").style.display = "none";
    document.getElementById("transferContainer").style.display = "none";
}

function withdrawMoney() {
    let withdrawAmountInput = document.getElementById("withdrawAmountInput").value;
    let amount = parseFloat(withdrawAmountInput);

    if (!isNaN(amount) && amount > 0) {
        total -= amount;
        updateBalance();
    }

    updateViewTotalAmount()

    document.getElementById("withdrawAmountInput").value = "0";
 
}

let withdrawSendButton = document.getElementById("withdrawSendButton");
withdrawSendButton.addEventListener("click", withdrawMoney);

// transfer

let transfer = document.getElementById("transfer");
transfer.addEventListener("click", showtransferMenu);

function showtransferMenu() {
    document.getElementById("transferContainer").style.display = "flex";
    document.getElementById("viewContainer").style.display = "none";
    document.getElementById("withdrawContainer").style.display = "none";
    document.getElementById("depositContainer").style.display = "none";
}

function transferMoney() {
    let transferAmountInput = document.getElementById("transferAmountInput").value;
    let amount = parseFloat(transferAmountInput);
    let transferToAccountInput = document.getElementById("transferToAccountInput").value;
    
    if (!isNaN(amount) && amount > 0 && !isNaN(transferToAccountInput)) {
        total -= amount;
        updateBalance();
        invalidAccountNumber.style.display = "none";
    } else {
        let invalidAccountNumber = document.getElementById("invalidAccountNumber");
        invalidAccountNumber.style.display = "block";
    }

    updateViewTotalAmount() 

    document.getElementById("transferAmountInput").value = "0";
    document.getElementById("transferToAccountInput").value = "";
}

let transferSendButton = document.getElementById("transferSendButton");
transferSendButton.addEventListener("click", transferMoney);


// view

let view = document.getElementById("view");
view.addEventListener("click", showviewMenu);

function showviewMenu() {
    document.getElementById("viewContainer").style.display = "flex";
    document.getElementById("withdrawContainer").style.display = "none";
    document.getElementById("depositContainer").style.display = "none";
    document.getElementById("transferContainer").style.display = "none";
}

function updateViewTotalAmount() {
    document.getElementById("viewTotalAmount").innerText = total;
}






   


