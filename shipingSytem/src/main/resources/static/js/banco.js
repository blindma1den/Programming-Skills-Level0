// Call the dataTables jQuery plugin


function getHeaders(){
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

}


 function sendPackage() {

     let sender = document.getElementById('sender').value;
     let recipient = document.getElementById('recipient').value;
     let cantKG = document.getElementById('weight').value;
     let numberPackage = this.asignNumberPackage();
     let price = this.calculatePrice();

     if (sender === '' || recipient === '') {
         alert("Llene estos campos,son obligatorios!")
         return;
     }

     let respuesta = confirm("El precio del paquete de numero:" + numberPackage + "es de:" + price + ".Desea realizar otra operacion?")

     if (respuesta){
         alert("Perfecto, ya puede hacer otra operacion");
 }
     else{
         alert("Hasta pronto");
         window.location.href = 'login.html'
     }


}

function calculatePrice() {

    let cantKG = document.getElementById('weight').value;

    let price = cantKG * 2;

    return "$" + price;
}

function asignNumberPackage() {
    return Math.random();
}



$(document).ready(function() {



});