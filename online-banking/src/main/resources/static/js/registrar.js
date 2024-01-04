// Call the dataTables jQuery plugin

$(document).ready(function() {



});

function getHeaders(){
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': localStorage.token
    }

}

async function registrarUsuarios() {

    let datos = {};


    datos.nombre = document.getElementById('txtNombre').value;
    datos.apellido = document.getElementById('txtApellido').value;
    datos.email = document.getElementById('txtEmail').value;
    datos.password = document.getElementById('txtPassword').value;

    let repetirPassword = document.getElementById('txtRepeatPassword').value;

    if(repetirPassword !== datos.password) {
        alert('La contrasenna no coincide');
        return;
    }

    const request = await fetch('api/usuarios', {
        method: 'POST',
        headers: getHeaders(),

       body: JSON.stringify(datos)

    }
    );
    const text = await request.text();

    if (text === 'email duplicado') {
        alert("Este email ya existe")
    } else {
        alert("La cuenta fue creada con exito");
         window.location.href = 'login.html'
    }


}

