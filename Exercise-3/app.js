const loginForm = document.querySelector('.form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const firstNameInput = document.getElementById('first-name');
const lastNameInput = document.getElementById('last-name');
const programSelect = document.getElementById('program-select');
const campusSelect = document.getElementById('campus-select');
const enrollment = document.getElementById('enrollment-container');
const enrollmentButton = document.getElementById('enrollment-button');
const logoutButton = document.getElementById('logout-button');

//Create some initial variables
let wrongPasswordTimes = 0;
let currentUser;
const maxWrongAttempts = 3;
let users = [];
let campus = [];
let campusSelected;
let programSelected;
let citiesWithAvailableSlots;

//Function to fetch
const fetchJson = async (url) => {
  try {
    const response = await fetch(url);
    const data = await response.json();

    if (data) {
      return data;
    }
  } catch (error) {
    console.log(error);
  }
};
//Check if data is stored in LS. If not, get data from fetching.
if (!localStorage.getItem('users') || !localStorage.getItem('campus')) {
  fetchJson('./users.json')
    .then((data) => {
      if (data) {
        users = data;
        console.log(users);
      }
    })
    .catch((error) => console.log(error));

  fetchJson('./campus.json')
    .then((data) => {
      if (data) {
        campus = data;
        console.log(campus);
      }
    })
    .catch((error) => console.log(error));
} else {
  users = JSON.parse(localStorage.getItem('users')) || [];
  campus = JSON.parse(localStorage.getItem('campus')) || [];
}

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
//Function to logout
const logout = (e) => {
  e.preventDefault();
  currentUser = null;
  loginForm.style.display = 'block';
  enrollment.style.display = 'none';
  firstNameInput.value = '';
  lastNameInput.value = '';
  console.log('Logged out.');
};
//function to find campus id.
const findById = (array, id) => {
  return array.find((element) => element.id === id);
};
//Function to store data from enrollment form into array and LocalStorage.
//Checking if user fill required data, if not already enrolled, and if slots are available
const enrollmentForm = () => {
  let firstName = firstNameInput.value;
  let lastName = lastNameInput.value;
  let campusValue = Number(campusSelect.value);
  let program = programSelect.value;
  let campusSelected = findById(campus, campusValue);

  if (currentUser.program !== '') {
    console.log('You are already enrolled.');
    return true;
  } else if (campusSelected.availableSlots > 0) {
    campusSelected.availableSlots -= 1;
    currentUser.firstName = firstName;
    currentUser.lastName = lastName;
    currentUser.program = program;
    currentUser.campus = campusSelected.city;

    localStorage.setItem('users', JSON.stringify(users));
    localStorage.setItem('campus', JSON.stringify(campus));
    console.log('You are enrolled, congratulations.');
  } else {
    citiesWithAvailableSlots = campus
      .filter((city) => city.availableSlots > 0)
      .map((city) => city.city);
    // If slots are full in the campus selected, we show another options in console.
    if (citiesWithAvailableSlots.length > 0) {
      console.log(
        'The program is full. Thanks for try to enroll. See you next year!'
      );
    } else showOtherOptions();
  }
};
//Function to show campus options with availability.
const showOtherOptions = () => {
  console.log(
    `There is not available spots.\nPlease try in ${JSON.stringify(
      citiesWithAvailableSlots
    )}`
  );
};

//Handle Submit form function to authenticate user
const handleFormSubmit = (e) => {
  e.preventDefault();
  authenticate();
};
const handleEnrollmentFormSubmit = (e) => {
  e.preventDefault();
  enrollmentForm();
};

//Hide and unhide operation if logged
const showOperations = () => {
  loginForm.style.display = 'none';
  enrollment.style.display = 'block';
};

//Listening buttons events
loginForm.addEventListener('submit', handleFormSubmit);
enrollmentButton.addEventListener('click', handleEnrollmentFormSubmit);
logoutButton.addEventListener('click', logout);
