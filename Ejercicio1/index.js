// 1. Create an online banking system with the following features:

// * Users must be able to log in with a username and password.
// * If the user enters the wrong credentials three times, the system must lock them out.
// * The initial balance in the bank account is $2000.
// * The system must allow users to deposit, withdraw, view, and transfer money.
// * The system must display a menu for users to perform transactions.=
let currentUser;
const usuario = document.getElementById("usuario");
const contrasena = document.getElementById("contrasena");
const submit = document.getElementById("submit");
const alerta = document.getElementById("alert");
const options = document.getElementById("options-section");
const formulario = document.getElementById("formulario");
const bienvenidaName = document.getElementById("bienvenida-username");
const balance = document.getElementById("balance");

const userDestinyInput = document.getElementById("user-destiny");
const depositAmount = document.getElementById("deposit-amount");
const withdrawAmount = document.getElementById("withdraw-amount");
const tranferAmount = document.getElementById("tranfer-amount");
const buttonDeposit = document.getElementById("button-deposit");
const buttonWithdraw = document.getElementById("button-withdraw");
const buttonTransfer = document.getElementById("button-transfer");
console.log(depositAmount);
submit.addEventListener("click", (e) => login(e));
buttonDeposit.addEventListener("click", () =>
  deposit(currentUser, parseInt(depositAmount.value))
);
buttonWithdraw.addEventListener("click", () =>
  withdraw(currentUser, parseInt(withdrawAmount.value))
);
buttonTransfer.addEventListener("click", () =>
  transfer(currentUser, userDestinyInput, parseInt(tranferAmount.value))
);

let intentos = 0;
const defaultUsers = [
  { nombre: "jayler", contrasena: "123456", balance: 2000 },
  { nombre: "Andres", contrasena: "contraseñaFuerte456", balance: 2000 },
  { nombre: "Camilo", contrasena: "secreto789", balance: 2000 },
  { nombre: "Santiago", contrasena: "protegido2022", balance: 2000 },
  { nombre: "Carlos", contrasena: "privado555", balance: 2000 },
];
console.log(usuario.value);
function updateBalanceDisplay() {
  balance.innerText = `$${currentUser.balance}`;
}
function login(e) {
  e.preventDefault();
  const usuarioEncontrado = defaultUsers.find(
    (user) =>
      user.nombre === usuario.value && user.contrasena === contrasena.value
  );
  if (usuarioEncontrado) {
    console.log("Inicio exitoso");
    options.style.display = "flex";
    formulario.style.display = "none";
    console.log(usuarioEncontrado.balance);
    bienvenidaName.innerText = `${usuarioEncontrado.nombre}`;
    currentUser = usuarioEncontrado;
    updateBalanceDisplay();
  } else {
    alerta.style.display = "block";

    intentos++;
  }
  if (intentos === 3) {
    alerta.innerText =
      "numero de intentos maximos excedidos de se bloquedo su ingreso";
    submit.disabled = true;
  }
}
function deposit(currentUser, amount) {
    console.log(amount);
  currentUser.balance += amount;
  alert(
    `se ha realizado el deposito de $${amount} correntamente`
  );
  depositAmount.value =""
  updateBalanceDisplay();
}
function withdraw(currentUser, amount) {
  if (currentUser.balance < amount) {
    alert("Fondos insuficientes");
  } else {
    currentUser.balance -= amount;
    alert(
      `se ha realizado el retiro de $${amount}`
    );
    withdrawAmount.value =""
    updateBalanceDisplay();
  }
}
function transfer(userOrigin, DestinyInput, amount) {
  console.log(`${userOrigin} ${DestinyInput.value} ${amount} `);
  const userDestiny = defaultUsers.find(
    (user) => user.nombre == DestinyInput.value
  );
  console.log(userDestiny);
  if (userOrigin && userDestiny) {
    if (userOrigin.balance >= amount && amount > 0) {
      userOrigin.balance -= amount;
      userDestiny.balance += amount;
      updateBalanceDisplay();

      console.log(
        `Transferencia de ${amount} de ${userOrigin.nombre} a ${userDestiny.nombre} realizada.`
      );
      console.log(
        `Nuevo balance de ${userOrigin.nombre}: ${userOrigin.balance}`
      );
      console.log(
        `Nuevo balance de ${userDestiny.name}: ${userDestiny.balance}`
      );
    } else if (amount < 0) {
      alert(`el valor para enviar debe ser positivo`);
    } else if (userOrigin.balance <= amount) {
      alert(`Saldo insuficiente para realizar la transferencia.`);
    }
  } else {
    alert(`Usuario de origen o destino no encontrado.`);
  }
  userDestinyInput.value = "";
  tranferAmount.value = "";
}
