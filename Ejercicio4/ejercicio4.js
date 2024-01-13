// 4. Create an online shipping system with the following features:
// * The system has a login that locks after the third failed attempt.
// * Display a menu that allows: Sending a package, exiting the system.
// * To send a package, sender and recipient details are required.
// * The system assigns a random package number to each sent package.
// * he system calculates the shipping price. $2 per kg.
// * The user must input the total weight of their package, and the system should display the amount to pay.
// * The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu.
// If it's no, it should close the system.
import inquirer from "inquirer";

const users = [
  { username: "user1", password: "pass123" },
  { username: "user2", password: "pass456" },
  { username: "user3", password: "pass789" },
];
const askCredentials = [
  {
    type: "input",
    name: "username",
    message: "Enter your username:",
  },
  {
    type: "password",
    name: "password",
    message: "Enter your password:",
    mask: "*",
  },
];
const askMenu = {
  type: "list",
  name: "options",
  message: `What would you like to do?`,
  choices: ["Sending a package", "exiting the system"],
};
const senderQuestions = [
  {
    type: "input",
    name: "senderName",
    message: "Enter your full name:",
  },
  {
    type: "input",
    name: "senderAddress",
    message: "Enter your address:",
  },
  {
    type: "input",
    name: "senderPhoneNumber",
    message: "Enter your phone number:",
    validate: function (input) {
      const phoneRegex = /^\d{10}$/;
      return phoneRegex.test(input)
        ? true
        : "Please enter a valid 10-digit phone number";
    },
  },
  {
    type: "input",
    name: "senderEmail",
    message: "Enter your email address:",
    default: "user@example.com",
    validate: function (input) {
      const emailRegex = /\S+@\S+\.\S+/;
      return emailRegex.test(input)
        ? true
        : "Please enter a valid email address";
    },
  },
  {
    type: "input",
    name: "packageWeight",
    message: "Enter the total weight of your package in kg:",
    validate:function (input) {
      return !isNaN(input)
        ? true
        : "Please enter a valid number";
    },
  },
];
const recipientQuestions = [
  {
    type: "input",
    name: "recipientName",
    message: "Enter the recipient's full name:",
  },
  {
    type: "input",
    name: "recipientAddress",
    message: "Enter the recipient's address:",
  },
  {
    type: "input",
    name: "recipientPhoneNumber",
    message: "Enter the recipient's phone number:",
    validate: function (input) {
      const phoneRegex = /^\d{10}$/;
      return phoneRegex.test(input)
        ? true
        : "Please enter a valid 10-digit phone number";
    },
  },
  {
    type: "input",
    name: "recipientEmail",
    message: "Enter the recipient's email address:",
    default: "user@example.com",
    validate: function (input) {
      const emailRegex = /\S+@\S+\.\S+/;
      return emailRegex.test(input)
        ? true
        : "Please enter a valid email address";
    },
  },
];
const continueOperation = [
  {
    type: "confirm",
    name: "continue",
    message: "Do you want to perform another operation?",
    default: true,
  },
];

async function login() {
  let tries = 1;

  while (tries <= 3) {
    const credentials = await inquirer.prompt(askCredentials);
    const user = users.find(
      (student) =>
        student.username === credentials.username &&
        student.password === credentials.password
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
async function showMenu() {
  const optionMenu = await inquirer.prompt(askMenu);
  if (optionMenu.options === "Sending a package") {
    await sendPackage();
  } else {
    return;
  }
}
async function sendPackage() {
  console.log(
    `
Please provide the sender's information to proceed with the package shipment.
    `
  );
  const senderData = await inquirer.prompt(senderQuestions);
  console.log(
    `
Please provide the recipient's information to proceed with the package shipment.
    `
  );
  
  const recipientData = await inquirer.prompt(recipientQuestions);
  const price = await calculatePrice(senderData.packageWeight);
  const numberPackage = await generateRandomNumber();
  console.log(`Package sent successfully!`);
  console.log(`Package Number: ${numberPackage}`);
  console.log(`Shipping Price: $${price.toFixed(2)}`);
  console.log("Sender: " + senderData.senderName);
  console.log(`Sender Address: ${senderData.senderAddress}`);
  console.log("Recipient: " + recipientData.recipientName);
  console.log(`Recipient Address: ${recipientData.recipientAddress}`)
  console.log("");
  const userWantsToContinue = await inquirer.prompt(continueOperation)
  if (userWantsToContinue.continue) {
    await showMenu()
    
  }
}
async function generateRandomNumber() {
  return Math.floor(Math.random() * 1000);
}

async function calculatePrice(kg) {
  return Number(kg) * 2;
}
async function main() {
  const loggedIn = await login();
  if (loggedIn) {
    await showMenu();
  }
  console.log("Thank you for using our system! See you soon.");
}
main();
