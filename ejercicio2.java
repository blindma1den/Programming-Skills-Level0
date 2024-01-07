package conversormonedas;

import java.util.Scanner;

public class ConversorMonedas {
    static final double CLP = 884 , ARS = 811, USD = 1;
    static final double EUR = 0.91, TRY = 29.74, GBP = 0.79;
    
    static Scanner teclado = new Scanner(System.in);

    public static void main(String[] args) {
        while(true){
        double montoConvertido = conversorDivisas();
        if(!retirar(montoConvertido) ){
            break;
            }
        
    } }

    public static double conversorDivisas() {
        System.out.println("Ingrese su divisa:");
        System.out.println("1-CLP");
        System.out.println("2-ARS");
        System.out.println("3-USD");
        System.out.println("4-EUR");
        System.out.println("5-TRY");
        System.out.println("6-GBP");
        int opcion = teclado.nextInt();

        double divisaActual;
        switch (opcion) {
            case 1: divisaActual = CLP; break;
            case 2: divisaActual = ARS; break;
            case 3: divisaActual = USD; break;
            case 4: divisaActual = EUR; break;
            case 5: divisaActual = TRY; break;
            case 6: divisaActual = GBP; break;
            default:
                System.out.println("Ingrese un numero correcto");
                return 0;
        }

        System.out.println("Ingrese la moneda a la que quiere convertir:");
        System.out.println("1-CLP");
        System.out.println("2-ARS");
        System.out.println("3-USD");
        System.out.println("4-EUR");
        System.out.println("5-TRY");
        System.out.println("6-GBP");
        int opcionConversion = teclado.nextInt();

        double monedaConversion;
        String strConversion;
        switch (opcionConversion) {
            case 1: monedaConversion = CLP; 
            strConversion = "CLP";
            break;
            case 2: monedaConversion = ARS; 
            strConversion = "ARS";
            break;
            case 3: monedaConversion = USD; 
            strConversion = "USD";
            break;
            case 4: monedaConversion = EUR; 
            strConversion = "EUR";
            break;
            case 5: monedaConversion = TRY; 
            strConversion = "TRY";
            break;
            case 6: monedaConversion = GBP; 
            strConversion = "GBP";
            break;
            default:
                System.out.println("Ingrese un numero correcto");
                return 0;
        }

        System.out.println("Ingrese la cantidad de dinero que desee convertir a " + strConversion);
        double cantConvertida = teclado.nextDouble();

        double monedaFinal = cantConvertida / divisaActual * monedaConversion;
        System.out.println("Monto convertido: " + monedaFinal);
        return monedaFinal;
    }

    public static boolean retirar(double monedaFinal) {
        System.out.println("Desea retirar dinero?");
        System.out.println("1-Si\n2-No");
        int retiro = teclado.nextInt();

        if (retiro == 1) {
            System.out.println("Ingrese la cantidad que desea retirar:");
            double cantidadRetiro = teclado.nextDouble();

            if (cantidadRetiro <= monedaFinal) {
                monedaFinal -= cantidadRetiro;
                System.out.println("Ha retirado " + cantidadRetiro);
                System.out.println("Su balance ahora es de " + monedaFinal);
            } else {
                System.out.println("Fondos insuficientes.");   
            }
        }
        else{ return false;}
        return true;
    } 

}