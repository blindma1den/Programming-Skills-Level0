def main_menu():
    print("Welcome to the main menu!")
    print("Type the number of the exercise that you want to execute:")

    choice = input("Enter your choice: ")

    if choice == "1":
        from exercise1.main import main1
    elif choice == "2":
        from exercise2.main import main2
    elif choice == "3":
        from exercise3.main import main3
    elif choice == "4":
        from exercise4.main import main4
    elif choice == "5":
        from exercise5.main import main5
    else:
        print("Invalid choice. Please try again.")
        main_menu()

main_menu()
