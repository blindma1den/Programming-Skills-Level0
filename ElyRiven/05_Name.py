# 5. Develop a finance management application with the following features:
# *		The user records their total income.
# *		There are categories: Medical expenses, household expenses, leisure, savings, and education.
# *		The user can list their expenses within the categories and get the total for each category.
# *		The user can obtain the total of their expenses.
# *		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
# *		If the user spends less than they earn, the system displays a congratulatory message on the screen.
# *		If the user spends more than they earn, the system will display advice to improve the user's financial health.

def main():
    endProgramm = False
    print("\t\tWelcome to Save Finance\n\n")
    user = getIncome()
    while not endProgramm:
        chosedOption = None
        while chosedOption == None:
            print(f'Your total expenses: ${user.getTotalExpenses()}\n')
            chosedOption = mainMenu()
        if chosedOption == 1:
            print('Please select a category for record your expenses\n')
            print('Medical expenses [me] - Household expenses [he] - Leisure [l] - Savings [s] - Education [e]')
            category = getCategory()
            if category != None:
                expense = float(input('Insert your expenses: '))
                if category == 'medical expenses':
                    user.addMedicalExpenses(expense)
                if category == 'household expenses':
                    user.addHouseholdExpenses(expense)
                if category == 'leisure':
                    user.addLeisureExpenses(expense)
                if category == 'savings':
                    user.addSavingsExpenses(expense)
                if category == 'education':
                    user.addEducationExpenses(expense)
            else:
                print('Invalid category')
        elif chosedOption == 2:
            print('Please select a category\n')
            print('Medical expenses [me] - Household expenses [he] - Leisure [l] - Savings [s] - Education [e]')
            category = getCategory()
            if category != None:
                if category == 'medical expenses':
                    print(f'Your medical expenses are: ${user.medicalExpenses}')
                if category == 'household expenses':
                    print(f'Your household expenses are: ${user.householdExpenses}')
                if category == 'leisure':
                    print(f'Your leisure expenses are: ${user.leisureExpenses}')
                if category == 'savings':
                    print(f'Your savings are: ${user.savingsExpenses}')
                if category == 'education':
                    print(f'Your education expenses are: ${user.educationExpenses}')
            else:
                print('Invalid category')
        elif chosedOption == 3:
            income = user.income
            expenses = user.getTotalExpenses()
            print(f'Your total income: ${income}\t<------->\tYour total expenses: ${expenses}')
            if income == expenses:
                print(f'You should reduce your expenses on the category: {user.getMostExpenseCategory()[0]}\nYour expenses on this category: ${user.getMostExpenseCategory()[1]}')
            elif income > expenses:
                print('Congratulations! You have a healthy financial status. Remember to check your expenses often.\n')
            elif income < expenses:
                print('You should improve your financial health. You could start learning to budget your expenses, pay with cash instead cards and monitor your taxes\n')
        if chosedOption == 0:
            endProgramm = True
            continue

def getCategory():
    try:
        category = input()
        if category == 'me':
            return 'medical expenses'
        elif category == 'he':
            return 'household expenses'
        elif category == 'l':
            return 'leisure'
        elif category == 's':
            return 'savings'
        elif category == 'e':
            return 'education'
    except:
        print('Invalid Input')
        return None

def getIncome():
    try:
        value = float(input('Please insert your total income: '))
        return User(value)
    except:
        print('Please insert a valid number')

def mainMenu():
    print('What do you want to do?\n\nAdd Expenses [1] - List Expenses by Category [2] - Compare Income and Expenses [3] - Exit [0]')
    try:
        option = int(input())
        if option < 0 or option > 3:
            print('Please insert a valid option\n')
        else:
            return option
    except:
        print('Please insert a valid option\n')
        return None

class User:
    def __init__(self, income):
        self.income = income
        self.medicalExpenses = 0
        self.householdExpenses = 0
        self.leisureExpenses  = 0
        self.savingsExpenses   = 0
        self.educationExpenses = 0
        self.totalExpenses = 0

    def addMedicalExpenses(self, ammount):
        self.medicalExpenses += ammount
    
    def addHouseholdExpenses(self, ammount):
        self.householdExpenses += ammount
    
    def addLeisureExpenses(self, ammount):
        self.leisureExpenses += ammount

    def addSavingsExpenses(self, ammount):
        self.savingsExpenses += ammount

    def addEducationExpenses(self, ammount):
        self.educationExpenses += ammount

    def getTotalExpenses(self):
        self.totalExpenses = self.medicalExpenses + self.householdExpenses + self.leisureExpenses + self.savingsExpenses + self.educationExpenses
        return self.totalExpenses

    def getMostExpenseCategory(self):
        mostExpense = 0
        category = ''
        if self.medicalExpenses > mostExpense:
            mostExpense = self.medicalExpenses
            category = 'medical expenses'
        if self.householdExpenses > mostExpense:
            mostExpense = self.householdExpenses
            category = 'household expenses'
        if self.leisureExpenses > mostExpense:
            mostExpense = self.leisureExpenses
            category = 'leisure expenses'
        if self.savingsExpenses > mostExpense:
            mostExpense = self.savingsExpenses
            category = 'savings expenses'
        if self.educationExpenses > mostExpense:
            mostExpense = self.educationExpenses
            category = 'education expenses'
        return category, mostExpense

if __name__ == "__main__":
    main()