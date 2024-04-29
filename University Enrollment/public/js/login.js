const form = document.getElementById("myform");
form.addEventListener("submit",e=>{
    e.preventDefault();
    const data={
        username:document.getElementById("username").value,
        password:document.getElementById('password').value
    }
    console.log(data);
    fetch('/login',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(response=>{
        const contentType=response.headers.get('Content-Type');
        if(contentType && contentType.includes('application/json')){
            return response.json();
        }else{
            return response.text();
        }
}).then(data=>{
    console.log(typeof data)
    if(typeof data ==="string"){
        alert(data);
    }else{
        console.log(data.inProgram)
        if(data.inProgram===true){
            window.location.href=`/program/${data.program}/${data.username}`
        }else{
            window.location.href=`/menu/${data.username}`
        }
        
    }
}).catch(error=>{
    console.error('Error',error)
})
})











const registerRequest=document.getElementById('register');
registerRequest.addEventListener('click',e=>{
    console.log('HOLA DESDE EL BOTON REGISTRASE')
    window.location="/register"
})