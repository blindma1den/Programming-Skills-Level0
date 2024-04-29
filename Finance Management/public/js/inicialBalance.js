
const form=document.getElementById("register");

form.addEventListener("submit",e=>{
    e.preventDefault();
    const data={
    uid:id,
    monthlyIncome:document.getElementById("monthly_income").value,
    monthlyIncomeDescription:document.getElementById("monthly_income_description").value,
    education:document.getElementById("education").value,
    educationDescription:document.getElementById("education_description").value,
    entertainmentDescription:document.getElementById('entertainment_description').value,
    entertainment:document.getElementById('entertainment').value,
    medicalDescription:document.getElementById('medical_description').value,
    medical:document.getElementById("medical").value,
    savingsDescription:document.getElementById('savings_description').value,
    savings:document.getElementById("savings").value,
    homeExpensesDescription:document.getElementById("home_expenses_description").value,
    homeExpenses:document.getElementById("home_expenses").value,
}
    //console.log(data)
    
    fetch(`/initialBalance`,{
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
    return response.json()
}).then(data=>{
    alert(data.message)
    window.location.href=`/menu/${id}`
}).catch(error=>{
    console.error('Error',error)
})

})

