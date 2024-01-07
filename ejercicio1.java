
package banco;

import java.util.Scanner;

public class Banco {
     static int balance = 2000;
    public static void main(String[] args) {
         if (login()) {
            acciones();
        }
    }
    public static boolean login(){
         int totalAttemps = 0;
         String username = "Pepito";
        String password = "123";
            Scanner teclado = new Scanner(System.in);
    
    while(totalAttemps < 3){
        System.out.println("Ingrese su usuario");
         String user = teclado.nextLine();
        System.out.println("Ingrese su contrasenia");
         String pass = teclado.nextLine();
         if(!username.equals(user) || !password.equals(pass)){
               System.out.println("El nombre de usuario o contraseña ingresados son incorrectos");
              totalAttemps = totalAttemps + 1;
    }
    else{
        System.out.println("Ha iniciado sesion correctamente!");
        return true;
    
    }
}
         return false;
    }
    public static void depositar(){
        Scanner teclado = new Scanner(System.in);
        System.out.println("Cuanto dinero desea depositar?");
         int deposito = teclado.nextInt();
             balance =balance + deposito ;
            System.out.println("Su dinero ahora es: " + balance);
}
    public static void retirar(){

        Scanner teclado = new Scanner(System.in);
         System.out.println("Cuanto dinero desea retirar?");
         int retiro = teclado.nextInt();
         balance =balance - retiro ;
        System.out.println("Su dinero ahora es: " + balance);
}
    public static void transferir(){
        Scanner teclado = new Scanner(System.in);
         String username = "Franco";
         int transferencia = 0;
         System.out.println("Ingrese el nombre del usuario al cual desea transferir: ");
         String cuenta2 = teclado.nextLine();
         if(cuenta2.equals(username)){
        System.out.println("Ingrese el monto que desea transferir: ");
         transferencia =teclado.nextInt();
         if(balance > transferencia){
             balance = balance - transferencia;
             System.out.println("El monto transferido es de " + transferencia + " " + "su saldo ahora es de" + balance);
      }     else{
            System.out.println("Balance insuficiente.");
         }
      }
             else{System.out.println("Usuario no encontrado");}
      
   
}
    public static void verBalance(){

        System.out.println("Balance: " + balance);}

    public static void acciones(){
        Scanner teclado = new Scanner(System.in);
        int accion = 0;
        while(accion != 5){
            System.out.println("Que desea hacer?");
            System.out.println("1-Depositar 2-Retirar 3-Transferir 4-Mi balance 5-Salir");
            accion = teclado.nextInt();
             if(accion == 1){
                 depositar();
    }
            else if(accion == 2){
                  retirar();
    }
             else if(accion == 3){
                transferir();
    }
             else if(accion == 4){
                verBalance();
    }
            else if(accion == 5){
                System.out.println("-------------Haz salido del sistema-------------");    }
    
}

}
}