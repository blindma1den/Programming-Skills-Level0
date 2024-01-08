from models.User import User


class Bank(object):
    users: dict[str, User]

    def __init__(self, users=None):
        if users is None:
            users = {}
        self.users = users

    def menu(self):
        print("BANKING SYSTEM")
        print("1. Register new account")
        print("2. Login")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Transfer")
        print("6. View")
        option = int(input(">> "))
        return option

    def login(self) -> User:

        attempts: int = 3
        while attempts != 0:
            username = input("Username: ")
            password = input("Password: ")

            if username not in self.users:
                print("User not registered")
                continue

            user = self.users.get(username)

            if user.username == username and user.password == password:
                print("Successfully logged in")
                return user
            else:
                print("Incorrect credentials")
                attempts -= 1
                if attempts == 0:
                    user.is_blocked = True
                    print("Your account will be blocked for security reasons")

        return None

    def register_user(self, user: User):
        if user.username not in self.users.keys():
            self.users.update({user.username: user})
        else:
            print("User already registered")

    def transfer(self, origin_account: User, destination_account: str, amount: float) -> bool:

        if origin_account.username not in list(self.users.keys()) or destination_account not in list(self.users.keys()):
            print("Account not registered")
            return False

        if origin_account.balance < amount:
            print("Not enough funds to perform transfer")
            return False

        if origin_account.is_blocked or self.users.get(destination_account).is_blocked:
            print("Account blocked, transform cannot be performed")
            return False

        origin_account.withdraw(amount)
        self.users.get(destination_account).deposit(amount)

        return True
