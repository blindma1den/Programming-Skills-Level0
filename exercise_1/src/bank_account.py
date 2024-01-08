class BankAccount:
    def __init__(self, username, password, account_id, balance=0):
        self._balance = balance
        self._username = username
        self._password = password
        self._account_id = account_id

    @property
    def username(self):
        """The username property (read-only)."""
        return self._username

    @property
    def password(self):
        """The password property (read-only)."""
        return self._password

    @property
    def account_id(self):
        """The account_id property (read-only)."""
        return self._account_id

    @property
    def balance(self):
        """The balance for the account."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    def __str__(self):
        """Return the details for the account."""
        account_details = "Account details:\n"
        account_details += f"Username: {self.username}\n"
        account_details += f"Account number: {self.account_id}"
        account_details += f"Balance: {self.balance}"
        return account_details

    def withdraw(self):
        """Check if the amount is correct and makes the withdraw."""
        print("Withdraw.\n")
        valid_amount = False
        while not valid_amount:
            amount = float(input("Amount to withdraw: "))
            if amount <= 0 or amount > self.balance:
                print("Invalid quantity. Please try again.\n")
            else:
                valid_amount = True
        self.balance -= amount
        print(f"Withdraw success. New balance: {self.balance}.")

    def show_balance(self):
        """Prints the balance."""
        print("Show balance.\n")
        print(f"Your balance is: ${self.balance}")

    def deposit(self):
        """Check valid amount and deposits."""
        print("Deposit.\n")
        valid_amount = False
        while not valid_amount:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Invalid amount, try again.")
            else:
                valid_amount = True
                self.balance += amount
        print(f"Deposit success. New balance: ${self.balance}.")

    def transference(self, other_accounts):
        """Checks for valid account and amount. Then makes transference."""
        print("Transference.\n")
        valid_account = False
        valid_amount = False
        while not valid_account and not valid_amount:
            destiny_account = input("Account to transfer: ")
            amount = float(input("Amount: "))
            amount_check = amount > 0 and amount <= self.balance
            if destiny_account in other_accounts and amount_check:
                print("Data verified successfuly. Making transference.")
                valid_account = True
                valid_amount = True
                self.balance -= amount
                print(f"New balance: ${self.balance}.")
            else:
                print("Invalid data. Please try again.")
