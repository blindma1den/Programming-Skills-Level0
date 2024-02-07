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
            choiceCampus();
                }
            else {
                console.log("Program Unavailable")};
            break;
        case "2":
            if (counterMed < 2) {
                counterMed++
            console.log("You will enroll in Medicine");
            submitFullName(username)
            users[username]['Program'] = 'Medicine'
            }
            else {console.log("Program unavailable")}
            break;
        case "3":
            if (counterMarketing < 2) {
                counterMarketing++
            console.log("You will enroll in Marketing")
            submitFullName(username)
            users[username]['Program'] = 'Marketing'
            } else {console.log("Program unavailable")}
            break;
        case "4":
            if (counterArts < 2) {
                counterArts++
            console.log("You will enroll in Arts");
            submitFullName(username)
            user[username]['Program'] = 'Arts'
            } else { console.log("Program unavailable")}
            break;
        case "5":
            break
        default:
            console.log("Incorrect Option");
             }
        }
    }

    
let choiceCampus = () => {
   

    let counterCampusLondon = 0;
    let counterCampusManchester = 0;
    let counterCampusLiverpool = 0;

    let menuOptionCampus = 0;

    while (menuOptionCampus != 4) {
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
                if (counterCampusLondon < 1) {
                    counterCampusLondon++
                console.log("You will study in London")
                menuOptionCampus = 4
                } else {
                    console.log("No slots available in London. Choose another campus")
                }
                break;
            case "2":
                if (counterCampusManchester < 3) {
                    ++counterCampusManchester
                    console.log("You will study in Manchester")
                    menuOptionCampus = 4
                } else {
                    console.log("No slots available in Manchester. Choose another campus")
                }
                break;
            case "3":
                if (counterCampusLiverpool < 1) {
                    ++counterCampusLiverpool
                    console.log("You will study in Liverpool")
                    menuOptionCampus = 4
                } else {
                    console.log("No slots available in Liverpool. Choose another campus")
                }
                break;
            case "4":
                break;
            default:
                console.log("Incorrect Option")
        }
    }
}

console.log(users)
login("user1", 1234)