
function getHeaders(){
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',

    }

}
let moneda1 = '';
let moneda2 = '';

$(document).ready(function() {

    var select1 = document.getElementById('moneda1');
    select1.addEventListener("click", () => {
        select1.addEventListener("change",
            function(){
                moneda1 = this.options[select1.selectedIndex].value;
                console.log(moneda1);
            })});
    let select2 = document.getElementById('moneda2');
    select2.addEventListener("click", () => {
        select2.addEventListener('change',
            function () {
                moneda2 = this.options[select2.selectedIndex].value;
                console.log(moneda2);
            });
    });
});

 async function convertir() {

     let valorInicial = document.getElementById('valor1').value;
     document.getElementById('valor2').value = 0;
     console.log("el valor de la moneda1 es :" + moneda1);
     console.log("el valor de la moneda2 es :" + moneda2);
     let datos = {
         "moneda1": moneda1, "moneda2": moneda2,
         "valor": valorInicial
     };

     const request = await fetch('api/change_money', {
             method: 'POST',
             headers: getHeaders(),
             body: JSON.stringify(datos),
             'Content-Type': 'application/json'
         }
     );
     const text = await request.text();
     document.getElementById('valor2').value = text;

 }

 async function extraer() {
     let valorInicial = document.getElementById('valor1').value;
     let valorExtraccion = document.getElementById('valor2').value;
     document.getElementById('valor2').value = 0;
     let datos = {
         "valor": valorInicial
     };
     const request = await fetch('api/discount', {
             method: 'POST',
             headers: getHeaders(),
             body: JSON.stringify(datos),
             'Content-Type': 'application/json'
         }
     );
     const text = await request.text();
     document.getElementById('valor2').value = text;

     var respuesta = confirm("Usted extrajo:"+text+moneda2 +'/n'+"Desea realizar otra operacion.")

     if(respuesta)
         alert("Usted aceptó.");
     else
         alert("Usted no aceptó.");
         window.location.reload();
 }

