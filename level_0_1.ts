// 1. Create an online banking system with the following features:

// * Users must be able to log in with a username and password.
// * If the user enters the wrong credentials three times, the system must lock them out.
// * The initial balance in the bank account is $2000.
// * The system must allow users to deposit, withdraw, view, and transfer money.
// * The system must display a menu for users to perform transactions.2. 

//just logic
interface data {
    username: string,
    password: string,
    amount: number,
    loginAttempts: number,
    isLocked: boolean,
    depositAccount: string
}

const database = [
    {
        username: 'fedecha',
        password: 'fedecha',
        amount: 2000,
        isLocked: false,
        loginAttemps: 0
    }
]

const menu = ['view','withraw', 'deposit', 'transfer']

const login = (username: string, password: string, isLocked: boolean) => {
    //if you have a form gather the info of the form
    //let user = inputUsername.value 
    //let password = inputPassword.value

    let currentUser = database.find((user) => user.username === username)

    if (isLocked) {
        console.log("Your account is locked out!");
        return false;
    }

    if(currentUser && currentUser.password === password ){
        currentUser.loginAttemps = 0
        console.log("you're logged!")
        return menu.forEach(item => console.log(item))
    }else {
        if(currentUser){
            ++currentUser.loginAttemps
            if(currentUser.loginAttemps >= 3) return false
            else {  
                alert(`Incorrect username or password ${3 - currentUser.loginAttemps} attempts left.`)
                return false
            }
        }
    }
}

const viewAccount = (username: string): string => {
    let currentUser = database.find((user) => user.username === username);
    return `username:${currentUser?.username} Amount: ${currentUser?.amount}`
};

const deposit = (depositAccount:string, amount:number): string => {
    const depositAddress = database.find((user) => user.username === depositAccount)

    if(depositAddress) {
        depositAddress.amount += amount
        return `you deposited ${amount} to ${depositAddress.username} `
    }else {
        return 'deposit was incorrect'
    }
  
};

const transfer = (username: string, depositAccount:string, amount:number): string => {
    const currentUser = database.find((user) => user.username === username);
    const depositAddress = database.find((user) => user.username === depositAccount)

    if(currentUser && depositAddress) {
        if(currentUser.amount < amount) return "you don't have enough money for this transaction"
        else {
            currentUser.amount -= amount
            depositAddress.amount += amount
            return `you transfer ${amount} to ${depositAddress.username} `
        } 
    }else {
        return 'transfer was incorrect'
    }
  
};

const withraw = (username: string, amount:number): string => {
    const currentUser = database.find((user) => user.username === username);

    if(currentUser) {
        if(currentUser.amount < amount) return "you don't have enough money for this withrawal"
        else {
            currentUser.amount -= amount
            return `you withraw ${amount} from your bank account`
        } 
    }else {
        return 'transfer was incorrect'
    }
  
};