//Capture DOM elements
const loginForm = document.querySelector('.form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const operations = document.getElementById('operations-container');
const depositButton = document.getElementById('deposit-button');
const withdrawButton = document.getElementById('withdraw-button');
const balanceButton = document.getElementById('balance-button');
const transferButton = document.getElementById('transfer-button');
const depositInput = document.getElementById('deposit-input');
const withdrawInput = document.getElementById('withdraw-input');
const transferInput = document.getElementById('transfer-input');
const recipientInput = document.getElementById('transfer-recipient-input');

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

//Deposit Function
const depositOperation = () => {
  const depositAmount = parseFloat(depositInput.value);
  currentUser.balance += depositAmount;
  console.log(
    `You have deposited ${depositAmount}. Your new balance is ${currentUser.balance}.`
  );
  depositInput.value = '';
};
//Withdraw Function
const withdrawOperation = () => {
  const withdrawAmount = parseFloat(withdrawInput.value);
  if (withdrawAmount > currentUser.balance) {
    console.log('Insufficient funds');
    return;
  }
  currentUser.balance -= withdrawAmount;
  console.log(
    `You have withdrawn ${withdrawAmount}. Your new balance is ${currentUser.balance}.`
  );
  withdrawInput.value = '';
};
//Transfer Function
const transferOperation = () => {
  const transferAmount = parseFloat(transferInput.value);
  const recipient = recipientInput.value;
  const recipientUser = users.find((user) => user.accountId === recipient);
  if (!recipientUser) {
    console.log('Recipient not found');
    return;
  } else if (recipient === currentUser.accountId) {
    console.log('You cannot transfer money to yourself');
    return;
  } else if (transferAmount > currentUser.balance) {
    console.log('Insufficient funds');
    return;
  } else {
    currentUser.balance -= transferAmount;
    recipientUser.balance += transferAmount;
    console.log(
      `You have transferred from account ${currentUser.accountId} the amount of: ${transferAmount} to: ${recipientUser.username} in account Id: ${recipientUser.accountId}`
    );
    transferInput.value = '';
    recipientInput.value = '';
  }
};
//Balance Function
const balanceOperation = () => {
  console.log(
    `Hi ${currentUser.username}! In your account ${currentUser.accountId}, your current balance is: ${currentUser.balance}`
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

depositButton.addEventListener('click', (e) => {
  e.preventDefault();
  depositOperation();
});
withdrawButton.addEventListener('click', (e) => {
  e.preventDefault();
  withdrawOperation();
});
transferButton.addEventListener('click', (e) => {
  e.preventDefault();
  transferOperation();
});

balanceButton.addEventListener('click', (e) => {
  e.preventDefault();
  balanceOperation();
});
