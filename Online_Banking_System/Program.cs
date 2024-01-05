namespace Online_Banking_System;

static class Program
{
    const string USER = "bankuser";
    const string PASSWORD = "123456*";
    const int EXIT_OPTION = 5;
    const int MAXIMUM_ATTEMPTS = 3;
    const decimal INITIAL_BALANCE = 2000;
    const string USER_TRANSFER = "usuario2";
    const decimal USER_TRANSFER_INITIAL_BALANCE = 2000;
    static decimal USER_ACTUAL_BALANCE = INITIAL_BALANCE;

    public static void Main(string[] args)
    {
        if(!login_success())
        {
            Console.WriteLine("");
            Console.WriteLine("You has used maximum attempts to login. Try again later.");
            Console.WriteLine("Thanks by using our services");
            return;
        }

        int optionSelected = 0;
        while (optionSelected!= EXIT_OPTION)
        {
            Console.Clear();
            showMenu();
            optionSelected = int.Parse(Console.ReadLine());
            Console.WriteLine("");

            switch(optionSelected) 
            {
                case 1: // Deposit
                    depositTransaction();
                    break;
                case 2: // Withdraw
                    withdrawTransaction();
                    break;
                case 3: // View
                    viewTransaction();
                    break;
                case 4: // Transfer
                    transferTransaction();
                    break;
                case 5: // Exit
                    Console.WriteLine("Thanks by using our services");
                    break;
                default:
                    Console.WriteLine("Wrong option, try again");
                    Console.WriteLine("");
                    optionSelected = int.Parse(Console.ReadLine());
                    Console.WriteLine("");
                    break;
            } // switch
        }  // while
    } // main

    static bool login_success()
    {
        int loginAttempts = 0;
        bool grantedAccess = false;

        while(loginAttempts<=MAXIMUM_ATTEMPTS)
        {
            Console.Clear();
            Console.WriteLine("Input username");
            string username = Console.ReadLine();
            Console.WriteLine("Input password");
            string password = Console.ReadLine();


            if(username==USER)
            {
                if(password==PASSWORD)
                {
                    grantedAccess=true;
                    break;
                } 
                else 
                {
                    loginAttempts += 1;
                    Console.WriteLine("Wrong password. Try again. Press a key to continue");
                    Console.ReadLine();
                } //(password==PASSWORD)
            } 
            else 
            {
                loginAttempts += 1;
                Console.WriteLine("User does not exist. Try again. Press a key to continue");
                Console.ReadLine();
            } // (username==USER)
        } // (loginAttempts<=MAXIMUM_ATTEMPTS)

        return grantedAccess;
    }

    static void showMenu() 
    {
        Console.WriteLine($"User: {USER}");
        Console.WriteLine("--------------");
        Console.WriteLine("Operations");
        Console.WriteLine("--------------");
        Console.WriteLine("1. Deposit");
        Console.WriteLine("2. Withdraw");
        Console.WriteLine("3. View");
        Console.WriteLine("4. Transfer");
        Console.WriteLine("--------------");
        Console.WriteLine("");
        Console.WriteLine("Select an option (Press 5 to Exit): ");
    }

    static void depositTransaction() 
    {
        Console.Clear();
        Console.WriteLine("Deposit");
        Console.WriteLine("----------");
        Console.WriteLine($"Actual Balance: {USER_ACTUAL_BALANCE}");
        Console.WriteLine("Input amount to deposit");
        decimal depositAmount = decimal.Parse(Console.ReadLine());
        decimal previousBalance = USER_ACTUAL_BALANCE;
        USER_ACTUAL_BALANCE += depositAmount;

        Console.WriteLine("Operation Succesful");
        Console.WriteLine("----------");
        Console.WriteLine($"Previous Balance: {previousBalance}");
        Console.WriteLine($"Deposit Amount: {depositAmount}");
        Console.WriteLine($"Actual Balance: {USER_ACTUAL_BALANCE}");
        Console.WriteLine("");
        Console.WriteLine("Press a key to continue");
        Console.ReadLine();
    }

    static void withdrawTransaction() 
    {
        Console.Clear();
        Console.WriteLine("Withdraw");
        Console.WriteLine("----------");
        Console.WriteLine($"Actual Balance: {USER_ACTUAL_BALANCE}");
        Console.WriteLine("Input amount to withdraw");
        decimal withdrawAmount = decimal.Parse(Console.ReadLine());
        
        if(withdrawAmount > USER_ACTUAL_BALANCE)
        {
            Console.WriteLine("Unable to make withdraw. Insufficient funds.");
            Console.WriteLine("");
            Console.WriteLine("Press a key to continue");
            Console.ReadLine();
            return;
        }
        
        decimal previousBalance = USER_ACTUAL_BALANCE;
        USER_ACTUAL_BALANCE -= withdrawAmount;

        Console.WriteLine("");
        Console.WriteLine("Operation Succesful");
        Console.WriteLine("----------");
        Console.WriteLine($"Previous Balance: {previousBalance}");
        Console.WriteLine($"Withdraw Amount: {withdrawAmount}");
        Console.WriteLine($"Actual Balance: {USER_ACTUAL_BALANCE}");

        Console.WriteLine("");
        Console.WriteLine("Press a key to continue");
        Console.ReadLine();
    }

    static void viewTransaction() 
    {
        Console.Clear();
        Console.WriteLine("View Balance");
        Console.WriteLine("----------");
        Console.WriteLine($"Actual Balance: {USER_ACTUAL_BALANCE}");
        Console.WriteLine("----------");

        Console.WriteLine("");
        Console.WriteLine("Press a key to continue");
        Console.ReadLine();
    }

    static void transferTransaction() 
    {
        Console.Clear();
        Console.WriteLine("Transfer Funds");
        Console.WriteLine("----------");
        Console.WriteLine($"Actual Balance: {USER_ACTUAL_BALANCE}");
        Console.WriteLine("Input username to transfer");
        string usernameToTransfer = Console.ReadLine();
        Console.WriteLine("Input amount to transfer");
        decimal transferAmount = decimal.Parse(Console.ReadLine());

        if(transferAmount > USER_ACTUAL_BALANCE)
        {
            Console.WriteLine("Unable to make transfer. Insufficient funds.");
            Console.WriteLine("");
            Console.WriteLine("Press a key to continue");
            Console.ReadLine();
            return;
        }

        decimal previousBalance = USER_ACTUAL_BALANCE;
        USER_ACTUAL_BALANCE -= transferAmount;

        Console.WriteLine("");
        Console.WriteLine("Operation Succesful");
        Console.WriteLine("----------");
        Console.WriteLine($"Previous Balance: {previousBalance}");
        Console.WriteLine($"Transfer Amount: {transferAmount}");
        Console.WriteLine($"Username Transfer Destination: {usernameToTransfer}");
        Console.WriteLine($"Actual Balance: {USER_ACTUAL_BALANCE}");

        Console.WriteLine("");
        Console.WriteLine("Press a key to continue");
        Console.ReadLine();
    }
} // program