let users = {
    user1: {
        password: 1234
    },
    user2: {
        password: 1234
    },
    user3: {
        password: 1234
    },
    user4: {
        password: 1234
    },
    user5: {
        password: 1234
    }
}

let login = (username, password) => {
    if (users[username] === undefined || users[username]["password"] != password) {
        console.log("Incorrect username/password")
    } else {
        console.log("Successful Login!")
        menu(username)
    }
}


let menu = (username) => {

    let counterCS = 0;
    let counterMed = 0;
    let counterMarketing = 0;
    let counterArts = 0;

    let menuOption = 0;

    let submitFullName = (username) => {
        enterFirstName = prompt("Enter first Name")
        enterLastName = prompt("Enter last name")

        let fullName = enterFirstName + " " + enterLastName

        users[username]['fullName'] = fullName
    }
    
    while (menuOption != 5) {
        console.log(`
    BlindMaiden University
    1.Computer Science
    2.Medicine
    3.Marketing
    4.Arts
    5.Quit
    `);
    
    menuOption = prompt("Select an option");
    switch(menuOption) {
        case "1":
            if (counterCS < 2) {
                counterCS++
            console.log("You will enroll in Computer Science"); 
            submitFullName(username)
            users[username]['Program'] = "Computer Science"
                }
            else {
                console.log("Program Unavailable")};
            break;
        case "2":
            if (counterMed < 2) {
                counterMed++
                console.log("You will enroll in Medicine");
            }
            break;
        case "3":
            console.log("You will enroll in Marketing");
            break;
        case "4":
            console.log("You will enroll in Arts");
            break;
        case "5":
            break
        default:
            console.log("Incorrect Option");
             }
    console.log(counterCS)
        }
    }

let choiceCampus = () => {
    let menuOptionCampus = 0;
    let counterCampusLondon = 0;
    let counterCampusManchester = 0;
    let counterCampusLiverpool = 0;

    while (menuOptionCampus =! 4) {
        console.log(`
        BlindMaiden University
        1.London
        2.Manchester
        3.Liverpool
        4.Quit
        `);

        menuOptionCampus = prompt("Choose a campus");
        switch(menuOptionCampus) {
            case "1":
                break;
            case "2":
                break;
            case "3":
                break;
            case "4":
                break;
        }
    }
}

console.log(users)
login("user1", 1234)


