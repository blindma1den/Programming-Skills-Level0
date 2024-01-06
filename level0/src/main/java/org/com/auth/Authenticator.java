
package org.com.auth;

import java.util.Scanner;
import java.util.function.BiPredicate;
import java.util.function.Predicate;


public class Authenticator {
    private Scanner scanner = new Scanner(System.in);
    public Boolean isLogged = false;

    private void printMessage(String x) {
        System.out.println(x);
    }

    public void authProcessFor(int tries,
                               String passwordP,
                               String userName) {
        var isLoged = false;
        while (! isLoged && tries > 0) {
            isLoged = authLogic().test(passwordP, userName);
            if(!isLoged){
                printMessage("you still have " + (tries - 1) + " tries left");
                tries--;
            }
        }
        isLogged = isLoged;
        authMessage();
    }


    private BiPredicate<String, String> authLogic() {
        return (passwordP, userNameP) -> {
            printMessage("Enter User Name");
            var userName = scanner.next();
            printMessage("Enter Password");
            var password = scanner.next();
            return userName.equals(userNameP) && password.equals(passwordP);
        };
    }

    public void authMessage() {
        if (! isLogged) {
            printMessage("Sorry, max try possible");
        } else {
            printMessage("Welcome ");
        }
    }
}
