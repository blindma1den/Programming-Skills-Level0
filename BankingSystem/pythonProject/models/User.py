class User(object):
    username: str
    password: str
    is_blocked: bool
    balance: float = 2000

    def __init__(self, username: str, password: str, is_blocked=False, balance=2000):
        self.username = username
        self.password = password
        self.balance = balance
        self.is_blocked = is_blocked

    def deposit(self, amount: float) -> bool:
        self.balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if self.balance - amount < 0:
            print("Not enough available funds")
            return False
        else:
            self.balance -= amount
            return True

    def view(self) -> None:
        print(f"Your balance is {self.balance}")


