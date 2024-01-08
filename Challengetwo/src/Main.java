import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    private static final DecimalFormat df = new DecimalFormat("0.00");
    public static void main(String[] args) {
        bankMenu();
    }


    static void bankMenu() {
        switch (mainMenu()) {
            case 1:
                System.out.println("Currently unavailable");
                break;
            case 2:
                System.out.println("Currently unavailable");
                break;
            case 3:
                System.out.println("Currently unavailable");
                break;
            case 4:
                System.out.println("Currently unavailable");
                break;
            case 5:
                converterMenu(moneyAsker());
                break;
            case 6:
                System.out.println("Cya");
                break;
            default:
                System.out.println("Cya");
                break;
        }
    }
    static int mainMenu() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to your HomeBank ");
        System.out.println("Choose the operation you want to do: ");
        System.out.println("1. Deposit");
        System.out.println("2. Withdraw");
        System.out.println("3. View");
        System.out.println("4. Transfer");
        System.out.println("5. Currency Converter");
        System.out.println("6. Exit");
        System.out.print("Option: ");
        int numberOption = scanner.nextInt();
        System.out.println("The option chosen was: " + numberOption);

        return numberOption;
    }
    static void converterMenu(double amount) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Orange Currency Converter ");
        System.out.println("We got hacked so please be patient!");
        System.out.println("Choose initial Currency: ");
        System.out.println("-> USD");
        System.out.println("-> EUR");
        System.out.println("-> ARS");
        System.out.println("-> CLP");
        System.out.println("-> TRY");
        System.out.println("-> GBP");
        System.out.print("Type the Initial Currency you want to use (USD, EUR, ...): ");
        String option = scanner.next();
        System.out.println("The option choosen was: " + option);

        double usd = convertToUSD(option, amount);
        specificMenu(option, usd);
    }
    static void specificMenu(String optionChosen, double usd) {
        Scanner scanner = new Scanner(System.in);
        String optionChosen2 = null;
        switch (optionChosen) {
            case "USD", "EUR", "ARS", "CLP", "TRY", "GBP" -> {
                System.out.println("Choose the currency you want to convert to: ");
                System.out.println("-> USD");
                System.out.println("-> EUR");
                System.out.println("-> ARS");
                System.out.println("-> CLP");
                System.out.println("-> TRY");
                System.out.println("-> GBP");
                System.out.print("Type the Initial Currency you want to use (USD, EUR, ...): ");
                optionChosen2 = scanner.next();
                System.out.println("The option chosen was: " + optionChosen2);

                while (optionChosen2.equals(optionChosen)){
                    System.out.println("Choose a different option! : ");
                    System.out.println("-> USD");
                    System.out.println("-> EUR");
                    System.out.println("-> ARS");
                    System.out.println("-> CLP");
                    System.out.println("-> TRY");
                    System.out.println("-> GBP");
                    System.out.print("Type the Initial Currency you want to use (USD, EUR, ...): ");
                    optionChosen2 = scanner.next();
                    System.out.println("The option chosen was: " + optionChosen2);
                }
            }
        }
        optionChosen = optionChosen2;
        subMenu(convert(usd,optionChosen), optionChosen);
    }

    static void subMenu(double finalAmount, String optionChosen){
        Scanner scanner = new Scanner(System.in);
        System.out.println("The amount of money after the conversion is: " + df.format(finalAmount) + optionChosen);
        System.out.println("Select one of these following options: ");
        System.out.println("1. Withdraw");
        System.out.println("2. Back to Main Menu");
        int option = scanner.nextInt();

        while (option != 1 && option != 2){
            System.out.print("Wrong Option, try again: ");
            option = scanner.nextInt();
        }

        if (option == 1){
            withdraw(finalAmount, optionChosen);
        } else {
            bankMenu();
        }
    }
    static Double convertToUSD(String key, double amount){
        HashMap<String, Double> initialCurrency = new HashMap<>();

        initialCurrency.put("USD", 1.00);
        initialCurrency.put("EUR", 1.10);
        initialCurrency.put("ARS", 0.0012);
        initialCurrency.put("GBP", 1.27);
        initialCurrency.put("TRY", 0.034);
        initialCurrency.put("CLP", 0.00112);

        // ESTO DEVUELVE DOLARES
        return (amount * initialCurrency.get(key));
    }
    static Double convert(double usd, String monedaFinal){
        HashMap<String, Double> usdConverter = new HashMap<String, Double>();

        usdConverter.put("USD", 1.00);
        usdConverter.put("EUR", 0.91);
        usdConverter.put("CLP", 888.94);
        usdConverter.put("ARS", 811.20);
        usdConverter.put("TRY", 29.81);
        usdConverter.put("GBP", 0.79);

        return (usd * usdConverter.get(monedaFinal));
    }

    static void withdraw(double finalAmount, String optionChosen) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("How much money do you want to withdraw?");
        double cantidad = scanner.nextDouble();
        double verif= cantidad + (cantidad*0.01);
        if ( verif > finalAmount && cantidad < 0) {
            System.out.println("Invalid quantity, please try again");
            withdraw(finalAmount, optionChosen);
        } else {
            finalAmount = finalAmount - verif;
            System.out.println("Total amount: " + df.format(finalAmount) + optionChosen);
            menuAnotherOperation();
        }
    }

    static int moneyAsker(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Minimum and Maximum amount per currency");
        System.out.println("USD -> [Min: 500, Max: 100000]");
        System.out.println("EUR -> [Min: 500, Max: 100000]");
        System.out.println("CLP -> [Min: 500, Max: 100000]");
        System.out.println("ARS -> [Min: 500, Max: 100000]");
        System.out.println("TRY -> [Min: 500, Max: 100000]");
        System.out.println("GBP -> [Min: 500, Max: 100000]");
        System.out.print("Please, insert how much money you want to convert: ");
        int money = scanner.nextInt();
        if ((money >= 500) && (money <= 100000)){
            return money;
        }else{
            System.out.println("Error, invalid amount. Try again.");
            moneyAsker();
        }
        return money;
    }

    static void menuAnotherOperation() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Do you want to perform another operation?");
        System.out.println("1. Yes");
        System.out.println("2. No, leave me alone");
        int option = scanner.nextInt();

        while (option != 1 && option != 2) {
            System.out.print("Wrong Option, try again: ");
            option = scanner.nextInt();
        }

        if (option == 1) {
            bankMenu();
        }
    }
}

