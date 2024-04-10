using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace L0E4
{
    /*
     4. Create an online shipping system with the following features:
* 		
* 		The system has a login that locks after the third failed attempt. --- DONE
* 		Display a menu that allows: Sending a package, exiting the system. --- DONE
* 		To send a package, sender and recipient details are required. --- DONE
* 		The user must input the total weight of their package, and the system should display the amount to pay. --- DONE
* 		The system assigns a random package number to each sent package. --- DONE
* 		The system calculates the shipping price. $2 per kg. --- DONE
*

* 		The system should ask if the user wants to perform another operation. If the answer is yes, 
* 		it should return to the main menu. If it's no, it should close the system. --- DONE 
     
     
     
     */

    internal class ShippingSys
    {
        const string username = "sysadmin";
        const string password = "adm1n";
        const int attempts = 3;
        const decimal shippPrice = 2.00M;


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

            while (optionSelected != 2)
            {
                Console.Clear();
                MainMenu();
                optionSelected = Convert.ToInt32(Console.ReadLine());

                switch (optionSelected)
                {
                    case 1:
                        SendPackage();
                        break;
                    case 2:
                        Console.WriteLine("\nThanks for using Downtown Shipping System.\nPress any key to exit the system...");
                        Console.ReadKey();
                        break;
                    default:
                        Console.WriteLine("Defautl Case.");
                        optionSelected = Convert.ToInt32(Console.ReadLine());
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

                if (logUser == username) // if typedUser equals to username then validate pass
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
                        logAttempts += 1;

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
            Console.WriteLine("---Shipping System---");
            Console.WriteLine("1. Send a Package");
            Console.WriteLine("2. Exit the System");
            Console.WriteLine("--------------");
            Console.WriteLine("Please, choose an option: ");
        }

        static void SendPackage()
        {
            Random random = new Random();

            Console.WriteLine("Please, type the name of the person who sends the package");
            string packageSenderName = Console.ReadLine();
            Console.WriteLine("Please, type the address of the person who sends the package");
            string addressSender = Console.ReadLine();
            Console.WriteLine("Please, type the name of the person who RECEIVES the package");
            string packageReceiverName = Console.ReadLine();
            Console.WriteLine("Please, type the address of the Person who RECEIVES the package");
            string addressReceiver = Console.ReadLine();
            Console.WriteLine("Please, type the Package Weight");
            decimal packageWeight = decimal.Parse(Console.ReadLine());
            decimal total = packageWeight * shippPrice;
            Console.WriteLine("\n------------------------------");
            Console.WriteLine("        SHIPMENT DETAILS        ");
            Console.WriteLine($"Sender: {packageSenderName}" +
                $"\nSender Address: {addressSender}" +
                $"\n---------" +
                $"\nReceiver: {packageReceiverName}" +
                $"\nReceiver Address: {addressReceiver}" +
                $"\nPackage Weight: {packageWeight}" +
                $"\nTotal Price: {total}");
            Console.WriteLine("Package ID: " + random.Next(1000000, 2000000));
            Console.WriteLine("------------------------------");

            Console.WriteLine("Are you sure to perform this operation?\n1.YES\n2.NO");
            int youSure = Convert.ToInt32(Console.ReadLine());

            if (youSure == 2)
            {
                return;
            }

            Console.WriteLine("*********************");
            Console.WriteLine("Success!");
            Console.WriteLine($"Total price: {total}");
            Console.WriteLine("*********************");

            Console.WriteLine("\nDo you want to perform another shipment?\nY/N");
            string anotherShipment = Console.ReadLine();

            if (anotherShipment.ToUpper() == "Y")
            {
                return;
            }
            else if (anotherShipment.ToUpper() == "N")
            {
                Console.WriteLine("Thank you for using Downtown Shipping System.\n Press any key to exit the system...");
                Console.ReadKey();
                Environment.Exit(0);
            }






        }
    }
}
