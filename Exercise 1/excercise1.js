// User's database:

let users = {
    user1: {
        balance: 2000,
        password: 1234
    },

    user2: {
        balance: 1500,
        password: 5678
    },

};


// Transactions's functions:

let deposit = (user, depositedAmount) => {
    return users[user]['balance'] += depositedAmount;
}

let withdraw = (user, withdrawalAmount) => {
    return users[user]['balance'] -= withdrawalAmount
    
};

let transfer = (fromUser, toUser, amount) => {
    withdraw(fromUser, amount)
    deposit(toUser, amount)
    return users;
};

let viewBalance = (user) => {
    return users[user]['balance']
};

// Login's menu:

loginUsername = prompt("Enter username")
loginPassword = prompt("Enter password")


let login = (inputUsername, password) => {

    let counterCredentials = 1

    // while ((users[inputUsername] === undefined || users[inputUsername]['password'] != password) && ++counterCredentials < 3)  {
    //     console.log("Incorrect username or password")
    // } 
    
    while (counterCredentials < 3)  {
        if (users[inputUsername] === undefined || users[inputUsername]['password'] != password) {
            ++counterCredentials;
            loginUsername = prompt("Please, enter correct username")
            loginPassword = prompt("Please, enter correct password")
            console.log("Failed attempts " + counterCredentials)
        } else {
            console.log("Correct login!") 
            menu()
            break}
    } 

    if (counterCredentials == 3) {
        console.log("Your account has been blocked!")
    } 
    // else if (users[inputUsername]['password'] === password ) {
    //     console.log("You're logged in!")
        
    // }
};

// let inputUsername = prompt('Please enter your username')
// let counterUsername = 0;

// while (inputUsername != users[inputUsername] && ++counterUsername < 3) {
//     inputUsername = prompt('Please enter your correct username')
// }   

// if (counterUsername == 3) {
//     alert("Your account has been blocked!")
// } else {
//     alert("Correct Username")
// }

// Menu:

let menu = () => {

let menuOption = 0;

while (menuOption != 5) {
    console.log(`
BlindMaiden Bank
1.Transfer
2.Deposit
3.Withdraw
4.View Balance
5.Quit
`);

menuOption = prompt("Select an option");
switch(menuOption) {
    case "1":
        console.log("You will transfer"); 
        break;
    case "2":
        console.log("You will deposit");
        break;
    case "3":
        console.log("You will withdraw");
        break;
    case "4":
        console.log("You will view your Balance");
        // selectUser = prompt('Select a user')
        console.log(viewBalance(loginUsername))
        break;
    case "5":
        break
    default:
        console.log("Incorrect Option");
         }
    }
}


// Now, we test the functions:
// console.log(transfer('user1', 'user2', 500))
login(loginUsername, loginPassword)

