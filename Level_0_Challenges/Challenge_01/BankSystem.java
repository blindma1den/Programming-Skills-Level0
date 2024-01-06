package Level_0_Challenges.Challenge_01;

import java.util.InputMismatchException;
import java.util.Scanner;

public class BankSystem {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Bank bank = new Bank();
        int attempts = 0;
        User user = null;

        while (true) {
            printMainMenu();

            while (!sc.hasNextInt()) {
                System.out.println("Error! Please enter a valid number");
                sc.next();
                printMainMenu();
            }

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    user = signIn(sc, bank, attempts);
                    if (user != null) {
                        transactionsMenu(sc, user, bank);
                    }
                    break;

                case 2:
                    // Salir
                    System.out.println("Logging off. See you later!");
                    System.exit(0);

                default:
                    System.out.println("\nInvalid option. Try again");
                    break;
            }
        }
    }

    private static void printMainMenu() {
            System.out.println("\n**** Welcome to the Bank System ****");
            System.out.println("1. Sign in");
            System.out.println("2. Exit\n");
            System.out.print("Select an option: ");
    }

    private static User signIn(Scanner sc, Bank bank, int attempts) {
        do {
            System.out.println("\n**** Login System ****");
            System.out.print("Enter your username: ");
            String userName = sc.next();
            System.out.print("Enter your password: ");
            String userPassword = sc.next();

            User user = bank.signIn(userName, userPassword);

            if (user == null) {
                attempts++;
                System.out.println("Login failed. Please try again");

                if (attempts == 3) {
                    System.out.println("User account locked! :(");
                    System.exit(0);
                }
            } else {
                return user;
            }
        } while (true);
    }

    private static void transactionsMenu(Scanner sc, User user, Bank bank) {
        outerLoop:
        while (true) {
            System.out.println("\n**** Transactions Menu ****");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. View balance");
            System.out.println("4. Transfer");
            System.out.println("5. Sign out\n");
            System.out.print("Select an option: ");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("\n**** Deposit Transaction ****");
                    System.out.print("Enter the deposit amount: ");
                    double quantityDeposit = sc.nextDouble();
                    user.deposit(quantityDeposit);
                    break;

                case 2:
                    System.out.print("\nEnter the withdrawal amount: ");
                    double quantityWithdrawal = sc.nextDouble();
                    user.withdraw(quantityWithdrawal);
                    break;

                case 3:
                    user.viewBalance();
                    break;

                case 4:
                    System.out.print("\nEnter the recipient's username: ");
                    String recipientName = sc.next();
                    User recipientUser = bank.getUsers().get(recipientName);

                    if (recipientUser != null && recipientUser != user) {
                        System.out.print("Enter the transfer amount: ");
                        double quantityTransfer = sc.nextDouble();

                        user.transfer(recipientUser, quantityTransfer);
                    } else {
                        System.out.println("Failed transfer. Recipient user not found or cannot transfer to yourself :(");
                    }
                    break;

                case 5:
                    System.out.println("Logging out. See you later!");
                    break outerLoop;

                default:
                    System.out.println("Opción no válida. Inténtelo de nuevo.");
                    break;
            }
        }
    }
}