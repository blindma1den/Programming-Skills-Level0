package main;

import auxiliar.UserInfo;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean isValid = false;
        String savedUsername = "user1";
        String savedPass = "ripeadmin";

        boolean isLogged = login(savedUsername, savedPass, isValid, scanner);

        if (isLogged) {
            postalMenu();
        } else {
            System.out.println("Too many attempts! Cya loser!");
        }
    }

    static boolean login(String savedUsername, String savedPass, boolean isValid, Scanner scanner) {
        int count = 0;
        System.out.println("Welcome to your Orange Parcel Service \n" +
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

        System.out.println("Choose the operation you want to do: ");
        System.out.println("1. Send my Package, huh?");
        System.out.println("2. Exit");
        System.out.print("Option: ");
        int numberOption = scanner.nextInt();
        System.out.println("The option chosen was: " + numberOption);

        return numberOption;
    }

    static void postalMenu() {
        switch (mainMenu()) {
            case 1:
                int random_int = (int) Math.floor(Math.random() * (1000 - 100 + 1) + 100);
                summary(form(), packageWeight(), random_int);
                break;
            case 2:
                System.out.println("Cya!");
                break;
            default:
                System.out.println("Wrong Option! Try again (Only one time left).");
                postalMenu();
                break;
        }
    }

    static ArrayList<UserInfo> form() {
        Scanner scanner = new Scanner(System.in);

        ArrayList<UserInfo> userList = new ArrayList<>();
        UserInfo userSender = new UserInfo();
        UserInfo userRecipient = new UserInfo();

        Pattern pattern = Pattern.compile("^(Street|Avenue|Diagonal)\\s([1-9]|[1-9][0-9]|100)\\s.\\S+$");

        System.out.println("The address format is: Street|Avenue|Diagonal [Street number] [City Name]");

        System.out.println("----Sender's Info----");
        System.out.print("Introduce sender's name: ");
        String senderName = scanner.nextLine();
        userSender.setName(senderName);

        System.out.print("Introduce sender's address: ");
        String senderAddress = scanner.nextLine();
        userSender.setAddress(senderAddress);

        System.out.println("----Recipient's Info----");
        System.out.print("Introduce recipient's name: ");
        String recipientName = scanner.nextLine();
        userRecipient.setName(recipientName);
        System.out.print("Introduce recipient's address: ");
        String recipientAddress = scanner.nextLine();
        userRecipient.setAddress(recipientAddress);

        Matcher matcherSender = pattern.matcher(senderAddress);
        Matcher matcherRecipient = pattern.matcher(recipientAddress);

        boolean senderMatch = matcherSender.matches();
        boolean recipientMatch = matcherRecipient.matches();

        if (senderMatch && recipientMatch) {
            userList.add(userSender);
            userList.add(userRecipient);
        } else {
            System.out.println("The address format is wrong! Check it!");
            form();
        }

        return userList;
    }

    static double packageWeight() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce the package Weight in Kg: ");
        double weight = scanner.nextDouble();
        return Math.ceil(weight);
    }

    static void summary(ArrayList<UserInfo> infoList, double packageWeight, int random_int) {
        int packagePrice = (int) (packageWeight * 2);
        System.out.println("---------- SUMMARY OF THE PACKAGE " + random_int + " ----------");
        System.out.println("Sender's Information: ");
        System.out.println("Name: " + infoList.get(0).getName());
        System.out.println("Address: " + infoList.get(0).getAddress());
        System.out.println("Recipient's Information: ");
        System.out.println("Name: " + infoList.get(1).getName());
        System.out.println("Address: " + infoList.get(1).getAddress());
        System.out.println("The package weight is: " + packageWeight + "Kg" + ", so the price is: " + packagePrice + "USD");
        System.out.println("---------- END OF THE SUMMARY ----------");

        Scanner scanner = new Scanner(System.in);

        System.out.println("Do you agree with the price?");
        System.out.println("1. Yes!");
        System.out.println("2. No, let me ESCAPE THIS HELL!");
        System.out.print("Select your option: ");
        int option = scanner.nextInt();

       if (option == 1){
           System.out.println("Thanks for use our Services!");
           keepOrLeave();
       } else {
           postalMenu();
       }

    }

    static void keepOrLeave(){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Do you want to perform another operation?");
        System.out.println("1. Yes!");
        System.out.println("2. No, let me ESCAPE THIS HELL!");
        System.out.print("Select your option: ");
        int option = scanner.nextInt();

        if (option != 1 && option != 2){
            System.out.println("Wrong option, try again!");
            keepOrLeave();
        } else if (option == 1){
            postalMenu();
        }
    }
}