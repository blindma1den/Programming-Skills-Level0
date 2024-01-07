username = "pepe"
password = "123"


def login():
    """Ask up to three times the user for credentials. If success then log in
    else the program terminates."""


# Bienvenida
print("Welcome to your favorite home-banking system")
print("To continue please log in:")

# Login
login_tries_left = 3
logged_in = False

while login_tries_left > 0 and not logged_in:
    print(f"\nYou have {login_tries_left} tries left. Be careful.")
    username_input = input("\nUsername:\n")
    password_input = input("\nPassword:\n")
    if username == username_input and password == password_input:
        print(f"Welcome")
        logged_in = True
    else:
        login_tries_left -= 1

if not logged_in:
    print(
        "You have entered your credentials wrong three times. For security reasons"
        + " your access is blocked. gl hf with the support bud."
    )
