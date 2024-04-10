using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace L0E3
{
    /* 3. Create an university enrollment system with the following characteristics:
   * - The system has a login with a username and password.                                                        DONE 
   * 
   * - If login information is incorrect three times, the system should be locked.                                 DONE
   * 
   * - Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.   DONE 
   * 
   * - The user must input their first name, last name, and chosen program.                                        DONE
   * 
   * - Each program has only 5 available slots. The system will store the data of each registered user, 
   *  and if it exceeds the limit, it should display a message indicating the program is unavailable.              DONE
   *  
   * - The user must choose a campus from three cities: London, Manchester, Liverpool.                             DONE
   * 
   * - In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool,     DONE
   * there is 1 slot per program.
   * 
   * - If the user selects a program at a campus that has no available slots, the system should display 
   * the option to enroll in the program at another campus.                                                        DONE
   
     */ 

    internal class Enrollment
    {
        //Login Variables
        const string user = "admin";
        const string password = "$ecurePass";
        const int attempts = 3;

        //Programs
        static int[] London = {1, 1, 1, 1};
        static int[] Manchester = {3, 3, 3, 3};
        static int[] Liverpool = {1, 1, 1, 1};


        static void Main(string[] args)
        {
            if (!Login())
            {
                Console.WriteLine("\nToo many tries! The Downtown Enrollment System has been blocked.\nPlease try again another time.");
                Console.WriteLine("\nPress Enter to close the system.");
                Console.ReadKey();
                return;
            }

            int optionSelected = 0;

            while (optionSelected != 5)
            {
                Console.Clear();
                MainMenu();
                optionSelected = int.Parse(Console.ReadLine());
                Console.WriteLine("");

                switch (optionSelected)
                {
                    //Computer Science
                    case 1:
                        csProgram();
                        break;
                    //Medicine
                    case 2:
                        medProgram();
                        break;
                    //Marketing
                    case 3:
                        artProgram();
                        break;
                    //Arts
                    case 4:
                        marProgram();
                        break;
                    //ExitApp
                    case 5:
                        Console.WriteLine("Thanks for using Downtonw Enrollment System.\n Press Enter to close the App.");
                        Console.ReadKey();
                        break;
                    //case default
                    default:
                        Console.WriteLine("Default\n");
                        optionSelected = int.Parse(Console.ReadLine());
                        Console.WriteLine("");
                        break;
                }
            }

        }

        static bool Login()
        {
            string logUser, logPass;
            int logAttempts = 0;
            bool grantedAccess = false;

            do
            {
                Console.Clear();
                Console.WriteLine("---LOG-IN---");
                Console.WriteLine("Welcome to Downtown Enrollment System.");
                Console.WriteLine("TYPE YOUR USERNAME:");
                logUser = Console.ReadLine();
                Console.WriteLine("TYPE YOUR PASSWORD");
                logPass = Console.ReadLine();

                if (logUser == user) // if typedUser equals to username then validate pass
                {
                    if (logPass == password) // if typedPass equals to Pass then grantedAcess = true
                    {
                        grantedAccess = true;
                        break;
                    }
                    else // else tell the user that typed pass is incorrect and subtract 1 of the 3 attempts.
                    {
                        Console.WriteLine("\nThe username or the password typed is incorrect or does not exist. Try again.");
                        Console.WriteLine("You have " + (attempts - logAttempts) + " attempts left.\nPress Enter to Try again.");
                        Console.ReadKey();
                        logAttempts++;

                    } //logPass == password
                }
                else // else tell the user that typed username is incorrect and subtract 1 of the 3 attempts.
                {                   
                    Console.WriteLine("\nThe username or the password typed is incorrect or does not exist. Try again.");
                    Console.WriteLine("You have " + (attempts - logAttempts) + " attempts left.\nPress Enter to Try again.");
                    Console.ReadKey();
                    logAttempts += 1;

                } //logUser == user

            } while ((logAttempts != attempts)); //while logAttempts = 0 don't equals to attempts = 3

            return grantedAccess;
        }

        static void MainMenu()
        {
            Console.WriteLine("---PROGRAMS---");
            Console.WriteLine("1. Computer Science");
            Console.WriteLine("2. Medicine");
            Console.WriteLine("3. Marketing");
            Console.WriteLine("4. Arts");
            Console.WriteLine("5. Exit Program");
            Console.WriteLine("--------------");
            Console.WriteLine("Please, choose an option: ");
        }

        static void csProgram()
        {
            Console.Clear();
            ConsoleKeyInfo keyInfo = Console.ReadKey();
            Console.WriteLine("Computer Science Program");
            Console.WriteLine("Select a Campus");
            string selectedCampus = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    if (London[0] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slot in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue");
                        
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");                                
                            }
                            
                        } while (keyInfo.Key != ConsoleKey.Enter);
                        
                        return;
                    }
                    break;
                case "MANCHESTER":
                    if (Manchester[0] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                case "LIVERPOOL":
                    if (Liverpool[0] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE.\n Press any key to try again.");
                    Console.ReadKey();
                    csProgram();
                    break;
            } //switch

            Console.WriteLine("ENROLLMENT.");
            Console.WriteLine("Please, type your Name");
            string inputName = Console.ReadLine();
            Console.WriteLine("Please, type your Last Name");
            string inputLastName = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    London[0] -= 1;
                    break;
                case "MANCHESTER":
                    Manchester[0] -= 1;
                    break;
                case "LIVERPOOL":
                    Liverpool[0] -= 1;
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE. \n Press any key...");
                    Console.ReadKey();
                    return;
                    break;
            }

            Console.WriteLine("Enrollment completed succesfully.");
            Console.WriteLine("Do you want to make another Enrollment?\n1. YES\n2. NO" );
            int youSure = Convert.ToInt32(Console.ReadLine());
            if (youSure == 1)
            {
                MainMenu();
            }
            else if (youSure == 2)
            {
                Console.WriteLine("Thank you for using the Downtown Enrollment System");
                Console.WriteLine("Press any key to exit the program/system");
                Console.ReadKey();
            }
        } // csProgram void

        static void medProgram()
        {
            Console.Clear();
            ConsoleKeyInfo keyInfo = Console.ReadKey();
            Console.WriteLine("Medicine Program");
            Console.WriteLine("Select a Campus");
            string selectedCampus = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    if (London[1] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slot in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue");

                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }

                        } while (keyInfo.Key != ConsoleKey.Enter);

                        return;
                    }
                    break;
                case "MANCHESTER":
                    if (Manchester[1] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                case "LIVERPOOL":
                    if (Liverpool[1] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE.\n Press any key to try again.");
                    Console.ReadKey();
                    csProgram();
                    break;
            } //switch

            Console.WriteLine("ENROLLMENT.");
            Console.WriteLine("Please, type your Name");
            string inputName = Console.ReadLine();
            Console.WriteLine("Please, type your Last Name");
            string inputLastName = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    London[1] -= 1;
                    break;
                case "MANCHESTER":
                    Manchester[1] -= 1;
                    break;
                case "LIVERPOOL":
                    Liverpool[1] -= 1;
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE. \n Press any key...");
                    Console.ReadKey();
                    return;
                    break;
            }

            Console.WriteLine("Enrollment completed succesfully.");
            Console.WriteLine("Do you want to make another Enrollment?\n1. YES\n2. NO");
            int youSure = Convert.ToInt32(Console.ReadLine());
            if (youSure == 1)
            {
                MainMenu();
            }
            else if (youSure == 2)
            {
                Console.WriteLine("Thank you for using the Downtown Enrollment System");
                Console.WriteLine("Press any key to exit the program/system");
                Console.ReadKey();
            }
        } // medProgram void

        static void artProgram()
        {
            Console.Clear();
            ConsoleKeyInfo keyInfo = Console.ReadKey();
            Console.WriteLine("Art Program");
            Console.WriteLine("Select a Campus");
            string selectedCampus = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    if (London[2] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slot in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue");

                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }

                        } while (keyInfo.Key != ConsoleKey.Enter);

                        return;
                    }
                    break;
                case "MANCHESTER":
                    if (Manchester[2] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                case "LIVERPOOL":
                    if (Liverpool[2] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE.\n Press any key to try again.");
                    Console.ReadKey();
                    csProgram();
                    break;
            } //switch

            Console.WriteLine("ENROLLMENT.");
            Console.WriteLine("Please, type your Name");
            string inputName = Console.ReadLine();
            Console.WriteLine("Please, type your Last Name");
            string inputLastName = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    London[2] -= 1;
                    break;
                case "MANCHESTER":
                    Manchester[2] -= 1;
                    break;
                case "LIVERPOOL":
                    Liverpool[2] -= 1;
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE. \n Press any key...");
                    Console.ReadKey();
                    return;
                    break;
            }

            Console.WriteLine("Enrollment completed succesfully.");
            Console.WriteLine("Do you want to make another Enrollment?\n1. YES\n2. NO");
            int youSure = Convert.ToInt32(Console.ReadLine());
            if (youSure == 1)
            {
                MainMenu();
            }
            else if (youSure == 2)
            {
                Console.WriteLine("Thank you for using the Downtown Enrollment System");
                Console.WriteLine("Press any key to exit the program/system");
                Console.ReadKey();
            }
        } // artProgram void
        static void marProgram()
        {
            Console.Clear();
            ConsoleKeyInfo keyInfo = Console.ReadKey();
            Console.WriteLine("Marketing Program");
            Console.WriteLine("Select a Campus");
            string selectedCampus = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    if (London[3] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slot in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue");

                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }

                        } while (keyInfo.Key != ConsoleKey.Enter);

                        return;
                    }
                    break;
                case "MANCHESTER":
                    if (Manchester[3] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                case "LIVERPOOL":
                    if (Liverpool[3] == 0)
                    {
                        Console.WriteLine("Sorry, but there is no available slots in this campus. Try with the other ones.");
                        Console.WriteLine("Press Enter to continue..");
                        do
                        {
                            Console.ReadKey();
                            if (keyInfo.Key != ConsoleKey.Enter)
                            {
                                Console.WriteLine("You must Press ENTER to continue...");
                            }
                        } while (keyInfo.Key != ConsoleKey.Enter);
                    }
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE.\n Press any key to try again.");
                    Console.ReadKey();
                    csProgram();
                    break;
            } //switch

            Console.WriteLine("ENROLLMENT.");
            Console.WriteLine("Please, type your Name");
            string inputName = Console.ReadLine();
            Console.WriteLine("Please, type your Last Name");
            string inputLastName = Console.ReadLine();

            switch (selectedCampus.ToUpper())
            {
                case "LONDON":
                    London[3] -= 1;
                    break;
                case "MANCHESTER":
                    Manchester[3] -= 1;
                    break;
                case "LIVERPOOL":
                    Liverpool[3] -= 1;
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE. \n Press any key...");
                    Console.ReadKey();
                    return;
                    break;
            }

            Console.WriteLine("Enrollment completed succesfully.");
            Console.WriteLine("Do you want to make another Enrollment?\n1. YES\n2. NO");
            int youSure = Convert.ToInt32(Console.ReadLine());
            if (youSure == 1)
            {
                MainMenu();
            }
            else if (youSure == 2)
            {
                Console.WriteLine("Thank you for using the Downtown Enrollment System");
                Console.WriteLine("Press any key to exit the program/system");
                Console.ReadKey();
            }
        } // marProgram void
    }
}
