const form =document.getElementById('form');
console.log(username)
form.addEventListener("submit",e=>{
    e.preventDefault();
    console.log("hola desde el form")
    const programs=document.getElementsByName("program");
    let program=""
    programs.forEach(element => {
        if(element.checked){
            program=element.value
        }
    });
    let campus=""
    const campuses=document.getElementsByName('campus');
    campuses.forEach(element=>{
        if(element.checked){
            campus=element.value
        }
    })
    console.log(campus)
    const data={
        name:document.getElementById('name').value,
        lastname:document.getElementById('lastname').value,
        campus:campus,
        program:program,
        username:username
    }
    console.log(data);
    fetch('/menu/registerProgram',{
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
    console.log(data);
    if(data.campus){
        alert(`${data.message} ${data.campus.join("or")}`)
        console.log("a")
    }
    else{
        console.log("b")
        console.log()
        alert(data.message)
        window.location.href=`/program/${data.program}/${data.username}`
    }
}).catch(error=>{
    console.error('Error',error)
})
})

    
