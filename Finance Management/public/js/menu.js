
// LIST RENDER
function activeList(buttonId,divId){
    const element=document.getElementById(buttonId);
    element.addEventListener("click",e=>{
        const activate=document.getElementById(divId);
        document.getElementById("medicalList").classList.add("hidden");
        document.getElementById("homespendsList").classList.add("hidden");
        document.getElementById("leisureList").classList.add("hidden");
        document.getElementById("savingList").classList.add("hidden");
        document.getElementById("educationList").classList.add("hidden");
        document.getElementById("incomesList").classList.add("hidden");
        activate.classList.remove("hidden");
    })
}
activeList("medicalButton","medicalList");
activeList("homeSpendingButton","homespendsList");
activeList("educationButton","educationList");
activeList("leisureButton","leisureList");
activeList("savingButton","savingList");
activeList("incomesButton","incomesList");


//BALANCE STATUS CARD
const warningsParagraph={
    negative:"Your balance is negative, you should visit our channel with tips to reduce expenses",
    equal:"The balance between your income and expenses is tight, you may need to take measures to reduce expenses",
    positive:"You are managing your income very well, congratulations."
}

let warnings={
    h2:document.getElementById("h2-warning"),
    p:document.getElementById('p-warning'),
    div:document.getElementById("div-warning")

}
console.log(warnings.h2)
console.log(document.getElementById("h2-warning"))

if(balance >0){
    warnings.h2.textContent="Congrats";
    warnings.p.textContent=warningsParagraph.positive;
    warnings.div.classList=[];
    warnings.div.classList.add("bg-green-500", "text-white" ,"rounded-lg", "p-6" ,"mb-8","shadow-lg")
};
if(balance<0){
    warnings.h2.textContent="Warning!";
    warnings.p.textContent=warningsParagraph.negative;
    warnings.div.classList=[];
    warnings.div.classList.add("bg-red-500", "text-white" ,"rounded-lg", "p-6" ,"mb-8","shadow-lg")
}
if(balance==0){
    warnings.h2.textContent="Could be better";
    warnings.p.textContent=warningsParagraph.equal;
    warnings.div.classList=[];
    warnings.div.classList.add("bg-yellow-500", "text-white" ,"rounded-lg", "p-6" ,"mb-8","shadow-lg")
}
//TIPS CARD
const links={
    homespends:"https://www.youtube.com/watch?v=WByjhBqxWn0&pp=ygURaG9tZSBzYXZpbmdzIHRpcHM%3D",
    medicals:"https://www.youtube.com/watch?v=5Linp0J5awA",
    leisure:"https://www.youtube.com/watch?v=XTGP6stvhQ8",
    saving:"https://www.youtube.com/watch?v=hzxS9qWTcBM",
    education:"https://www.youtube.com/watch?v=kwvGdQrwSxs"
}
const a=document.getElementById("a-link");
console.log(links[biggestExpense])
console.log(biggestExpense)
a.href=links[biggestExpense]
//GET TOTAL EXPENSES BY CATEGORY
const getExpensesById=document.getElementById("getExpensesById");
getExpensesById.addEventListener("submit",e=>{
    e.preventDefault();
    const select=document.getElementById("expense_by_category").value
    const data={
        value:select,
        uid:id
    }
    fetch('/menu/getExpensesByCategory',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(response=>{
    if(!response.ok){
        throw new Error('FAILED REQUEST')
    }
    return response.json()
}).then(data=>{
    alert(data.message)
}).catch(error=>{
    console.error('Error',error)
})
});

//GET TOTAL OF ALL EXPENSES
const totalExpenses=document.getElementById("totalExpenses");
totalExpenses.addEventListener("click",e=>{
    const data={
        uid:id
    }
    fetch('/menu/getTotalExpenses',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(response=>{
    if(!response.ok){
        throw new Error('FAILED REQUEST')
    }
    return response.json()
}).then(data=>{
    alert(data.message)
}).catch(error=>{
    console.error('Error',error)
})
});

//GET TOTAL OF ALL INCOMES
const totalIncomes=document.getElementById("totalIncomes");
totalIncomes.addEventListener("click",e=>{
    const data={
        uid:id
    }
    fetch('/menu/getTotalIncomes',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(response=>{
    if(!response.ok){
        throw new Error('FAILED REQUEST')
    }
    return response.json()
}).then(data=>{
    alert(data.message)
}).catch(error=>{
    console.error('Error',error)
})
});

//REGISTER NEW INCOME
const registerIncome=document.getElementById("registerIncome");
registerIncome.addEventListener("submit",e=>{
    e.preventDefault();
    const data={
        description:document.getElementById("income_description").value,
        amount:document.getElementById("income_amount").value,
        uid:id
    }
    console.log(data);
    fetch('/menu/newIncome',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(response=>{
    if(!response.ok){
        throw new Error('FAILED REQUEST')
    }
    return response.json()
}).then(data=>{
    alert(data.message)
    window.location.reload()
}).catch(error=>{
    console.error('Error',error)
})
})

//REGISTER NEW EXPENSE
const registerExpense=document.getElementById("registerExpense");
registerExpense.addEventListener("submit",e=>{
    e.preventDefault();
    const data={
        value:document.getElementById("expense_category").value,
        description:document.getElementById("expense_description").value,
        amount:document.getElementById("expense_amount").value,
        uid:id
    }
    console.log(data)
    fetch('/menu/newExpense',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(response=>{
    if(!response.ok){
        throw new Error('FAILED REQUEST')
    }
    return response.json()
}).then(data=>{
    alert(data.message)
    window.location.reload()
}).catch(error=>{
    console.error('Error',error)
})
})