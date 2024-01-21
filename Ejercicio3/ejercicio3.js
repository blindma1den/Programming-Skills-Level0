// 3. Create an university enrollment system with the following characteristics:
// * 	The system has a login with a username and password.
// * 	Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
// * 	The user must input their first name, last name, and chosen program.
// * 	Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
// * 	If login information is incorrect three times, the system should be locked.
// * 	The user must choose a campus from three cities: London, Manchester, Liverpool.
// * 	In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
// * 	If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
const readline = require("readline");
let name;
let lastname;
let Program;
const users = [
  { username: "user1", password: "pass123" },
  { username: "user2", password: "pass456" },
  { username: "user3", password: "pass789" },
];
const programs = {
    ComputerScience: {
      totalStudents: 0,
      campuses: {
        London: [],
        Manchester: [],
        Liverpool: [],
      },
    },
    Medicine: {
      totalStudents: 0,
      campuses: {
        London: [],
        Manchester: [],
        Liverpool: [],
      },
    },
    Marketing: {
      totalStudents: 0,
      campuses: {
        London: [],
        Manchester: [],
        Liverpool: [],
      },
    },
    Arts: {
      totalStudents: 0,
      campuses: {
        London: [],
        Manchester: [],
        Liverpool: [],
      },
    },
  };
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
function askQuestion(question) {
  return new Promise((resolve) => {
    rl.question(question, resolve);
  });
}
async function login() {
  let username;
  let password;
  let tries = 1;

  while (tries <= 3) {
    username = await askQuestion("Enter your username: ");
    password = await askQuestion("Enter your password: ");

    const user = users.find(
      (student) =>
        student.username === username && student.password === password
    );

    if (user) {
      console.log("Login successful!");
      return true;
    } else {
      console.log("Incorrect credentials. Please try again.");
      tries++;
    }
  }

  console.log("Maximum attempts exceeded. Exiting...");
  return false;
}
async function enrollment() {
  console.log("Choose the program to enroll in");
  console.log("1. Computer Science");
  console.log("2. Medicine");
  console.log("3. Marketing");
  console.log("4. Arts");
  let NumProgram;
  try {
    NumProgram = await askQuestion("Please enter the number associated with the program: ");
    if (isNaN(Number(NumProgram)) || NumProgram < 1 || NumProgram > 4) {
      throw new Error("Invalid program number. Please enter a valid number.");
    }
  } catch (error) {
    console.log(error.message);
    await enrollment(); // Reinicia el proceso de inscripción si hay un error
    return;
  }
   name = await askQuestion("Please enter your name: ");
   lastname = await askQuestion("Please enter your lastname: ");

  switch (Number(NumProgram)) {
    case 1:
      Program = "ComputerScience";
      break;
    case 2:
      Program = "Medicine";
      break;
    case 3:
      Program = "Marketing";
      break;
    case 4:
      Program = "Arts";
      break;

    default:
      break;
  }

  if (programs[Program].totalStudents < 5) {
    console.log(Program);
    await chooseCampus();
  }else{
    console.log(`Sorry, there is no available slot for ${Program}.`);

  }
}
async function chooseCampus() {
    let campus;
    let campusFull = true;
  
    while (campusFull) {
      console.log("Choose a campus:");
      console.log("1. London");
      console.log("2. Manchester");
      console.log("3. Liverpool");
  
      let numCampus;
      try {
        numCampus = await askQuestion("Enter the number of your chosen campus: ");
        if (isNaN(Number(numCampus)) || numCampus < 1 || numCampus > 3) {
          throw new Error("Invalid campus number. Please enter a valid number.");
        }
      } catch (error) {
        console.log(error.message);
        continue;
      }
      
      switch (Number(numCampus)) {
        case 1:
          campus = "London";
          break;
        case 2:
          campus = "Manchester";
          break;
        case 3:
          campus = "Liverpool";
          break;
        default:
          break;
      }
  
      if (campus === "London" || campus === "Liverpool") {
        if (programs[Program].campuses[campus].length < 1) {
          campusFull = false;
        } else {
          console.log("The selected campus is full. Please choose another campus.");
        }
      } else if (campus === "Manchester") {
        if (programs[Program].campuses[campus].length < 3) {
            campusFull = false;
          } else {
            console.log("The selected campus is full. Please choose another campus.");
          }
        
      }
    }
  
    console.log(`${Program} ${campus}`);
    await registerStudent(Program, campus);
  }
async function registerStudent(program, campus) {
    const studentName = `${name} ${lastname}`;
    programs[program].totalStudents++;
    programs[program].campuses[campus].push(studentName)
    console.log(`
    Student Information:
    Name: ${name}
    Lastname: ${lastname}
    Program: ${program}
    Campus: ${campus}
    Enrollment successful!
  `);
  const continueEnrollment = await askQuestion("Do you want to continue enrollment? (yes/no): ");
  if (continueEnrollment.toLowerCase() === 'yes') {
    await enrollment();
  } else {
    rl.close();
  }
    
    
}
async function main() {
  const loggedIn = await login();
  if (loggedIn) {
    await enrollment();
  }
  rl.close();
}
main();
