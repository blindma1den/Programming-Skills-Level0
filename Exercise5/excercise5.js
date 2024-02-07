let users = {
    user1: {
        income: 0
    }
    
}

let expenses = {
    medical: {
        amount: 500
    },
    household: {
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
    let savedIncome = users['user1']['income'] = newIncome
    console.log("Your monthly income is: " + savedIncome)
}

let recordExpenses = (category, amount) => {
    expenses[category]['amount'] = amount
    console.log("Expenses for " + category + " are " + amount)
}

let subMenu = () => {

    let subMenu = 0

    while (subMenu != 6) {
        console.log(`
    Expense Tracker
    1. Medical
    2. Household
    3. Leisure
    4. Savings
    5. Education
    6. Quit
    `)
    
    subMenu = prompt("List your expense")
    switch(subMenu) {
        case "1":
            inputAmount = Number(prompt("Record your expense"))
            recordExpenses("medical", inputAmount)
            break;
        case "2":
            inputHousehold = Number(prompt("Record your expense"))
            recordExpenses("household", inputHousehold)
            break;
        case "3":
            inputAmount = Number(prompt("Record your expense"))
            recordExpenses("leisure", inputAmount)
            break;
        case "4":
            inputAmount = Number(prompt("Record your expense"))
            recordExpenses("savings", inputAmount)
            break;
        case "5":
            inputAmount = Number(prompt("Record your expense"))
            recordExpenses("education", inputAmount)
            break;
        case "6":
            break;
        default:
            console.log("Incorrect Option")
        }
    }
}

let getTotalExpenses = (array) => {

    let total = 0;

    for (let i in array) {
        for(let j in array[i]) {
        total += array[i][j]
        }
    }

    return total
}

let financialStatus = (expenses) => {
    if (expenses > users['user1']['income']) {
        console.log("You need to improve your financial health")
    } else if (expenses === users['user1']['income']) {
        console.log("You need to reduce expenses in the category where you have spent the most money")
    } else {
        console.log("Congratulations!")
    }
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
            enterIncome = Number(prompt("Please, enter your income"))
            recordIncome(enterIncome)
            break;
        case "2":
            console.log("Please, record your expenses")
            subMenu()
            break;
        case "3":
            let totalExpenses = getTotalExpenses(expenses)
            console.log("Your total expenses are: " + totalExpenses)
            financialStatus(totalExpenses)
            break;
        case "4":
            break;
        default:
            console.log("Incorrect Option")
        }
    }
}

// recordExpenses("medical", 200)
console.log(expenses)
console.log(getTotalExpenses(expenses))
console.log(users)
console.log(users['user1']['income'])
menu()


