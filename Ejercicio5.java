
package ejercicio5;

import java.util.Scanner;


public class Ejercicio5 {
static Scanner teclado = new Scanner(System.in);
    private static String[] categorias = { "Medicina", "Hogar", "Ocio", "Ahorros", "Educación" };
    private static double[] array = new double[5];
    private static         double gastos;
    public static void main(String[] args) {
              System.out.println("Ingrese sus ingresos totales: ");
       int ingresosTotales = teclado.nextInt();

        for(int i = 0;i < categorias.length;i++){
            System.out.println("Ingrese sus gastos en " + categorias[i]);
            array[i] = teclado.nextDouble();
            gastos = gastos + array[i];
        }
        
            if( gastos == ingresosTotales){
                System.out.println("Deberia reducir sus gastos si desea obtener ahorros.");
            }
            else if(gastos < ingresosTotales){
                System.out.println("Felicitaciones, su balance es positivo!");
            }
            else{System.out.println("Deberia reducir gastos ya que en su balance gasta mas de lo que gana.");}
                    
            System.out.println("Sus gastos totales son de $" +  gastos + "y su capacidad de ahorro es de $" + (ingresosTotales - gastos));
        }
    }
   
    

