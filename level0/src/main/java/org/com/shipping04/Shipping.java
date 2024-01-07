package org.com.shipping04;

import org.com.auth.Authenticator;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Shipping {
    static Authenticator authenticator = new Authenticator();
    static Scanner scanner = new Scanner(System.in);
    static final double priceFactor = 2.00;
    static final String[] direcciones = new String[]{"Calle Lupo 32, Argentina",
            "Calle Juan 25, Colombia", "a", "b"};
    static Map<String, String> message =
            Map.of("options", """
                            1) Send a Package\s
                            2) Exit
                            """,
                    "askingInfo", """
                            Please insert details\s
                            Sender Address:
                            """);

    private static void printMessage(String x) {
        var s = message.get(x);
        System.out.println(s != null ? s : x);
    }

    public static void main(String[] args) {
        var tries    = 3;
        var password = "aaa";
        var username = "alex";

        authenticator.authProcessFor(tries, password, username);
        shippingProcess();
    }

    private static void shippingProcess() {
        while (authenticator.isLogged) {
            printMessage("options");
            switch (scanner.nextInt()) {
                case 1 -> {
                    var result           = askrequiredData();
                    var areValidAddresses = valitationData(result);
                    if (areValidAddresses) {
                        printMessage("Amount pay is: " + priceFactor * result.packageWeight());
                    } else {
                        printMessage("Not allowed Addresses");
                    }
                }
                case 2 -> {
                    printMessage("Thank you for using the service.");
                    authenticator.isLogged = false;
                }
                default -> printMessage("Please enter a valid choice.");

            }
        }
    }

    private static boolean valitationData(RequiredData result) {
        return Arrays.asList(direcciones)
                       .containsAll(List.of(result.senderAddress(),
                               result.receiverAddress()))
               && result.packageWeight > 0;
    }

    private static RequiredData askrequiredData() {
        printMessage("askingInfo");
        var senderAddress = scanner.next();
        printMessage("Receive Address:");
        var receiverAddress = scanner.next();
        printMessage("Package weight (kg):");
        var packageWeight = scanner.nextDouble();
        return new RequiredData(senderAddress, receiverAddress, packageWeight);
    }

    private record RequiredData(
            String senderAddress, String receiverAddress, double packageWeight
    ) {}
}
