namespace Finance_Management_Application;

class Program
{
    static decimal medical;
    static decimal household;
    static decimal leisure;
    static decimal savings;
    static decimal education;
    static decimal totalIncome;
    static decimal totalExpenses;
    static void Main(string[] args)
    {
        Console.WriteLine("Finance Management Application");
        Console.WriteLine("------------------------------");
        Console.WriteLine("Input total income: ");
        totalIncome = decimal.Parse(Console.ReadLine());

        Console.WriteLine("Input expenses. Select an expense type and input amount");
        Console.WriteLine("-------------------------------------------------------");

        string confirmation = "y";
        while(confirmation == "y")
        {
            Console.WriteLine("Select an expense type (MEDICAL,HOUSEHOLD,LEISURE,SAVINGS,EDUCATION): ");
            string expenseType = Console.ReadLine();
            Console.WriteLine("Input amount: ");
            decimal expenseAmount = decimal.Parse(Console.ReadLine());

            switch (expenseType)
            {
                case "MEDICAL":
                    medical += expenseAmount;
                    break;
                case "HOUSEHOLD":
                    household += expenseAmount;
                    break;
                case "LEISURE":
                    leisure += expenseAmount;
                    break;
                case "SAVINGS":
                    savings += expenseAmount;
                    break;
                case "EDUCATION":
                    education += expenseAmount;
                    break;
                default:
                    Console.WriteLine("Wrong expense choice. Try another");
                    break;
            }

            Console.WriteLine("Do you want to register another expense (y/n)?: ");
            confirmation = Console.ReadLine();
        }

        showFinalResults();

    }

    static void showFinalResults()
    {
        totalExpenses = medical + household + leisure + savings + education;

        if(totalExpenses==totalIncome)
        {
            Console.WriteLine($"You should to reduce your expenses in the category {totalIncome}");
        }

        if(totalExpenses>totalIncome)
        {
            Console.WriteLine("You need to improve your financial health");
        }

        if(totalExpenses<totalIncome)
        {
            Console.WriteLine("Excellent! you have an excellent financial health");
        }

        Console.WriteLine($"Total Income: {totalIncome} / Total Expenses: {totalExpenses}");
    }

    static string majorExpenseCategory()
    {
        return "";
    }

    static decimal majorAmountExpenseCategory(string nameExpenseCategory)
    {
        return 0;
    }
}
