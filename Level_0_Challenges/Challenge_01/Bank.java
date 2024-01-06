package Level_0_Challenges.Challenge_01;

import java.util.HashMap;
import java.util.Map;

public class Bank {
    private Map<String, User> users;

    public Bank() {
        users = new HashMap<>();
        users.put("Sara", new User("Sara","x123"));
        users.put("Sergio", new User("Sergio","z123"));
    }

    public User signIn(String userName, String userPassword) {
        User user = users.get(userName);

        if (user != null && user.getUserPassword().equals(userPassword)) {
            return user;
        } else {
            return null;
        }
    }

    public Map<String, User> getUsers() {
        return users;
    }
}
