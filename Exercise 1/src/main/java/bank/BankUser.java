package bank;

import login.LoginInterface;
import user.User;

public class BankUser extends User implements LoginInterface {
    public BankUser(String password, String username, String firstName, String lastName) {
        super(password, username, firstName, lastName);
    }
    
    @Override
    public boolean validatePassword(String p) {
        return p.equals(this.getPassword());
    }
}
