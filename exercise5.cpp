/*5. Develop a finance management application with the following features:
 * 		The user records their total income.
 * 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
 * 		The user can list their expenses within the categories and get the total for each category.
 * 		The user can obtain the total of their expenses.
 * 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
 * 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
 * 		If the user spends more than they earn, the system will display advice to improve the user's financial health.
 */

#include <iostream>

using namespace std;

int total_income = 0, total_expenses = 0;

int expenses[5];
int higher = 0;
string categories[5] = {"medical", "household", "leisure", "savings", "education"};
string mayor_category = "";

int main()
{

    cout << "Welcome to the finance management application.  \n";
    cout << "Please type your total monthly income: ";
    cin >> total_income;
    cout << "Now you will type your total monthly expenses in the next categories: \n ";
    cout << "Type your medical expenses please: \n";
    cin >> expenses[0];
    cout << "Type your household expenses please: \n";
    cin >> expenses[1];
    cout << "Type your leisure expenses please: \n";
    cin >> expenses[2];
    cout << "Type your savings please: \n";
    cin >> expenses[3];
    cout << "Type your education expenses please: \n";
    cin >> expenses[4];

    for (int i = 0; i < 5; i++)
    {

        total_expenses += expenses[i];

        if (expenses[i] > higher) 
        {
            higher = expenses[i];
            mayor_category = categories[i];
        }
    }

    if ((total_income - total_expenses) == 0)
    {

        cout << "Hey! Your expenses and incomes are the same, please reduce your expenses in the " << mayor_category << " category.";
    }
    else if ((total_income - total_expenses) > 0)
    {

        cout << "Congratz!!!\n";
    }
    else
    {
        cout << "you have to improve your financial health!\n";
    }
}