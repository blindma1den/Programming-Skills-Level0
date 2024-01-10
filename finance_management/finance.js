let montoInicial = 0
let montoActual = 0
let gasto1 = 0
let gasto2 = 0
let gasto3 = 0
let gasto4 = 0
let gasto5 = 0
let totalGastado = 0
 function ingresar(){
   let  nuevoIngreso = document.getElementById('total').value

     montoInicial += parseInt(nuevoIngreso)
     montoActual = montoInicial
 }

function gastar() {
    let nuevoGasto = document.getElementById('monto').value
    let selectCategory = document.getElementById('category')
    let categoriaGasto = selectCategory.value

    console.log(selectCategory)
    console.log(categoriaGasto)
    montoActual = parseInt(montoActual) - parseInt(nuevoGasto)

    switch (categoriaGasto) {
        case "1":

            gasto1 += parseInt(nuevoGasto)
            console.log("Gasto 1: "+ gasto1);
            document.getElementById('gasto1').innerText = gasto1
            break;
        case "2":

            gasto2 += parseInt(nuevoGasto)
            document.getElementById('gasto2').innerText = gasto2
            console.log("Gasto 2: "+ gasto2);
            break;

        case "3":

            gasto3 += parseInt(nuevoGasto)
            document.getElementById('gasto3').innerText = gasto3
            console.log("Gasto 3: "+ gasto3);
            break;
        case "4":

            gasto4 += parseInt(nuevoGasto)
            document.getElementById('gasto4').innerText = gasto4
            console.log("Gasto 4: "+ gasto4);
            break;
        case "5":

            gasto5 += parseInt(nuevoGasto)
            document.getElementById('gasto5').innerText = gasto5
            console.log("Gasto 5: "+ gasto5);
            break;

    }

    montoActual += parseInt(nuevoGasto)
    console.log(montoActual)
}

function totalGastos(){

totalGastado = parseInt(gasto1) + parseInt(gasto2) + parseInt(gasto3) + parseInt(gasto4) + parseInt(gasto5)
document.getElementById('totalGastado').innerText = totalGastado
}

function gastoXCategoria(){

document.getElementById('misGastos').removeAttribute("hidden");
}

function consejo(){
    totalGastado = parseInt(gasto1) + parseInt(gasto2) + parseInt(gasto3) + parseInt(gasto4) + parseInt(gasto5)
    if (totalGastado > montoInicial){
        alert("Debes tener cuidado ,estas gastando mas de lo que ingresas")
    }
    else if(totalGastado === montoInicial){
       let mayorGasto = Math.max(gasto1, gasto2, gasto3,gasto4,gasto5)
       let c = buscarCategoriaXGasto(mayorGasto)
        alert("Debe reducir los gastos en la categoria: " + c)
    }
    else {
        alert("Felicidades")
    }
}

function buscarCategoriaXGasto(gasto){
    let categoriaMayorGasto
    if (gasto === gasto1) {
        categoriaMayorGasto = "Medical expenses"
    }
    if (gasto === gasto2) {
        categoriaMayorGasto = "Household expenses"
    }
    if (gasto === gasto3) {
        categoriaMayorGasto = "Leisure"
    }
    if (gasto === gasto4) {
        categoriaMayorGasto = "Savings"
    }
    if (gasto === gasto5) {
        categoriaMayorGasto = "Education"
    }

    return categoriaMayorGasto
}