def main():
    categories = [
        "Medical expenses",
        "Household expenses",
        "Leisure",
        "Education",
        "Savings"
    ]
    print("-------FINANCE MANAGEMENT SYSTEM------")
    income = float(input("Let us know your income: $"))
    register_category: bool = True
    expenses = dict()
    while register_category:

        option = input("Do you want to register an expense? y/n: ")
        if option.upper() != "Y":
            register_category = False
            continue

        for index, category in enumerate(categories):
            print(f"{index + 1}. {category}")

        option = int(input("Category: "))
        if option > len(categories):
            print("Error, fail on category input")
        else:
            print(f"Expense on {categories[option - 1]}")
            amount = float(input("Expense amount: "))
            expenses.update({categories[option - 1]: amount})

    print("Registered epxenses: ")
    print(expenses)
    total_expense = sum(list(expenses.values()))
    print(f"Total expense: {total_expense}" )

    if total_expense - income == 0:
        max_expense = max(list(expenses.values()))
        max_index = list(expenses.values()).index(max_expense)
        max_cat = list(expenses.keys())[max_index]
        print(f"Reduce your expenses in {max_cat}")
    elif total_expense - income > 0:
        print("Improve your financial health")
    else:
        print("Congratulations!! You are saving money")


if __name__ == "__main__":
    main()