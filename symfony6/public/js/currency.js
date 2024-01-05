
function getHeaders(){
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',

    }

}

$(document).ready(function() {

    let moneda1 = '';
    let moneda2 = '';

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

 function convertir() {

     let valorInicial = document.getElementById('valor1').value;

     var select1 = document.getElementById('moneda1');
     select1.addEventListener("click", () => {
         select1.addEventListener("change",
             function(){
             console.log("moneda1 seleccionada"+ this.options[select1.selectedIndex].text)
                 moneda1 = this.options[select1.selectedIndex].text;
                 console.log(moneda1);
             })});
     let select2 = document.getElementById('moneda2');
     select2.addEventListener("click", () => {
         select2.addEventListener('change',
             function () {
                 console.log("moneda2 seleccionada"+this.options[select2.selectedIndex].value)
                 moneda2 = this.options[select2.selectedIndex].value;
                 console.log(moneda2);
             });
     });
     console.log("el valor de la moneda1 es :"+ moneda1);
     console.log("el valor de la moneda2 es :"+moneda2);
     let datos = {
         "moneda1": moneda1, "moneda2": moneda2,
         "valor": valorInicial
     };

     const request = fetch('api/change_money', {
             method: 'POST',
             headers: getHeaders(),
             body: JSON.stringify(datos),
             'Content-Type': 'application/json'
         }
     );
     const text = request.text();

     // alert("Deposito realizado con exito");
     // window.location.href = 'index.html'


 }

