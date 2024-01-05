namespace Online_Shipping_System;

class Program
{
    const string USER = "system";
    const string PASSWORD = "123456*";
    const int EXIT_OPTION = 2;
    const int MAXIMUM_ATTEMPTS = 3;
    const decimal SHIPPING_PRICE = 2.00M;
    static void Main(string[] args)
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
                case 1: // Send Package
                    sendingOperation();
                    break;
                case EXIT_OPTION: // Exit
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
    }

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
        Console.WriteLine("1. Send package");
        Console.WriteLine("--------------");
        Console.WriteLine("");
        Console.WriteLine("Select an option (Press 2 to Exit): ");
    }

    static void sendingOperation()
    {
        Console.WriteLine("Sending a package: ");
        Console.WriteLine("-------------------");
        Console.WriteLine("Input sender name: ");
        string nameSender = Console.ReadLine();
        Console.WriteLine("Input sender address: ");
        string addressSender = Console.ReadLine();
        Console.WriteLine("Input recipient name: ");
        string nameRecipient = Console.ReadLine();
        Console.WriteLine("Input recipient address: ");
        string addressRecipient = Console.ReadLine();
        Console.WriteLine("-------------------");
        Console.WriteLine("Package details");
        Console.WriteLine("-------------------");
        Console.WriteLine("Input weight package");
        decimal weightPackage = decimal.Parse(Console.ReadLine());
        decimal totalPrice = weightPackage * SHIPPING_PRICE;

        Console.WriteLine("Confirm operation (y/n)? ");
        string confirmation = Console.ReadLine();

        if(confirmation.ToLower() == "n")
        {
            return;
        }

        Console.WriteLine("Transaction confirmed.");
        Console.WriteLine($"Total payment: {totalPrice}");

        Console.WriteLine("Do you want to perform another operation (y/n)? ");
        string anotherOperation = Console.ReadLine();

        if(anotherOperation.ToLower() == "n")
        {
            return;
        }
    }

}