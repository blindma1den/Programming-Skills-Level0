// User's database:

let users = {
    user1: {
        balance: 2000,
        password: 1234
    },

    user2: {
        balance: 2000,
        password: 5678
    },

};

// Transactions's menu:

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

let login = (user, password) => {
    
    if (users[user] === undefined) {
        console.log("Username doesn't exist" )
    } else if (users[user]['password'] === password ) {
        console.log("You're logged in!")
    } else if (users[user]['password'] != password) {
        console.log("Incorrect password!")
    }
};



// console.log(withdraw('user1', 500))
console.log(transfer('user1', 'user2', 500))
login('user1', 12346)
