let users = {
    user1: {
        income: 0
    }
    
}

let expenses = {
    medical: {
        amount: 0
    },
    houseHold: {
        amount: 0
    },
    leisure: {
        amount: 0
    },
    savings: {
        amount: 0
    },
    education: {
        amount: 0
    }
}

let recordIncome = (newIncome) => {
    users['user1']['income'] = newIncome
}

let recordExpenses = (category, amount) => {
    expenses[category]['amount'] = amount
}

let menu = () => {
    
    let menuOption = 0;

    while (menuOption != 4) {
        console.log(`
    Blindmaiden Finance App
    1. Record income
    2. Record expenses
    3. Get total Expenses
    4. Quit
    `);
    
    menuOption = prompt("Select an option");
    switch(menuOption) {
        case "1":
            console.log("Please, enter your income")
            break;
        case "2":
            console.log("Please, record your expenses")
            break;
        case "3":
            console.log("Your total expenses are: ")
            break;
        default:
            console.log("Incorrect Option")
              }
    }
}

recordExpenses("medical", 200)
console.log(expenses)