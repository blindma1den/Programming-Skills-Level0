/*
    1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.
*/
let username = 'usuario';
let password = '1234'
let int = 3;
let balance = 2000;

function login(){
    //username = usuario
    user = prompt('Por favor, ingresa tu username: ');
    pass = prompt('Ingrese su contraseña')

    if(user == username && pass === password){
        menu()
    }else if(user === "" || pass === ""){
        alert("No dejar campos vacios")
        login()
    }else{
        if(int > 1 ){
            alert('Usuario o Contraseña incorrecta. Quedan ' + int-- + " intentos")
            login()
        }else if(int === 1){
            alert('Usuario o Contraseña incorrecta. Ultimo intento')
            int--;
            login()
        }else{
            alert("SU CUENTA HA SIDO BLOOQUEDA")
        }
    }
}

function menu(){
    let options = prompt('Elije el numero correspondiente a la operacion que deseas realizar:\n 1.- Deposito\n 2. Retiro\n 3. Consulta\n 4. Transferencia\n 5. Salir del sistema')

    if(options === "1"){
        deposit()
    }else if(options === "2"){
        withdraw()
    }else if(options === "3"){
        view();
    }else if(options === "4"){
        transfer();
    }else{
        alert("GRACIAS POR SU PREFERENCIA. VUELVA PRONTO")
    }
}


function deposit(){
    let amount = prompt("Por favor ingrese el  monto a depositar: ")
    balance +=  Number(amount);

    let Dconfirm = confirm("Usted ha depositado: $" + amount + "\nSu saldo es: $" + balance + "\n\nDesea realizar otra operacion?")
    if(Dconfirm === true){
        menu();
    }else{
        alert("GRACIAS POR SU PREFERENCIA. VUELVA PRONTO")
    }
}

function withdraw(){
    let withdrawamount = prompt("Ingrese monto a retirar:")
    Number(withdrawamount);

    if(withdrawamount > balance ){
        let Wconfirm = confirm("Disculpe FONDOS INSUFICIENTES\nDesea realizar otra operacion?")
        if(Wconfirm === true){
            menu();
        }else{
            alert("GRACIAS POR SU PREFERENCIA. VUELVA PRONTO")
        }
    }else if(withdrawamount <= balance){
        balance -= withdrawamount
        let Wconfirm = confirm("Usted ha retirado: $" + withdrawamount + "\nSu balance es: $" + balance + "\n\n Desea realizar otra operacion?")
        if(Wconfirm === true){
            menu();
        }else{
            alert("GRACIAS POR SU PREFERENCIA. VUELVA PRONTO")
        }
    }

}

function transfer(){
    let transferamount = prompt("Ingresar el monto a transferir:")
    Number(transferamount);

    if(transferamount > balance){
        let Tconfirm = confirm("DISCULPE FONDOS INSUFICIENTES\nDesea realizar otra operacion?");
        if(Tconfirm === true){
            menu();
        }else{
            alert("GRACIAS POR SU PREFERENCIA. VUELVA PRONTO")
        }
    }else if(transferamount <= balance){
        balance -= transferamount;
        let Tconfirm = confirm("Usted ha transferido: $" + transferamount + "\nSu balance es: $" + balance + "\n\n Desea realizar otra operacion?")
        if(Tconfirm === true){
            menu();
        }else{
            alert("GRACIAS POR SU PREFERENCIA. VUELVA PRONTO")
        }
    }
}

function view(){
    let Vconfirm = confirm("Su balance es: $" + balance+ "\n\n Desea realizar otra operacion?");
    if(Vconfirm === true){
        menu();
    }else{
        alert("GRACIAS POR SU PREFERENCIA. VUELVA PRONTO")
    }
}

login()
