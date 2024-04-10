using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace L0E5
{

    /*
        Develop a finance management application with the following features:

* 		The user records their total income.
* 		
* 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
* 		
* 		The user can list their expenses within the categories and get the total for each category.
* 		The user can obtain the total of their expenses.
* 		
* 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce 
* 		expenses in the category where they have spent the most money.
* 		
* 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
* 		
* 		If the user spends more than they earn, the system will display advice to improve the user's financial health.

     
     */
    internal class FinanceApp
    {
        static decimal medicalExpense;
        static decimal householdExpense;
        static decimal leisureExpense;
        static decimal savingsExpense;
        static decimal eduExpense;
        static decimal totalIncome;
        static decimal totalExpenses;
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Downtown Finance System");
            Console.WriteLine("Please, type your total income: ");
            totalIncome = decimal.Parse(Console.ReadLine());

            int youSure = 1;
            while (youSure == 1)
            {
                
                    Console.WriteLine("Select an expense type (MEDICAL,HOUSEHOLD,LEISURE,SAVINGS,EDUCATION): ");
                    string expenseType = Console.ReadLine();
                    Console.WriteLine("Input amount: ");
                    decimal expenseAmount = decimal.Parse(Console.ReadLine());

                    switch (expenseType.ToUpper())
                    {
                        case "MEDICAL":
                            medicalExpense += expenseAmount;
                            break;
                        case "HOUSEHOLD":
                            householdExpense += expenseAmount;
                            break;
                        case "LEISURE":
                            leisureExpense += expenseAmount;
                            break;
                        case "SAVINGS":
                            savingsExpense += expenseAmount;
                            break;
                        case "EDUCATION":
                            eduExpense += expenseAmount;
                            break;
                        default:
                            Console.WriteLine("Wrong expense choice. Try another");
                            break;
                    }

                    Console.WriteLine("Do you want to register another expense \n1.YES\n2.NO");
                youSure = Convert.ToInt32(Console.ReadLine());
               
            } //while

            showFinalResults();

        }

        static void showFinalResults()
        {
            totalExpenses = medicalExpense + householdExpense + leisureExpense + savingsExpense + eduExpense;

            if (totalExpenses == totalIncome)
            {
                Console.WriteLine($"You should be careful with your expenses in the category {totalIncome}");
                Console.WriteLine("Press any key to continue...");
                Console.ReadKey();
            }

            if (totalExpenses > totalIncome)
            {
                Console.WriteLine("You need to improve your financial health");
                Console.WriteLine("Press any key to continue...");
                Console.ReadKey();
            }

            if (totalExpenses < totalIncome)
            {
                Console.WriteLine("Excellent! you have an excellent financial health");
                Console.WriteLine("Press any key to continue...");
                Console.ReadKey();
            }

            Console.WriteLine("------------------------RESULTS-------------------------------");
            Console.WriteLine($"Total Income: {totalIncome} / Total Expenses: {totalExpenses}");
            Console.WriteLine("Press any key to exit the system...");
            Console.ReadKey();
        }
    }
}
