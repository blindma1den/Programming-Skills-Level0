package Level_0_Challenges.Challenge_01;

public class User {

    private String userName;
    private String userPassword;
    private double userBalance;


    public User(String userName, String userPassword) {
        this.userName = userName;
        this.userPassword = userPassword;
        this.userBalance = 2000;
    }

    public String getUserName() {
        return userName;
    }

    public String getUserPassword() {
        return userPassword;
    }

    public double getUserBalance() {
        return userBalance;
    }

    public void deposit(double quantity) {
        userBalance += quantity;
        System.out.println("Successful deposit!");
    }

    public void withdraw(double quantity) {
        if (quantity <= userBalance) {
            userBalance -= quantity;
            System.out.println("Successful withdrawal!");
        } else {
            System.out.println("Insufficient Funds :(");
        }
    }

    public void transfer(User recipientUser, double quantity) {
        if (quantity > 0 && quantity <= userBalance) {
            userBalance -= quantity;
            recipientUser.userBalance += quantity;
            System.out.println("Successful transfer!");
        } else {
            System.out.println("Invalid transfer amount or insufficient funds to complete the transfer");
        }
    }

    public void viewBalance() {
        System.out.println("Current balance: $" + userBalance);
    }
}
