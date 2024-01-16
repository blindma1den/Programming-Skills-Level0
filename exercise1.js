let tries = 3
let balance = 2000
let balance_2 = 2000 
let user1 = "admin"
let pass1 = "1234"
let user2 = "admin2"
let pass2 = "5678"

let bool1 = false
let bool2 = false


function login(){
   
    if((user1 == document.getElementById("user").value && pass1 == document.getElementById("pass").value)){
        alert("Correct Data. Access Granted.")
        document.getElementById('bank').hidden = false   
        bool1 = true  
        bool2 = false
        document.getElementById('p-1').innerHTML = "Balance: " + balance
        document.getElementById('p-1').hidden = true; 
        document.getElementById('deposit-section').hidden = true;
        document.getElementById('transfer-section').hidden = true;
        document.getElementById('withdraw-section').hidden = true;
        document.getElementById('console').innerHTML = ""
    }
    else if(user2 == document.getElementById("user").value && pass2 == document.getElementById("pass").value){
        alert("Correct Data. Access Granted.")
        document.getElementById('bank').hidden = false
        bool2 = true   
        bool1 = false 
        document.getElementById('p-1').innerHTML = "Balance: " + balance_2
        document.getElementById('p-1').hidden = true; 
        document.getElementById('deposit-section').hidden = true;
        document.getElementById('transfer-section').hidden = true;
        document.getElementById('withdraw-section').hidden = true;
        document.getElementById('console').innerHTML = ""
    }
    else{
        tries--
        alert("Wrong Data. " + tries + " tries left")
        if(tries == 0){
            alert("Access Denied.")
            location.href ='https://google.com';
        }
    }
}

function view(){
    document.getElementById('console').innerHTML = "Account view:"
    if(bool1){
        document.getElementById('p-1').innerHTML = "Balance: " + balance
    }
    else if(bool2){
        document.getElementById('p-1').innerHTML = "Balance: " + balance_2
    }
    document.getElementById('p-1').hidden = false; 
    document.getElementById('deposit-section').hidden = true; 
    document.getElementById('transfer-section').hidden = true;
    document.getElementById('withdraw-section').hidden = true; 
    document.getElementById('console-2').innerHTML = ""  
    
}

function deposit(){
    document.getElementById('console').innerHTML = "Deposit view:"
    document.getElementById('p-1').innerHTML = "Enter the amount to deposit in your account: " 
    document.getElementById('deposit-section').hidden = false; 
    document.getElementById('transfer-section').hidden = true;
    document.getElementById('withdraw-section').hidden = true; 
    document.getElementById('console-2').innerHTML = ""  
}

function rdeposit(){
    if(bool1 ){
        balance += parseInt(document.getElementById("deposit-input").value)          
    }
    else if(bool2 ){
        balance_2 += parseInt(document.getElementById("deposit-input").value)     
    } 
    document.getElementById('console-2').innerHTML = "Successful deposit."   
}

function transfer(){
    document.getElementById('console').innerHTML = "Transfer view:"
    document.getElementById('p-1').innerHTML = "Enter the amount to transfer from the other account: " 
    document.getElementById('deposit-section').hidden = true;
    document.getElementById('transfer-section').hidden = false;
    document.getElementById('withdraw-section').hidden = true;
    document.getElementById('console-2').innerHTML = ""        
}

function rtransfer(){
    if(bool1){
        balance_2 += parseInt(document.getElementById("transfer-input").value)
        balance -= parseInt(document.getElementById("transfer-input").value)            
    }
    else if(bool2){
        balance += parseInt(document.getElementById("transfer-input").value)   
        balance_2 -= parseInt(document.getElementById("transfer-input").value)      
    }
    document.getElementById('console-2').innerHTML = "Successful transfer."   
       
}

function withdraw(){
    document.getElementById('console').innerHTML = "Whitdraw view:"
    document.getElementById('p-1').innerHTML = "Enter the amount to witdraw from your account: " 
    document.getElementById('deposit-section').hidden = true;
    document.getElementById('transfer-section').hidden = true;
    document.getElementById('withdraw-section').hidden = false;      
    document.getElementById('console-2').innerHTML = ""  
}

function rwithdraw(){
    if(bool1 ){
        balance -= parseInt(document.getElementById("withdraw-input").value)          
    }
    else if(bool2 ){
        balance_2 -= parseInt(document.getElementById("withdraw-input").value)     
    }    
    document.getElementById('console-2').innerHTML = "Successful whitdraw."   
}

function exit(){
    alert('Thanks for using our services, have a nice day')
    document.getElementById('bank').hidden = true;  

}
