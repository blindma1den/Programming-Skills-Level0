// Call the dataTables jQuery plugin


function getHeaders(){
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': localStorage.token
    }

}
async function depositar() {

  //  datos.monto = document.getElementById('monto').value;
   // datos.usuarioEmail = localStorage.email;

    let datos = {"monto": String(document.getElementById('monto').value),
        "email": localStorage.email};

    const request = await fetch('api/deposit', {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(datos),
            'Content-Type': 'application/json'
        }
    );
    const text = await request.text();

        alert("Deposito realizado con exito");
        window.location.href = 'index.html'



}

async function extraer() {


    let datosE = {"monto": String(document.getElementById('monto').value),
        "email": localStorage.email};

    const request = await fetch('api/withdraw', {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(datosE),
            'Content-Type': 'application/json'
        }
    );
    const text = await request.text();

    if (text === "ok") {
        alert("Extraccion realizado con exito");
        window.location.href = 'index.html'
    }
    else{
        alert("Extraccion no realizada");
    }


}

async function transferir() {


    let datosT = {
        "monto": String(document.getElementById('monto').value),
        "email": localStorage.email, "emailUsuarioDestino": String(document.getElementById('usuario').value)
    };

    const request = await fetch('api/transfer', {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(datosT),
            'Content-Type': 'application/json'
        }
    );
    const text = await request.text();

    if (text === "ok") {
        alert("Transferencia realizado con exito");
        window.location.href = 'index.html'
    } else {
        alert("Usted no cuenta con saldo para realizar transferencias");
    }
}

    async function verSaldo() {


        let datosT = {
            "email": localStorage.email
        };

        const request = await fetch('api/view?' + new URLSearchParams({
            email : datosT.email
        })
        );
        const text = await request.text();
        document.getElementById("saldoActual").innerHTML = '$'+ text;
    }



$(document).ready(function() {

    verSaldo();

});