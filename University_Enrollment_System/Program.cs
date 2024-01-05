namespace University_Enrollment_System;

class Program
{
    const string USER = "system";
    const string PASSWORD = "123456*";
    const int EXIT_OPTION = 5;
    const int MAXIMUM_ATTEMPTS = 3;
    //static string firstName;
    //static string lastName;
    static string selectedCampus = "";
    //static Dictionary<string,int> London = Dictionary<string,int>();
    //static Dictionary<string,int> Manchester = Dictionary<string,int>();
    //static Dictionary<string,int> Liverpool = Dictionary<string,int>();
    static int[] London = [1,1,1,1]; //Computer Science,Medicine,Marketing,Arts
    static int[] Manchester = [3,3,3,3]; //Computer Science,Medicine,Marketing,Arts
    static int[] Liverpool = [1,1,1,1]; //Computer Science,Medicine,Marketing,Arts
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
                case 1: // Computer Science
                    selectComputerScienceProgram();
                    break;
                case 2: // Medicine
                    selectMedicineProgram();
                    break;
                case 3: // Marketing
                    selectMarketingProgram();
                    break;
                case 4: // Arts
                    selectArtsProgram();
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
    } // Main

    static bool login_success()
    {
        int loginAttempts = 0;
        bool grantedAccess = false;

        while(loginAttempts<=MAXIMUM_ATTEMPTS)
        {
            Console.Clear();
            Console.WriteLine("Input username: ");
            string username = Console.ReadLine();
            Console.WriteLine("Input password: ");
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
                    Console.WriteLine("Wrong password. Try again. Press a key to continue...");
                    Console.ReadLine();
                } //(password==PASSWORD)
            } 
            else 
            {
                loginAttempts += 1;
                Console.WriteLine("User does not exist. Try again. Press a key to continue...");
                Console.ReadLine();
            } // (username==USER)
        } // (loginAttempts<=MAXIMUM_ATTEMPTS)

        return grantedAccess;
    }

    static void showMenu() 
    {
        Console.WriteLine("Select Program");
        Console.WriteLine("--------------");
        Console.WriteLine("Operations");
        Console.WriteLine("--------------");
        Console.WriteLine("1. Computer Science");
        Console.WriteLine("2. Medicine");
        Console.WriteLine("3. Marketing");
        Console.WriteLine("4. Arts");
        Console.WriteLine("--------------");
        Console.WriteLine("");
        Console.WriteLine("Select an option (Press 5 to Exit): ");
    }

    static void selectComputerScienceProgram()
    {
        
        Console.WriteLine("Select a campus");
        string campus = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":
               
                if (London[0] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "manchester":
                
                if (Manchester[0] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "liverpool":
                
                if (Liverpool[0] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment process");
        Console.WriteLine("------------------");
        Console.WriteLine("Input first name: ");
        string firstName = Console.ReadLine();
        Console.WriteLine("Input last name: ");
        string lastName = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":
                London[0] += -1;
                break;

            case "manchester":
                Manchester[0] += -1;
                break;

            case "liverpool":
                Liverpool[0] += -1;
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment successful");
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void selectMedicineProgram()
    {
        Console.WriteLine("Select a campus");
        string campus = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":

                if (London[1] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "manchester":

                if (Manchester[1] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "liverpool":

                if (Liverpool[1] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment process");
        Console.WriteLine("------------------");
        Console.WriteLine("Input first name: ");
        string firstName = Console.ReadLine();
        Console.WriteLine("Input last name: ");
        string lastName = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":
                London[1] += -1;
                break;

            case "manchester":

                Manchester[1] += -1;
                break;

            case "liverpool":

                Liverpool[1] += -1;
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment successful");
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void selectMarketingProgram()
    {
        Console.WriteLine("Select a campus");
        string campus = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":

                if (London[2] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "manchester":

                if (Manchester[2] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "liverpool":

                if (Liverpool[2] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment process");
        Console.WriteLine("------------------");
        Console.WriteLine("Input first name: ");
        string firstName = Console.ReadLine();
        Console.WriteLine("Input last name: ");
        string lastName = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":
                London[2] += -1;
                break;

            case "manchester":
                Manchester[2] += -1;
                break;

            case "liverpool":
                Liverpool[2] += -1;
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment successful");
        Console.WriteLine("Press a key to continue");
        Console.ReadLine();

    }

    static void selectArtsProgram() 
    {
        Console.WriteLine("Select a campus");
        string campus = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":

                if (London[3] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "manchester":

                if (Manchester[3] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            case "liverpool":

                if (Liverpool[3] == 0)
                {
                    Console.WriteLine("Not available slots in selected campus. Try with another");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                    return;
                }
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment process");
        Console.WriteLine("------------------");
        Console.WriteLine("Input first name: ");
        string firstName = Console.ReadLine();
        Console.WriteLine("Input last name: ");
        string lastName = Console.ReadLine();

        switch (campus.ToLower())
        {
            case "london":
                London[3] += -1;
                break;

            case "manchester":
                Manchester[3] += -1;
                break;

            case "liverpool":
                Liverpool[3] += -1;
                break;

            default:
                Console.WriteLine("Wrong campus selected");
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
                return;
                break;
        }

        Console.WriteLine("Enrollment successful");
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();

    }

}