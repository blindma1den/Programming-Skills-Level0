'''
5. Develop a finance management application with the following features:
*   The user records their total income.
*   There are categories: Medical expenses, household expenses, leisure, savings, and education.
*   The user can list their expenses within the categories and get the total for each category.
*   The user can obtain the total of their expenses.
*   If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
*   If the user spends less than they earn, the system displays a congratulatory message on the screen.
*   If the user spends more than they earn, the system will display advice to improve the user's financial health.

'''

global_expenses = {}

def finance():
    income= int(input('What is your total income(in $)? '))
    medical= int(input('How much are your medical expenses? '))
    household= int(input('How much are your household expenses? '))
    leisure= int(input('How much are your leisure expenses? '))
    savings= int(input('How much are your savings? '))
    education= int(input('How much are your educational expenses? '))
    


    expenses= { 'Medical': medical, 'Household': household, 'Leisure': leisure, 'Savings': savings, 'Education': education}
    global_expenses= expenses
    total_expenses = medical+household+leisure+savings+education
    print('Your total expenses is', total_expenses)
    if total_expenses < income:
        print('Congratulations your income is larger than your expenses. Keep it going!')
    elif total_expenses == income:
        print('You should not spend all your income. Maybe you should reduce your expenses.' )
    else:
        print('Your expenses are larger than your income. Be careful!')
        
if __name__ == "__main__":
    finance()
    
    
