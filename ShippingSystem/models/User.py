
class User:

    username: str
    password: str
    logged_in: bool
    blocked: bool

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.logged_in = False
        self.blocked = False

    def login_user(self) -> bool:

        if self.blocked:
            print("Account blocked")
            return False

        attempts: int = 3
        while not self.logged_in:
            username = input("Username: ")
            password = input("Password: ")
            if self.username != username or self.password != password:
                attempts -= 1
                print(f"Incorrect login, remaining attempts: {attempts}")
                if attempts == 0:
                    print("Account blocked")
                    self.blocked = True
            else:
                print("Successfully logged in")
                self.logged_in = True

        return self.logged_in


