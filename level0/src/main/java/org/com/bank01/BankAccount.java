package org.com.bank01;

import org.com.auth.Authenticator;

import java.util.Map;
import java.util.Scanner;
import java.util.function.BiFunction;
import java.util.function.Predicate;


public class BankAccount {
    static Scanner scanner = new Scanner(System.in);
    static Integer amount = 2000;
    static Authenticator authenticator = new Authenticator();

    static Map<String, String> fromMessageList =
            Map.of("forEventWithDraw", "How much do you want to withdraw?",
                    "forEventWithDeposit", "How much do you want to deposit?",
                    "forEventWithTransfer", "How much do you want to transfer?",
                    "wrongsValues", "It is no possible to make the process with the " +
                                    "current amount",
                    "printMenu", """ 
                            What do you want to do\s
                                1 to withdraw\s
                                2 to transfer\s
                                3 to deposit\s
                                4 to view\s
                                5 to exit"""
            );

    private static void printMessage(String x) {
        String s = fromMessageList.get(x);
        System.out.println(s != null ? s : x);
    }

    public static void main(String[] args) {
        var password    = "1";
        var triesNumber = 3;
        var username =  "a";

        authenticator.authProcessFor(triesNumber, password, username);
        accountProcess();
    }

    private static void accountProcess() {
        while (authenticator.isLogged) {
            printMessage("printMenu");
            switch (scanner.next()) {
                case "1" -> {
                    printMessage("forEventWithDraw");
                    accountEvent(
                            withdrawAmount -> (withdrawAmount > 0 || withdrawAmount < amount),
                            (amount, withdrawAmount) -> amount - withdrawAmount);
                    printMessage("your current amount is " + amount);
                }
                case "2" -> {
                    printMessage("forEventTransfer");
                    accountEvent(
                            transferAmount -> (transferAmount > 0 || transferAmount < amount),
                            (amount, transferAmount) -> amount - transferAmount);
                    printMessage("your current amount is " + amount);
                }
                case "3" -> {
                    printMessage("forEventDeposit");
                    accountEvent(
                            deposit -> deposit > 0,
                            Integer :: sum);
                    printMessage("your current amount is " + amount);
                }
                case "4" -> printMessage("your current amount is " + amount);
                case "5" -> {
                    printMessage("logout...");
                    authenticator.isLogged = false;
                }
                default -> printMessage("Not at option of menu");
            }
        }
    }


    private static void accountEvent(Predicate<Integer> predicate,
                                     BiFunction<Integer, Integer, Integer> fun) {
        var entryAmount = scanner.nextInt();
        if (predicate.test(entryAmount)) {
            amount = fun.apply(amount, entryAmount);
        } else {
            printMessage("wrongsValues");
        }
    }

}
