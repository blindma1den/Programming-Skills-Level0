income = {
    'Total Income': 0
}

expenses = {
    'Medical expenses': 0,
    'Household expenses': 0,
    'Leisure': 0,
    'Savings': 0,
    'Education': 0
}

def record_income():
    total_income = float(input("Enter your total income: $"))
    income['Total Income'] = total_income

def record_expenses():
    print("Expense Categories:")
    for category in expenses.keys():
        expense = float(input(f"Enter your expense for {category}: $"))
        expenses[category] = expense

def calculate_category_totals():
    category_totals = {}
    for category, expense in expenses.items():
        category_totals[category] = expense
    return category_totals

def calculate_total_expenses():
    total_expenses = sum(expenses.values())
    return total_expenses

def analyze_financial_health():
    total_income = income['Total Income']
    total_expenses = calculate_total_expenses()

    if total_expenses == total_income:
        max_expense_category = max(expenses, key=expenses.get)
        print("You have spent the same amount you earn.")
        print(f"Consider reducing expenses in the {max_expense_category} category.")
    elif total_expenses < total_income:
        print("Congratulations! You are spending less than you earn.")
    else:
        print("You are spending more than you earn.")
        print("Consider improving your financial health by reducing expenses or increasing income.")

def main5():
    record_income()
    record_expenses()
    
    category_totals = calculate_category_totals()
    total_expenses = calculate_total_expenses()
    
    print("Category Totals:")
    for category, total in category_totals.items():
        print(f"{category}: ${total}")
    
    print("Total Expenses: $", total_expenses)
    
    analyze_financial_health()

main5()