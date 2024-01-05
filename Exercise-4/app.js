// 4. Create an online shipping system with the following features:
// * 		The system has a login that locks after the third failed attempt.
// * 		Display a menu that allows: Sending a package, exiting the system.
// * 		To send a package, sender and recipient details are required.
// * 		The system assigns a random package number to each sent package.
// * 		The system calculates the shipping price. $2 per kg.
// * 		The user must input the total weight of their package, and the system should display the amount to pay.
// * 		The system should ask if the user wants to perform another operation.
// If the answer is yes, it should return to the main menu. If it's no, it should close the system.

/*
Sistema de login con 3 intentos
Menu: enviar paquete y logout
Para enviar un paquete: sender, recipient details
El sistema asigna un id random para cada paquete
El precio del KG es de $2 y calcula el precio total del paquete
El usuario debe poner cuanto pesa el paquete y le dira cuanto valio vrg
El sistema te pregunta si querés hacer algo mas. Si es si, vuelve al menu principal, sino logout (prompt)

HTML: LOGIN - FORM CON SENDER Y RECIPIENT: Full Name, Address, City, Country, Postal Code, Phone, Email. Package Weight.
Button to calculate shipping cost, and send package
*/

const loginForm = document.querySelector('.form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const shippingSection = document.getElementById('shipping-section');
const senderNameInput = document.getElementById('senderName');
const senderPhoneInput = document.getElementById('senderPhone');
const recipientNameInput = document.getElementById('recipientName');
const recipientPhoneInput = document.getElementById('recipientPhone');
const recipientAddressInput = document.getElementById('recipientAddress');
const recipientCityInput = document.getElementById('recipientCity');
const recipientCountryInput = document.getElementById('recipientCountry');
const packageDescriptionInput = document.getElementById('packageDescription');
const packageWeightInput = document.getElementById('packageWeight');
const calculateButton = document.getElementById('calculate-button');
const sendButton = document.getElementById('send-button');

let wrongPasswordTimes = 0;
let currentUser;
const maxWrongAttempts = 3;
let users = [];
let orders = [];
//Fetching user list from users.json
fetch('./users.json')
  .then((response) => response.json())
  .then((data) => {
    users = data;
  })
  .catch((error) => console.log(error));

//Authenticate Function with lock at third wrong try
const authenticate = () => {
  let username = usernameInput.value;
  let password = passwordInput.value;

  currentUser = users.find((user) => user.username === username);

  if (!currentUser) {
    console.log('Invalid username or password.');
    return false;
  }
  if (currentUser.isLocked) {
    console.log('User is locked.');
    return false;
  }

  if (username === currentUser.username && password === currentUser.password) {
    console.log('Authentication successful.');
    showOperations();
    return true;
  } else {
    wrongPasswordTimes = wrongPasswordTimes + 1;
    console.log('Invalid username or password.');
    console.log(`Attempts remaining: ${maxWrongAttempts - wrongPasswordTimes}`);

    if (wrongPasswordTimes >= maxWrongAttempts) {
      currentUser.isLocked = true;
      console.log(
        'You have exceeded the number of tries. Please try again later.'
      );
      return false;
    }
  }
};
//Handle Submit form function to authenticate user
const handleFormSubmit = (e) => {
  e.preventDefault();
  authenticate();
};

//Hide and unhide operation if logged
const showOperations = () => {
  loginForm.style.display = 'none';
  shippingSection.style.display = 'flex';
};
const calculateShipping = (weight) => {
  return weight * 2;
};
const calculateShippingCost = () => {
  const weight = parseFloat(packageWeightInput.value);
  const shippingCost = calculateShipping(weight);
  console.log(`$${shippingCost.toFixed(2)}`);
};

const sendOrder = () => {
  const senderName = senderNameInput.value;
  const senderPhone = senderPhoneInput.value;

  const recipientName = recipientNameInput.value;
  const recipientPhone = recipientPhoneInput.value;
  const recipientAddress = recipientAddressInput.value;
  const recipientCity = recipientCityInput.value;
  const recipientCountry = recipientCountryInput.value;

  const packageDescription = packageDescriptionInput.value;
  const packageweight = parseFloat(packageWeightInput.value);
  const shippingCost = calculateShipping(packageweight);
  const orderId = Math.floor(Math.random() * 10000000);

  const order = {
    orderId,
    senderName,
    senderPhone,
    recipientName,
    recipientPhone,
    recipientAddress,
    recipientCity,
    recipientCountry,
    packageDescription,
    packageweight,
    shippingCost,
  };
  orders.push(order);
  let newOrder = prompt(
    'If you want to make a new order, press 1. If you want to see your orders, and exit press 2'
  );
  if (newOrder === '1') {
    console.log('Please make another order');
  } else if (newOrder === '2') {
    console.log('Orders:', orders);
    console.log(
      'in 10 seconds your will be logged out. Thanks for your orders'
    );
    setTimeout(logout, 10000);
  } else {
    console.log('Invalid input');
  }
};

//Function to logout
const logout = (e) => {
  e.preventDefault();
  currentUser = null;
  loginForm.style.display = 'block';
  shippingSection.style.display = 'none';

  console.log('Logged out.');
};

//Handle Submit form function to send Order
const handleSendOrder = (e) => {
  e.preventDefault();
  sendOrder();
};

//Listening buttons events
loginForm.addEventListener('submit', handleFormSubmit);
calculateButton.addEventListener('click', calculateShippingCost);
sendButton.addEventListener('click', handleSendOrder);
logoutButton.addEventListener('click', logout);
