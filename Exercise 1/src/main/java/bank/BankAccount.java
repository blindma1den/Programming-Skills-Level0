package bank;

import login.LoginInterface;
import user.User;

public class BankAccount extends User implements LoginInterface {

    private Integer balance;

    public BankAccount(String password, String username, String firstName, String lastName) {
        super(password, username, firstName, lastName);
    }

    @Override
    public boolean validatePassword(String p) {
        return p.equals(this.getPassword());
    }

    public Integer getBalance() {
        return this.balance;
    }
    public void addBalance(Integer amount) {
        this.balance += amount;
    }
    public boolean withdrawBalance(Integer amount) {
        if ( amount > this.balance ) {
            return false;
        } else {
            this.balance -= amount;
            return true;
        }
    }
    public boolean transferBalance(Integer amount, BankAccount toAccount) {
        if ( amount > this.balance ) {
            return false;
        } else {
            this.balance -= amount;
            toAccount.addBalance(amount);
            return true;
        }
    }




}
