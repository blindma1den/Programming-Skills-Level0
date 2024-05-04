
       // Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
 	   // The user must choose their initial currency and the currency they want to exchange to.
 	   // The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
 	   // If the user decides to withdraw the funds, the system will charge a 1% commission.
 	   // Set a minimum and maximum amount for each currency, it can be of your choice.
 	   // The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.


        let initialAmount = '';

function inicio(){
    let initialCurrency = prompt('Bienvenidos a la casa de cambio.\nConvertir de:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £');   
    
    if(initialCurrency === ''){
        let continuar = confirm('CAMPO OBLIGATORIO.\n\nDesea continuar?');
        if(continuar === true){
            initialCurrency = prompt('Bienvenidos a la casa de cambio.\nConvertir de:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £')
        }else{
            alert('GRACIAS POR SU PREFERENCIA. VUELA PRONTO')
        }
    }else if(initialCurrency === '1'){
        initialAmount= prompt('Ingrese cantidad')
        let finalCurrency = prompt('Convertir a:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £')
        clp(initialAmount, finalCurrency);
    }else if(initialCurrency === '2'){
        initialAmount= prompt('Ingrese cantidad')
        let finalCurrency = prompt('Convertir a:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £')
        ars(initialAmount, finalCurrency);
    }else if(initialCurrency === '3'){
        initialAmount= prompt('Ingrese cantidad')
        let finalCurrency = prompt('Convertir a:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £')
        usd(initialAmount, finalCurrency);
    }else if(initialCurrency === '4'){
        initialAmount= prompt('Ingrese cantidad')
        let finalCurrency = prompt('Convertir a:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £')
        eur(initialAmount, finalCurrency);
    }else if(initialCurrency === '5'){
        initialAmount= prompt('Ingrese cantidad')
        let finalCurrency = prompt('Convertir a:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £')
        trycurrency(initialAmount, finalCurrency);
    }else if(initialCurrency === '6'){
        initialAmount= prompt('Ingrese cantidad')
        let finalCurrency = prompt('Convertir a:\n1. Pesos Chilenos - CLP: $\n2. Pesos Argentinos - ARS: $\n3. Dolares EstadoUnidenses - USD: $\n4. Euros - EUR: €\n5. Lira Turca - TRY: ₺\n6. Libra Esterlina - GBP: £')
        gbp(initialAmount, finalCurrency);
    }else {
        let pregunta = confirm('Desea salir del sistema?')
    
            if(pregunta === true){
                alert('GRACIAS POR SU PREFERENCIA. VUELA PRONTO')
            }
            inicio()
    }
}

function clp(amount, currency){
    if(currency === '1'){
        let symbol = '$';
        let cantidad = confirm('Pesos Chilenos - CLP: '+ symbol + Number(amount) / 1 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) / 1;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '2'){
        let symbol = '$';
        let cantidad = confirm('Pesos Argentinos - ARS: '+ symbol + Number(amount) * 0.94 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.94;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '3'){
        let symbol = '$';
        let cantidad = confirm('Dolares EstadoUnidenses - USD: '+ symbol + Number(amount) * 0.0011 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.0011;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '4'){
        let symbol = '€';
        let cantidad = confirm('Euros - EUR: '+ symbol + Number(amount) * 0.00099 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.00099;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '5'){
        let symbol = '₺';
        let cantidad = confirm('Lira Turca - TRY: '+ symbol + Number(amount) * 0.035 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.035;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '6'){
        let symbol = '£';
        let cantidad = confirm('Libra Esterlina - GBP: '+ symbol + Number(amount) * 0.00085 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.00085;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }
}

function ars(amount, currency){
    if(currency === '1'){
        let symbol = '$';
        let cantidad = confirm('Pesos Chilenos - CLP: '+ symbol + Number(amount) * 1.07 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 1.07;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '2'){
        let symbol = '$';
        let cantidad = confirm('Pesos Argentinos - ARS: '+ symbol + Number(amount) / 1 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) / 1;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '3'){
        let symbol = '$';
        let cantidad = confirm('Dolares EstadoUnidenses - USD: '+ symbol + Number(amount) * 0.0011 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.0011;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '4'){
        let symbol = '€';
        let cantidad = confirm('Euros - EUR: '+ symbol + Number(amount) * 0.0011 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.0011;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '5'){
        let symbol = '₺';
        let cantidad = confirm('Lira Turca - TRY: '+ symbol + Number(amount) * 0.037 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.037;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '6'){
        let symbol = '£';
        let cantidad = confirm('Libra Esterlina - GBP: '+ symbol + Number(amount) * 0.00090 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.00090;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }
}

function usd(amount, currency){
    if(currency === '1'){
        let symbol = '$';
        let cantidad = confirm('Pesos Chilenos - CLP: '+ symbol + Number(amount) * 938.92 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 938.92;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '2'){
        let symbol = '$';
        let cantidad = confirm('Pesos Argentinos - ARS: '+ symbol + Number(amount) * 878.75 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 878.75;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '3'){
        let symbol = '$';
        let cantidad = confirm('Dolares EstadoUnidenses - USD: '+ symbol + Number(amount) / 1 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) / 1;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '4'){
        let symbol = '€';
        let cantidad = confirm('Euros - EUR: '+ symbol + Number(amount) * 0.93 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.93;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '5'){
        let symbol = '₺';
        let cantidad = confirm('Lira Turca - TRY: '+ symbol + Number(amount) * 32.35 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 32.35;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '6'){
        let symbol = '£';
        let cantidad = confirm('Libra Esterlina - GBP: '+ symbol + Number(amount) * 0.7942 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.7942;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }
}

function eur(amount, currency){
    if(currency === '1'){
        let symbol = '$';
        let cantidad = confirm('Pesos Chilenos - CLP: '+ symbol + Number(amount) * 1012.72 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 1012.72;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '2'){
        let symbol = '$';
        let cantidad = confirm('Pesos Argentinos - ARS: '+ symbol + Number(amount) * 946.71 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 946.71;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '3'){
        let symbol = '$';
        let cantidad = confirm('Dolares EstadoUnidenses - USD: '+ symbol + Number(amount) * 1.08 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 1.08;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '4'){
        let symbol = '€';
        let cantidad = confirm('Euros - EUR: '+ symbol + Number(amount) / 1 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) / 1;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '5'){
        let symbol = '₺';
        let cantidad = confirm('Lira Turca - TRY: '+ symbol + Number(amount) * 34.85 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 34.85;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '6'){
        let symbol = '£';
        let cantidad = confirm('Libra Esterlina - GBP: '+ symbol + Number(amount) * 0.86 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.86;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }
}

function trycurrency(amount, currency){
    if(currency === '1'){
        let symbol = '$';
        let cantidad = confirm('Pesos Chilenos - CLP: '+ symbol + Number(amount) * 29.05 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 29.05;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '2'){
        let symbol = '$';
        let cantidad = confirm('Pesos Argentinos - ARS: '+ symbol + Number(amount) * 27.17 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 27.17;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '3'){
        let symbol = '$';
        let cantidad = confirm('Dolares EstadoUnidenses - USD: '+ symbol + Number(amount) * 0.031 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.031;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '4'){
        let symbol = '€';
        let cantidad = confirm('Euros - EUR: '+ symbol + Number(amount) * 0.029 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.029;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '5'){
        let symbol = '₺';
        let cantidad = confirm('Lira Turca - TRY: '+ symbol + Number(amount) / 1 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) / 1;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '6'){
        let symbol = '£';
        let cantidad = confirm('Libra Esterlina - GBP: '+ symbol + Number(amount) * 0.025 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 0.025;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }
}

function gbp(amount, currency){
    if(currency === '1'){
        let symbol = '$';
        let cantidad = confirm('Pesos Chilenos - CLP: '+ symbol  + Number(amount) * 1183.15 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 1183.15;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '2'){
        let symbol = '$';
        let cantidad = confirm('Pesos Argentinos - ARS: '+ symbol + Number(amount) * 1105.27 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 1105.27;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '3'){
        let symbol = '$';
        let cantidad = confirm('Dolares EstadoUnidenses - USD: '+ symbol  + Number(amount) * 1.26 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 1.26;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '4'){
        let symbol = '€';
        let cantidad = confirm('Euros - EUR: '+ symbol +  Number(amount) * 1.17 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) * 1.17;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '5'){
        let symbol = '₺';
        let cantidad = confirm('Lira Turca - TRY: '+ symbol + Number(amount) + 40.66 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) + 40.66;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }else if(currency === '6'){
        let symbol = '£';
        let cantidad = confirm('Libra Esterlina - GBP: '+ symbol + Number(amount) / 1 + "\nDesea retirar esta cantidad? ")
        let cantidadExchange = Number(amount) / 1;
        if(cantidad === true){
            withdraw(cantidadExchange, symbol);
        }else{
            inicio();
        }
    }
}

function withdraw(cantidad, symbol){
    Number(cantidad)
    let comision = cantidad * 0.01;
    let retiro = confirm('DATOS DE RETIRO\nCantidad: '+ symbol + cantidad + '\nComision 1%: ' + symbol + comision + '\nTotal a Retirar: ' + symbol+ (cantidad - comision) + '\n\nDesea realizar una nueva operacion?')
    
    if(retiro === true){
        inicio()
    }else{
        alert('GRACIAS POR SU PREFERENCIA. VUELA PRONTO')
    }
}

inicio()