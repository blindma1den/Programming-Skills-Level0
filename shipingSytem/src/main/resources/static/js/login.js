

$(document).ready(function() {



});

let intentosLogin = 0;
async function iniciarSesion() {

    let datos = {};

    datos.email = document.getElementById('txtEmail').value;
    datos.password = document.getElementById('txtPassword').value;

    console.log("Numero de intentos fallidos:"+ intentosLogin);

    const request = await fetch('api/login', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    });
    const respuesta = await request.text();

    console.log(respuesta)
    if(respuesta !== 'Fail'){
        localStorage.email = datos.email;
        window.location.href = 'usuarios.html'

    }
    else if((respuesta === 'Usuario bloqueado')){
        alert('Su usuario se encuentra bloqueado.Contacte al admin')
    }
    else {
        alert('Credenciales incorrectas')
        intentosLogin = intentosLogin + 1;
        localStorage.intentos = intentosLogin;

        if (localStorage.intentos === 3 || intentosLogin === 3) {
            const request = await fetch('api/blockUser', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });
        }
    }


}

