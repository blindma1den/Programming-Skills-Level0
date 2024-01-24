import java.util.Scanner;

//1. Create an online banking system with the following features:
//
//        * Users must be able to log in with a username and password.
//        * If the user enters the wrong credentials three times, the system must lock them out.
//        * The initial balance in the bank account is $2000.
//* The system must allow users to deposit, withdraw, view, and transfer money.
//* The system must display a menu for users to perform transactions.
public class Main {
    static int balance = 2000;
    public static void main(String[] args) {
        
        do{
            if(login()) System.out.println("Bienvenido");
            else break;

            System.out.println(buildMenu());



        }while (true);
    }

    private static boolean login() {
        Scanner in = new Scanner(System.in);
        String username = "user";
        String password = "pass";

        for (int i = 0; i < 3; i++) {
            System.out.println("Ingrese Usuario");
            String inputUser = in.nextLine();
            System.out.println("Ingrese Contrasena");
            String inputPassword = in.nextLine();

            if (inputUser.equals(username) && inputPassword.equals(password)) {
                return true;
            } else {
                System.out.println("Usuario/Contraena Incorrectos");
            }
        }
        System.out.println("Sistema bloqueado");
        return false;
    }

    private static String buildMenu() {
        StringBuilder menu = new StringBuilder();
        menu.append("1. Depositar dinero");
        menu.append("2. Retirar dinero");
        menu.append("3. Ver balance");
        menu.append("4. Transferir dinero");
        menu.append("0. Salir");
        return menu.toString();
    }
}

