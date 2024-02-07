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

let submenu = () => {
    let subMenu = 0
    let menuOption = 0

    while(subMenu != 2) {
        console.log(`
        BlindMaiden DHL
        1.Yes
        2.No
        `);

        subMenu = prompt("Do you want to perform another operation?")
        switch (subMenu) {
            case "1":
                subMenu = 2
                break;
            case "2":
                menuOption = 2
                subMenu = 2
                console.log("Logging out from the system");
                break;
        }
    }
    return menuOption
}

let menu = () => {

    let menuOption = 0;
    
    while (menuOption != 2) {
        console.log(`
    BlindMaiden DHL
    1.Send a package
    2.Quit
    `);
    
    menuOption = prompt("Select an option");
    switch(menuOption) {
        case "1":
            console.log("You will send a package")
            packageDetails();
            menuOption = submenu();
            break;
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