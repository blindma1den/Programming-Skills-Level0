console.log('hola desde el js')
const login=document.getElementById("login");
login.addEventListener("submit",e=>{
    e.preventDefault();
    const data={
        username:document.getElementById("username").value,
        password:document.getElementById('password').value
    }
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
    if(typeof data==="string"){
        alert(data)
    }else if (typeof data ==="object"){
        window.location.href=`/menu/${data.id}`
    }
}).catch(error=>{
    console.error('Error',error)
})
    
})