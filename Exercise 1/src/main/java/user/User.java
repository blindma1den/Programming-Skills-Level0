package user;

public class User {
    private String password;
    private String username;
    private String firstName;
    private String lastName;

    public User(String password, String username, String firstName, String lastName) {
        this.password = password;
        this.username = username;
        this.firstName = firstName;
        this.lastName = lastName;
    }
    private User() {
        this("","","","");
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}
