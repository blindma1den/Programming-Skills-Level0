// 2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
// * 		The user must choose their initial currency and the currency they want to exchange to.
// * 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw,
// it should return to the main menu.
// * 		If the user decides to withdraw the funds, the system will charge a 1% commission.
// * 		Set a minimum and maximum amount for each currency, it can be of your choice.
// * 		The system should ask the user if they want to perform another operation.
// If they choose to do so, it should restart the process; otherwise, the system should close.

//FROM EXERCISE 1
//Capture DOM elements
const loginForm = document.querySelector('.form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

const operations = document.getElementById('operations-container');
const balanceButton = document.getElementById('balance-button');

//Create some initial variables
let wrongPasswordTimes = 0;
let currentUser;
const maxWrongAttempts = 3;
let users = [];

//Fetching user list from users.json
fetch('./users.json')
  .then((response) => response.json())
  .then((data) => {
    users = data;
  })
  .catch((error) => console.log(error));

//Balance Function
const balanceOperation = () => {
  console.log(
    `Hi ${currentUser.username}! In your account ${
      currentUser.accountId
    }, your current balance is: ${JSON.stringify(currentUser.balance)}`
  );
};

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
  operations.style.display = 'block';
};

//Listening buttons events
loginForm.addEventListener('submit', handleFormSubmit);

balanceButton.addEventListener('click', (e) => {
  e.preventDefault();
  balanceOperation();
});

// EXERCISE 2

//Declare some variables
const apiKey = '55929cc551cb462692302e3ce47171f4';
const converterButton = document.getElementById('converter-button');
const comission = 0.99; //amount *0.99 = 1% (it's an alternative way i use frecuently in my job)
let amountInTargetCurrency;
let amountWithComission;
//Listen Click event in Converter Button
converterButton.addEventListener('click', () => {
  const amountInput = document.getElementById('converter-input').value;
  const fromCurrencySelect = document.getElementById('converter-from-select');
  const toCurrencySelect = document.getElementById('converter-to-select');
  let baseCurrency = fromCurrencySelect.value;
  let targetCurrency = toCurrencySelect.value;

  const apiUrl = `https://open.er-api.com/v6/latest/${baseCurrency}?apikey=${apiKey}`;

  //Fetching api to convert currencies
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      const exchangeRates = data.rates;
      const conversionRate = exchangeRates[targetCurrency];
      //Check if have enough funds
      if (amountInput > currentUser.balance[baseCurrency])
        console.log('Insufficient funds');
      else if (targetCurrency === baseCurrency) {
        console.log('You cannot exchange to the same currency');
      } else {
        //Convert currencies and logic
        let amountInBaseCurrency = amountInput;
        console.log(amountInBaseCurrency);
        amountInTargetCurrency = amountInBaseCurrency * conversionRate;
        amountWithComission = amountInTargetCurrency * comission;
        currentUser.balance[baseCurrency] -= amountInput;
        currentUser.balance[targetCurrency] += amountInTargetCurrency;
        console.log(
          `${amountInBaseCurrency} ${baseCurrency} are now converted in ${amountInTargetCurrency} ${targetCurrency}\nIf you want to withdraw, the comission is (1%) `
        );
        withdrawConvertButton.style.display = 'block';
      }
    })
    .catch((error) => console.error('Error getting exchange rates:', error));

  //capturing Withdraw convert button and listening click event
  const withdrawConvertButton = document.getElementById('withdraw-converted');
  withdrawConvertButton.addEventListener('click', (e) => {
    e.preventDefault();
    currentUser.balance[targetCurrency] -= amountInTargetCurrency;
    amountWithComission = amountInTargetCurrency * comission;
    console.log(
      `
      You has withdrawn ${amountWithComission} ${targetCurrency}\n
      You can see your actual balance clicking in Balance Button
        `
    );

    console.log(currentUser);
    withdrawConvertButton.style.display = 'none';
  });
});
