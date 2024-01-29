let users = {
    user1: {
        password: 1234
    },
    user2: {
        password:1234
    },
}

let packages = {}

loginUsername = prompt("Enter Username")
loginPassword = prompt("Enter Password")

let login = (username,password) => {

    let counterCredentials = 1

    while (counterCredentials < 3) {
        if (users[username] === undefined || users[username]["password"] != password) {
            ++counterCredentials
            loginUsername = prompt("Please, enter correct Username")
            loginPassword = prompt("Please, enter correct Password")
            console.log("Incorrect Username/Password. Failed attempts " + counterCredentials + " . Max attempts 3")
        } else {
            console.log("Successful Login")
            menu()
            break
        }
    }

    if (counterCredentials == 3) {
        console.log("Your account has been blocked!")
    }
}

let calculatePrice = (weight) => {
    let price = weight * 2
    console.log("Your order has been created. Package number is " + Math.floor(Math.random() * 100) + ". Total amount to pay is $" + price)
}

let packageDetails = (sender, recipient) => {
    senderDetails = prompt("Enter sender details")
    senderRecipient = prompt("Enter recipient")
    inputWeight = prompt("Input total weight of the package")
    calculatePrice(inputWeight)
}



let menu = () => {

    let menuOption = 0;
    
    while (menuOption != 2) {
        console.log(`
    BlindMaiden Bank
    1.Send a package
    2.Quit
    `);
    
    menuOption = prompt("Select an option");
    switch(menuOption) {
        case "1":
            console.log("You will send a package")
            packageDetails();
            
            menuOption2 = prompt("Do you want to continue?");
            if (menuOption2 == "yes") {
                break;
            } else {
                menuOption = 2
                break;
            }
        case "2":
            console.log("Logging out from the system");
            break;
        default:
            console.log("Incorrect Option");
             }
        }
    }


login(loginUsername, loginPassword)

// packageDetails()