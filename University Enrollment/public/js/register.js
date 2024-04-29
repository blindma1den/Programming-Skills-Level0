console.log('hola desde el registro')
const register=document.getElementById("register");
register.addEventListener('submit',e=>{
    e.preventDefault();
    const data={
        name:document.getElementById('name').value,
        lastname:document.getElementById('lastname').value,
        username:document.getElementById('username').value,
        password:document.getElementById('password').value
    }
    fetch('/register',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(response=>{
        console.log(response)
    if(!response.ok){
        throw new Error('FAILED REQUEST')
    }
    return response.text()
}).then(data=>{
    if(data.includes("SUCCESSFULLY")){
        alert(data)
        window.location="/"
    }else{
        alert(data)
    }
}).catch(error=>{
    console.error('Error',error)
})
})
