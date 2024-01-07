import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // int fixedValue = 2000;
        bankMenu();


        /*
        switch (scanner.next()){
            case "USD" -> {

            }
        }
         */
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
                converterMenu();
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

    static String converterMenu() {
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

        return specificMenu(option);
    }

    static String specificMenu(String optionChosen) {
        Scanner scanner = new Scanner(System.in);
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
                String optionChosen2 = scanner.next();
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
        return optionChosen;
    }


    static Double convertToUSD(String key, int fixedValue){
        HashMap<String, Double> initialCurrency = new HashMap<>();

        initialCurrency.put("USD", 1.00);
        initialCurrency.put("EUR", 1.10);
        initialCurrency.put("ARS", 0.0012);
        initialCurrency.put("GBP", 1.27);
        initialCurrency.put("TRY", 0.034);
        initialCurrency.put("CLP", 0.0011);

        // ESTO DEVUELVE DOLARES
        return fixedValue/initialCurrency.get(key);
    }

    static Double convert(double usd, String monedaFinal){
        HashMap<String, Double> usdConverter = new HashMap<String, Double>();

        usdConverter.put("USD", 1.00);
        usdConverter.put("EUR", 0.91);
        usdConverter.put("CLP", 888.94);
        usdConverter.put("ARS", 811.20);
        usdConverter.put("TRY", 29.81);
        usdConverter.put("GBP", 0.79);

        return usd * usdConverter.get(monedaFinal);
    }
}

