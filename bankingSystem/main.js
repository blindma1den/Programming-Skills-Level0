

let isAuthenticated = false;
let wrongCredentials= 3;

let users = JSON.parse(localStorage.getItem('users')) || [];

function saveUsersToLocalStorage() {
    localStorage.setItem('users', JSON.stringify(users));
}

function createAccount (){
    const newUsername = document.getElementById('newUsername').value;
    const newPassword = document.getElementById('newPassword').value;

    if(users.some(u => u.username === newUsername)){
        alert('nombre de usuario en uso')
        return
    }
    const newUser={
        username: newUsername,
        password:newPassword,
        balance:2000
    }
    users.push(newUser)
    saveUsersToLocalStorage();
    alert('account created')
    Account(); 
    console.log(newUser)

}
function login() {
    const username = document.getElementById('username').value
    const  password= document.getElementById('password').value
     const user= users.find(u => u.username === username && u.password === password);
 
     if (user){
        isAuthenticated = true;
        Account();  
        window.location.hash = '#Account';
        wrongCredentials=3;
     }
     else {
        // Si no está autenticado, redirige al usuario a la página de inicio de sesión
        window.location.hash = '#login';
        wrongCredentials--;
        document.getElementById('messageError').style.display = 'block';
        document.getElementById('messageError').innerHTML=`Incorrect credentials you have ${wrongCredentials} more attempts.`
        
        
        if(wrongCredentials > 0){
            document.getElementById('messageError').style.display = 'block';
            document.getElementById('messageError').innerHTML=`Incorrect credentials you have ${wrongCredentials} more attempts.`
        }else{
            blockAccount();
            document.getElementById('messageError').innerHTML='Oops, your account is temporarily out of service because you failed 3 times in your credentials.'
        }
        
    }
    
}

function singUp (){
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('singUp').style.display = 'grid';

}
function LoginHere (){
    document.getElementById('login-container').style.display = 'grid';
    document.getElementById('singUp').style.display = 'none';

}

function Account() {
    const  username = document.getElementById('username').value
    const  password= document.getElementById('password').value
    const user= users.find(u => u.username === username && u.password === password);
    
    if (isAuthenticated) {
        document.getElementById('login-container').style.display = 'none';
        document.getElementById('Account-container').style.display = 'block';
        document.getElementById('user').innerHTML='Hola,' + ' ' + username.toUpperCase()
        document.getElementById('balance').innerHTML='$ ' + user.balance.toLocaleString('en')

    } else {
        // Si no está autenticado, redirige al usuario a la página de inicio de sesión
        window.location.hash = '#login';
      
    }
}

// Resto de tus funciones...

// Agrega esta función para ocultar elementos cuando el usuario se desconecta
function logout() {
    isAuthenticated = false;
    document.getElementById('Account-container').style.display = 'none';
    document.getElementById('login-container').style.display = 'block';
    window.location.hash = '#login';
    window.readload
}

function blockAccount (){
    document.getElementById('username').disabled = true;
    document.getElementById('password').disabled = true;
    setTimeout(() => {
        document.getElementById('username').disabled = false;
        document.getElementById('password').disabled = false;
        wrongCredentials=3;
        document.getElementById('messageError').innerHTML=`you have ${wrongCredentials} attempts.`


      }, 10000);
}

function transaction (){
    const username = document.getElementById('username').value;
    const To = document.getElementById('usernameTo').value;
    const Monto = parseFloat(document.getElementById('monto').value);    
    
    const userFrom= users.find(u => u.username === username);
    const userTo = users.find(u => u.username === To );

    if(userFrom.balance < Monto){
        alert('Insufficient funds')
        return false;
    } 
    userFrom.balance -= Monto;
    userTo.balance += Monto;
    alert('transaction successful')
    return true;

    
}

function toDeposit (){
    const username = document.getElementById('usernameDeposit').value;
    const Monto = parseFloat(document.getElementById('montoDeposit').value); 
    const user= users.find(u => u.username === username);

    if (!user) {
        alert('User not found');
        return false;
    }
    user.balance += Monto;
    alert('transaction successful')
    return true;

}
function toWithdraw (){
    const username = document.getElementById('usernameWithdraw').value;
    const Monto = parseFloat(document.getElementById('montoWithdraw').value); 
    const user= users.find(u => u.username === username);

    if(user.balance < Monto){
        alert('Insufficient funds')
        return false;
    } 
    if (!user) {
        alert('User not found');
        return false;
    }
    user.balance -= Monto;
    alert('transaction successful')
    return true;

}