// 2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
// 		The user must choose their initial currency and the currency they want to exchange to.
// 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
// 		If the user decides to withdraw the funds, the system will charge a 1% commission.
// 		Set a minimum and maximum amount for each currency, it can be of your choice.
// 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.
import inquirer from "inquirer";
const minAmount = 10;
const maxAmount = 9000;
let originCurrency;
let Destinationcurrency;
let amount;
const conversiones = {
  USD: 1,
  EUR: 0.91,
  ARS: 808.47,
  CLP: 888.94,
  TRY: 29.81,
  GBP: 0.79,
};
function convert(originCurrency, Destinationcurrency, amount) {
  const originToUsd = (amount / conversiones[originCurrency]);
  const converteValue = (originToUsd * conversiones[Destinationcurrency]).toFixed(3);
  const commission = (getCommission(converteValue)).toFixed(3);
  const finalValue = (converteValue - commission).toFixed(3);
  return { converteValue, commission, finalValue };
}
function getCommission(amount) {
  return amount * 0.01;
}
const opcionesIniciales = [
  { name: "USD" },
  { name: "EUR" },
  { name: "ARS" },
  { name: "CLP" },
  { name: "TRY" },
  { name: "GBP" },
];

const preguntaMonedaOrigen = {
  type: "list",
  name: "originCurrency",
  message: "Selecciona la moneda de origen:",
  choices: opcionesIniciales,
};
const preguntaMonedaDestino = (originCurrency) => ({
  type: "list",
  name: "destinationcurrency",
  message: "Selecciona la moneda de destino:",
  choices: opcionesIniciales.filter((opcion) => opcion.name != originCurrency),
});
const preguntaCantidad = {
  type: "input",
  name: "amount",
  message: "Ingrese la cantidad de dinero:",
  validate: function (input) {
    const value = parseFloat(input);
    if (isNaN(value) || value <= 0) {
      return "Ingrese un número válido y mayor que cero.";
    } else if (value < minAmount || value > maxAmount) {
      return `Ingrese un valor entre ${minAmount} y ${maxAmount}.`;
    }
    return true;
  },
};

const preguntaConfirmacionTransaccion = {
  type: "confirm",
  name: "decision",
  message: "¿Estás seguro de realizar la transacción?",
  default: false,
};
const preguntarContinuacion = {
  type: "confirm",
  name: "decision",
  message: "¿Deseas realizar otra transaccion?",
  default: false,
};
function iniciarTransaccion() {
  inquirer
  .prompt(preguntaMonedaOrigen)
  .then((respuesta) => {
    originCurrency = respuesta.originCurrency;
    return inquirer.prompt(preguntaMonedaDestino(originCurrency));
  })
  .then((respuesta) => {
    Destinationcurrency = respuesta.destinationcurrency;
    return inquirer.prompt(preguntaCantidad);
  })
  .then((respuesta) => {
    amount = respuesta.amount;
    if (amount < maxAmount && amount < maxAmount) {
    }
    return convert(originCurrency, Destinationcurrency, amount);
  })
  .then((respuesta) => {
    console.log("Cuota por transacción del 1%");
    console.log(`Monto inicial: ${amount} ${originCurrency}`);
    console.log(`Monto después de la conversión: ${respuesta.converteValue} ${Destinationcurrency}`);
    console.log(`Monto final después de la comisión: ${respuesta.finalValue} ${Destinationcurrency}`);
    return inquirer.prompt(preguntaConfirmacionTransaccion);
  })
  .then((respuesta) => {
    if (respuesta.decision) {
      console.log("Transacción realizada con éxito.");
      return inquirer.prompt(preguntarContinuacion);
      
    }else{
        return iniciarTransaccion() 

    }
  })
  .then((respuesta) => {
    if (respuesta && respuesta.decision) {
      iniciarTransaccion() 
    }else{
      console.log("Gracias por usar nuestro servicio. ¡Hasta luego!");
    }
  })
  .catch((error) => {
    console.error("Error:", error);
  });
  
}
console.log("¡Bienvenido a la Aplicación de Conversión de Monedas!");
console.log("--------------------------------------------------");
iniciarTransaccion()

