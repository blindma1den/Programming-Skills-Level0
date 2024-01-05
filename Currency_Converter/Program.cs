namespace Currency_Converter;

public class Program
{
    const int EXIT_OPTION = 4;
    const decimal TAX = 0.01M;
    static Dictionary<string, decimal> UserBalance = new Dictionary<string, decimal>();
    static Dictionary<string, decimal> ARS_CurrencyChart = new Dictionary<string, decimal>();
    static Dictionary<string, decimal> CLP_CurrencyChart = new Dictionary<string, decimal>();
    static Dictionary<string, decimal> USD_CurrencyChart = new Dictionary<string, decimal>();
    static Dictionary<string, decimal> EUR_CurrencyChart = new Dictionary<string, decimal>();
    static Dictionary<string, decimal> TRY_CurrencyChart = new Dictionary<string, decimal>();
    static Dictionary<string, decimal> GBP_CurrencyChart = new Dictionary<string, decimal>();

    public static void Main(string[] args)
    {

        // Creating dictionaries with data
        chargeData();

        // User balance
        
        Console.WriteLine("Input your initial funds: ");
        decimal initialFunds = decimal.Parse(Console.ReadLine());
        Console.WriteLine("Select your currency to make transactions (CLP,ARS,USD,EUR,TRY,GBP): ");
        string selectedUserCurrency = Console.ReadLine();
        UserBalance[selectedUserCurrency] = initialFunds;
        
        int selectedOption = 0;
        while(selectedOption!=EXIT_OPTION)
        {
            Console.Clear();
            showMenu();
            selectedOption = int.Parse(Console.ReadLine());

            switch(selectedOption) 
            {
                case 1: // Exchange
                    exchangeOperation();
                    break;
                case 2: // Withdraw
                    withdrawOperation();
                    break;
                case 3: // View Balance
                    showUserBalance(UserBalance);
                    break;
                case EXIT_OPTION: // Exit
                    Console.WriteLine("Thanks by using our services");
                    break;
                default:
                    Console.WriteLine("Wrong option, try again");
                    Console.WriteLine("");
                    selectedOption = int.Parse(Console.ReadLine());
                    Console.WriteLine("");
                    break;
            } // switch
        } // while
    } // Main

    static void chargeData()
    {
        // ARS
        ARS_CurrencyChart.Add("ARS", 0);
        ARS_CurrencyChart.Add("CLP", 1.0957M);
        ARS_CurrencyChart.Add("USD", 0.0012M);
        ARS_CurrencyChart.Add("EUR", 0.0011M);
        ARS_CurrencyChart.Add("TRY", 0.0366M);
        ARS_CurrencyChart.Add("GBP", 0.0009M);

        // CLP
        CLP_CurrencyChart.Add("ARS", 37.7756M);
        CLP_CurrencyChart.Add("CLP", 0);
        CLP_CurrencyChart.Add("USD", 0.0011M);
        CLP_CurrencyChart.Add("EUR", 0.0010M);
        CLP_CurrencyChart.Add("TRY", 0.0334M);
        CLP_CurrencyChart.Add("GBP", 0.0008M);

        // USD
        USD_CurrencyChart.Add("ARS", 811.7830M);
        USD_CurrencyChart.Add("CLP", 888.9752M);
        USD_CurrencyChart.Add("USD", 0);
        USD_CurrencyChart.Add("EUR", 0.9127M);
        USD_CurrencyChart.Add("TRY", 29.7602M);
        USD_CurrencyChart.Add("GBP", 0.7879M);

        // EUR
        EUR_CurrencyChart.Add("ARS", 889.4313M);
        EUR_CurrencyChart.Add("CLP", 974.4397M);
        EUR_CurrencyChart.Add("USD", 1.0958M);
        EUR_CurrencyChart.Add("EUR", 0);
        EUR_CurrencyChart.Add("TRY", 32.6174M);
        EUR_CurrencyChart.Add("GBP", 0.8633M);

        // TRY
        TRY_CurrencyChart.Add("ARS", 27.2777M);
        TRY_CurrencyChart.Add("CLP", 29.8747M);
        TRY_CurrencyChart.Add("USD", 0.0336M);
        TRY_CurrencyChart.Add("EUR", 0.0307M);
        TRY_CurrencyChart.Add("TRY", 0);
        TRY_CurrencyChart.Add("GBP", 0.0265M);

        // GBP
        GBP_CurrencyChart.Add("ARS", 1030.3050M);
        GBP_CurrencyChart.Add("CLP", 1128.3697M);
        GBP_CurrencyChart.Add("USD", 1.2691M);
        GBP_CurrencyChart.Add("EUR", 1.1582M);
        GBP_CurrencyChart.Add("TRY", 37.7757M);
        GBP_CurrencyChart.Add("GBP", 0);

        // USER - UserBalance Initialization
        UserBalance.Add("ARS", 0);
        UserBalance.Add("CLP", 0);
        UserBalance.Add("USD", 0);
        UserBalance.Add("EUR", 0);
        UserBalance.Add("TRY", 0);
        UserBalance.Add("GBP", 0);
    }

    static void showMenu() 
    {
        Console.WriteLine("Operations");
        Console.WriteLine("-----------");
        Console.WriteLine("1. Exchange");
        Console.WriteLine("2. Withdraw");
        Console.WriteLine("3. View balance");
        Console.WriteLine("4. Exit");
        Console.WriteLine("-----------");
        Console.WriteLine("Select an option (Press 4 to exit): ");
    }

    static void exchangeOperation()
    {
        Console.WriteLine("Exchange");
        Console.WriteLine("---------------");
        Console.WriteLine("Select currency to exchange (CLP,ARS,USD,EUR,TRY,GBP): ");
        string selectedExchangeCurrency = Console.ReadLine();
        Console.WriteLine("Input amount to convert: ");
        decimal amountToExchange = decimal.Parse(Console.ReadLine());
        Console.WriteLine("Select currency to exchange to (CLP,ARS,USD,EUR,TRY,GBP): ");
        string selectedExchangeToCurrency = Console.ReadLine();
        
        decimal taxRate;

        switch (selectedExchangeCurrency)
        {
            case "ARS":
                taxRate = ARS_CurrencyChart[selectedExchangeToCurrency];
                break;
            case "CLP":
                taxRate = CLP_CurrencyChart[selectedExchangeToCurrency];
                break;
            case "USD":
                taxRate = USD_CurrencyChart[selectedExchangeToCurrency];
                break;
            case "EUR":
                taxRate = EUR_CurrencyChart[selectedExchangeToCurrency];
                break;
            case "TRY":
                taxRate = TRY_CurrencyChart[selectedExchangeToCurrency];
                break;
            case "GBP":
                taxRate = GBP_CurrencyChart[selectedExchangeToCurrency];
                break;
            default:
                taxRate = -1;
                break;
        }

        decimal convertedAmount = amountToExchange * taxRate;
        UserBalance[selectedExchangeToCurrency] += convertedAmount;
        UserBalance[selectedExchangeCurrency] -= amountToExchange;

        Console.WriteLine("Operation Successful");
        Console.WriteLine("Press a key to continue");
        Console.ReadLine();
    }

    static void withdrawOperation()
    {
        Console.WriteLine("Withdraw");
        Console.WriteLine("---------------");
        Console.WriteLine("Select currency to withdraw");
        string selectedCurrency = Console.ReadLine();
        Console.WriteLine("Input amount to withdraw: ");
        decimal amount = decimal.Parse(Console.ReadLine());
        decimal tax = amount * TAX;
        UserBalance[selectedCurrency] -= (amount + tax);
        
        Console.WriteLine("Operation Succesful");
        Console.WriteLine($"New balance: {selectedCurrency}: {UserBalance[selectedCurrency]}");
        Console.WriteLine("Press a key to continue");
        Console.ReadLine();
    }

    static void showUserBalance(Dictionary<string,decimal> UserBalance)
    {
        foreach (var item in UserBalance)
        {
            if (item.Value > 0)
            {
                Console.WriteLine($"{item.Key}: {item.Value}");
            }
        }

        Console.WriteLine("Press a key to continue");
        Console.ReadLine();
    }

    static void exchangeOperation(string currency, decimal amount, string currencyTo, decimal amountTo)
    {

    }
}