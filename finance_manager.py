'''Develop a finance management application with the following features:
* 		The user records their total income.
* 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
* 		The user can list their expenses within the categories and get the total for each category.
* 		The user can obtain the total of their expenses.
* 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
* 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
* 		If the user spends more than they earn, the system will display advice to improve the user's financial health.'''

expenses_list={"Medical expenses":0, "Household expenses":0, "Leisure":0, "Savings":0, "Education":0}

def add_expenses():
    for item in expenses_list:
        expenses_list[item]=int(input(f"how much do you expend in {item}. "))

def total_expenses(expenses_list:dict)->int:   
    return sum(expenses_list.values())

def get_max_expense()->int:
    return max(expenses_list, key=expenses_list.get)



def main():
    income = int(input("insert your total income. "))
    add_expenses()
    if income > total_expenses(expenses_list):
        print("Congrats! You have excelent financial health.")
    elif income == total_expenses(expenses_list):
        print(f"You're barely okay. I recommend you to reduce your expenses in {get_max_expense()}")
    elif income < total_expenses(expenses_list):
        print(f"Yikes! you have a terible financial health, you should reduce your expenses a little... mainly in {get_max_expense()}")
    print(f"Here your total expenses: {total_expenses(expenses_list)}.\n and your list of individual expenses: {expenses_list}")


if __name__=="__main__":
    main()