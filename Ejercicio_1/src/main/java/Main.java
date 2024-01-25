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
    static Scanner in = new Scanner(System.in);
    public static void main(String[] args) {
        Boolean exitFlag = false;
        if(login()) System.out.println("Bienvenido");
        else System.exit(0);
        do{

            System.out.println(buildMenu());
            switch (in.nextInt()) {
                case 1:
                    depositar();
                    break;
                case 2:
                    retirar();
                    break;
                case 3:
                    verBalance();
                    break;
                case 4:
                    transferir();
                    break;
                case 0:
                    exitFlag = true;
                    break;
            }
        }while (!exitFlag);
    }

    private static boolean login() {

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
        menu.append("1. Depositar dinero\n");
        menu.append("2. Retirar dinero\n");
        menu.append("3. Ver balance\n");
        menu.append("4. Transferir dinero\n");
        menu.append("0. Salir");
        return menu.toString();
    }

    private static void depositar() {
        System.out.println("Ingrese cantidad a depositar: ");
        balance += in.nextInt();
        verBalance();
    }

    private static void retirar() {
        System.out.println("Ingrese cantidad a retirar");
        int balanceRetirar = in.nextInt();
        if (balance < balanceRetirar) {
            System.out.println("No dispones de esa cantidad");
            return;
        } else {
            balance -= balanceRetirar;
            verBalance();
        }


    }

    private static void verBalance() {
        System.out.println("Balance actual: " + balance);
    }

    private static void transferir() {
        System.out.println("Ingrese cantidad a transferir: ");
        int balanceRetirar = in.nextInt();
        if (balance < balanceRetirar) {
            System.out.println("No dispones de esa cantidad");
            return;
        } else {
            balance -= balanceRetirar;
            verBalance();
        }
    }
}

