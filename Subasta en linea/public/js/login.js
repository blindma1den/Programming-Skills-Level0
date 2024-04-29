console.log(" A VER SI SE ENVIA DESDE EL LOGIN.JS")
const registerButton=document.getElementById("register");
registerButton.addEventListener('click',e=>{
    e.preventDefault();
    console.log("hola hola hola")
    const register=document.getElementById("registerForm");
    const login=document.getElementById("form")
    login.style.display="none";
    register.style.display='block';
})

const register=document.getElementById("registerForm")
register.addEventListener("submit",(e)=>{
    e.preventDefault();
    console.log("hola estoy enviando el registro")
    data={
        username:document.getElementById("registerUsername").value,
        password:document.getElementById('registerPassword').value
    }

    fetch("/createUser",{
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    })
    .then(response=>{
    if(!response.ok){
        throw new Error('LA SOLICITUD FALLO')
    }
    return response.json()
}).then(data=>{
    if(data===true){
        alert("USUARIO CREADO CON EXITO,YA PUEDES INGRESAR");
        window.location.reload();
        
    }else if(data===false){
        alert('ESE USUARIO YA SE ENCUENTRA REGISTRADO,INTENTA CON OTRO')
    }
    console.log(data);
}).catch(error=>{
    console.error('Error',error)
});
})

const login=document.getElementById('form');
login.addEventListener('submit',e=>{
    e.preventDefault();
     data={
        username:document.getElementById('username').value,
        password:document.getElementById('password').value
    }
    fetch("/login",{
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    })
    .then(response=>{
    if(!response.ok){
        throw new Error('LA SOLICITUD FALLO')
    }
    return response.json()
}).then(data=>{
    console.log(data);
    if(typeof data ==='string'){
        alert(data)
    }else{
        alert('validando',data)
        window.location.href = "/currencyMenu/"+data.username;
    }

}).catch(error=>{
    console.error('Error',error)
});
})

/*
<div class="flex justify-center mt-8">
  <form id="exchangeForm" class="w-96 p-4 border border-gray-300 rounded shadow-lg">
    <h2 class="text-xl font-semibold mb-4">Intercambio de Divisas</h2>
    
    <!-- Selección de moneda a intercambiar -->
    <div>
      <label for="currency_from" class="block mb-2">Selecciona la moneda a intercambiar:</label>
      <select name="currency_from" id="currency_from" class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-400">
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        <option value="ARS">ARS</option>
        <option value="CPL">CPL</option>
        <option value="TRY">TRY</option>
        <option value="GBP">GBP</option>
        <!-- Agrega más opciones según necesites -->
      </select>
    </div>
    
    <!-- Cantidad a intercambiar -->
    <div class="mt-4">
      <label for="amount" class="block mb-2">Cantidad:</label>
      <input type="number" name="amount" id="amount" class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-400" placeholder="Cantidad a intercambiar">
    </div>
    
    <!-- Selección de moneda a recibir -->
    <div class="mt-4">
      <label for="currency_to" class="block mb-2">Selecciona la moneda a recibir:</label>
      <select name="currency_to" id="currency_to" class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-400">
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        <option value="ARS">ARS</option>
        <option value="CPL">CPL</option>
        <option value="TRY">TRY</option>
        <option value="GBP">GBP</option>
        <!-- Agrega más opciones según necesites -->
      </select>
    </div>

    <!-- Botón de enviar -->
    <div class="mt-6">
      <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:bg-blue-600">Enviar</button>
    </div>
  </form>
</div>*/
