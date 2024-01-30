#Exercise 5#
#!Develop a finance management application with the following features:
#|The user records their total income.
#|There are categories: Medical expenses, household expenses, leisure, savings, and education.
#|The user can list their expenses within the categories and get the total for each category.
#|The user can obtain the total of their expenses.
#?If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
#?If the user spends less than they earn, the system displays a congratulatory message on the screen.
#?If the user spends more than they earn, the system will display advice to improve the user's financial health.

user_expenses = {
    "Medical expenses" : 0,
    "Household expenses" : 0,
    "Leisure" : 0,
    "Savings" : 0,
    "Education" : 0
}

def register(category):
    expenses = input(f"Enter your expenses for '{category}': $")
    if(expenses.isnumeric()):
        return int(expenses)
    else:
        print("Invalid input")
        return register(category)

def display_message(income, expenses):
    if(expenses == income):
        max = 0
        category = ""
        for e,f in user_expenses.items():
            if f > max:
                max = f
                category = e
            else:
                pass
        return f"Reduce your expenses in '{category}'"
    elif(expenses > income):
        return "Alert: Evaluate your spending and savings habits to achieve better financial well-being"
    elif(expenses < income):
        return "Great job! Your expenses are below your income. Keep up the good financial habits!"

def main(income):
    print("Welcome!")
    while True:
        print("=" * 100)
        expenses = 0
        
        for e in user_expenses.values():
            expenses += e

        print(f"Income: ${income} /// Expenses: ${expenses}")
        print(display_message(income, expenses))

        x = 1
        for i, j in user_expenses.items():
            print(f"{x}. {i}: ${j}")
            x+=1
        print("6. Change income")

        selection = input("In which category would you like to register your expenses?: ")
        match selection:
            case "1":
                user_expenses["Medical expenses"] = register("Medical expenses")
            case "2":
                user_expenses["Household expenses"] = register("Household expenses")
            case "3":
                user_expenses["Leisure"] = register("Leisure")
            case "4":
                user_expenses["Savings"] = register("Savings")
            case "5":
                user_expenses["Education"] = register("Education")
            case "6":
                new_income = input("Insert your total income: $")
                if new_income.isnumeric():
                    income = int(new_income)
                else:
                    print("Invalid input")
            case _:
                print("Invalid input")

while True:
    income = input("Insert your total income: $")
    if income.isnumeric():
        main(int(income))
        break
    else:
        print("Invalid input")