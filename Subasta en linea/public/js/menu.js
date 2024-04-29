const currencyForm=document.getElementById('exchangeForm')
currencyForm.addEventListener("submit",e=>{
    e.preventDefault();
    console.log("hola desde el menu.js")
    const data={
        a:document.getElementById('currency_from').value,
        b:document.getElementById('currency_to').value,
        amount:document.getElementById('amount').value,
        username:window.username
    }
    console.log(data)
    if(data.a===data.b){
        alert('NO SEAS TONTO MEN')
    }else{
        fetch("/currencyMenu",{
            method: 'PUT',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(data)
        })
        .then(response=>{
        if(!response.ok){
            throw new Error('LA SOLICITUD FALLO')
        }
        return response.text()
    }).then(data=>{
        if(data==="Intercambio exitoso"){
            const message=data+", deseas realizar otra operacion?"
            const messageComfirmed=window.confirm(message); 
            if(messageComfirmed){
                location.reload()
            }else{
                window.location.href="/"
            }
        }else{
            alert(data)
        }  
    }).catch(error=>{
        console.error('Error',error)
    });
    }
})

const withdrawForm=document.getElementById("withdrawForm")
withdrawForm.addEventListener("submit",e=>{
    e.preventDefault();
    const data={
        coin:document.getElementById("currency").value,
        amount:document.getElementById("withdrawAmount").value,
        username:window.username
    }
    const message="ESTAS SEGURO QUE DESEAS REALIZAR EL RETIRO?"
    const confirmWithdraw=window.confirm(message);
    if(confirmWithdraw){
        fetch("/currencyMenu/withdraw",{
        method: 'PUT',
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
    console.log(typeof(data))
    console.log(data)
    
    if(data.finalAmount){
        const message=`Retiro exitoso. \t Monto del retiro: ${data.netWithdraw} \t Comision del banco: ${data.comision} \t Monto final : ${data.finalAmount} \t DESEAS REALIZAR OTRA OPERACION?`
        //const message="mañana"
        const confirm=window.confirm(message);
        if(confirm){
            location.reload()
        }else{
            window.location.href="/"
        }
    }else{
        alert(data)
        location.reload()
    }
}).catch(error=>{
    console.error('Error',error)
});
    }
    
})


/*

*/

