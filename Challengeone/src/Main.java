import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);

        boolean isValid = false;
        int initAmount = 2000;

        String validcBank = "ES3321212200";

        String savedUsername = "user1";
        String savedPass = "2r7*{24LrA>z";

        if(login(savedUsername, savedPass, isValid, scanner)){
            bankMenu(scanner, initAmount, validcBank);
        } else {
            System.out.println("Contact with Orange!");
            Thread.sleep(5000);
            System.out.println("That's all folks!");
        }
    }

    static boolean login(String savedUsername, String savedPass, boolean isValid, Scanner scanner) {
        int count = 0;
        System.out.println("Welcome to your HomeBanking System \n" +
                "Please sign in");

        while (count < 3) {
            System.out.print("Username: ");
            String username = scanner.next();
            System.out.print("Password: ");
            String password = scanner.next();
            if (username.equals(savedUsername) && password.equals(savedPass)) {
                return isValid = true;
            } else {
                count = count + 1;
                System.out.println("Pass or user is incorrect");
            }
        }

        return isValid;
    }

    static int mainMenu() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to your HomeBank ");
        System.out.println("Choose the operation you want to do: ");
        System.out.println("1. Deposit");
        System.out.println("2. Withdraw");
        System.out.println("3. View");
        System.out.println("4. Transfer");
        System.out.print("Option: ");
        int numberOption = scanner.nextInt();
        System.out.println("The option chosen was: " + numberOption);

        return numberOption;
    }

    static void bankMenu(Scanner scanner, int initAmount, String validcBank) {
        switch (mainMenu()) {
            case 1:
                deposit(scanner, initAmount);
                break;
            case 2:
                withdraw(scanner, initAmount);
                break;
            case 3:
                System.out.println("Total amount: " + initAmount);
                break;
            case 4:
                transfer(scanner, initAmount, validcBank);
                break;
            default:
                System.out.println("Cya");
                break;
        }
    }

    static void deposit(Scanner scanner, int initAmount) {
        System.out.println("How much money do you want to deposit?");
        int cantidad = scanner.nextInt();
        if (cantidad < 0) {
            System.out.println("Invalid quantity, please try again");

        } else {
            initAmount = initAmount + cantidad;
            System.out.println("Total amount: " + initAmount);
        }
        scanner.close();
    }

    static void withdraw(Scanner scanner, int initAmount) {
        System.out.println("How much money do you want to withdraw?");
        int cantidad = scanner.nextInt();
        if (cantidad > initAmount || cantidad < 0) {
            System.out.println("Invalid quantity, please try again");

        } else {
            initAmount = initAmount - cantidad;
            System.out.println("Total amount: " + initAmount);
        }
        scanner.close();
    }

    static void transfer(Scanner scanner, int initAmount, String validcBank) {
        System.out.println("Introduce the bank account you want to transfer the money:");
        String cbank = scanner.next();
        if (cbank.equals(validcBank)) {
            System.out.println("How much money do you want to transfer?");
            int cantidad = scanner.nextInt();

            if (cantidad > initAmount || cantidad < 0) {
                System.out.println("Invalid quantity, please try again");

            } else {
                initAmount = initAmount - cantidad;
                System.out.println("Total amount: " + initAmount);
            }
        } else {
            System.out.println("Wrong bank account, try again");
        }
        scanner.close();
    }
}