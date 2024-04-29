console.log(id)
const getShipments=document.getElementById("getShipments");
getShipments.addEventListener("click",e=>{
    const data={
        uid:id
    }
    fetch('/menu/getShipments',{
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
    if(data.message){
        alert(data.message)
    }else{
        function showShipments(data,index){
           const message=`Shipping number ${index} \n ${data.destinatary} \n Shipment Code : ${data.shipmentCode} \n Status: ${data.status} \t`
            return message
        }
        let messages=`You have ${data.length} shipments \n`
        data.forEach((element,index)=>{
            let indexData=index+1
            const message=showShipments(element,indexData)
            messages=messages+message
        })
        alert(messages)
    }
}).catch(error=>{
    console.error('Error',error)
})
    
})

//LOGOUT
const logout=document.getElementById("logOut");
logout.addEventListener("click",e=>{

    const result=window.confirm("Are you sure you want to log out?")
    if(result){
        window.location.href="/"
    }else{
        console.log("cierre de sesion cancelado")
    }
})
//SHIPPING PRICE
const shippingPrice=document.getElementById('shippingPrice')
shippingPrice.addEventListener("submit",e=>{
    e.preventDefault()
    const data={
        weigth:document.getElementById('peso').value
    }
    fetch('/menu/getShippingPrice',{
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
    const result=window.confirm(data.message+", DO YOU WANT TO SEND THE PACKAGE?")
    if(result){
        window.location.href=`/menu/sendPackage/${id}`
    }else{
        console.log('Package send canceled')
    }
}).catch(error=>{
    console.error('Error',error)
})
})
