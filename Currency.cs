using System;
using System.Collections.Generic;
using System.Diagnostics.Eventing.Reader;
using System.Linq;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace L0E2
{
    internal class Currency
    {
        /*
*       2. Create a currency converter between CLP(Chile Peso), ARS(Argentina Peso), USD(Dolar), 
*       EUR(euro), TRY(Lira Turca), GBP(Libra Esterlina) with the following features:
*       
* 		- The user must choose their initial currency and the currency they want to exchange to.
* 		
* 		- The user can choose whether or not to withdraw their funds. If they choose not to withdraw, 
* 		it should return to the main menu.
* 		
* 		- If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		
* 		- Set a minimum and maximum amount for each currency, it can be of your choice.
* 		
* 		- The system should ask the user if they want to perform another operation. If they choose to do so,
* 		it should restart the process; otherwise, the system should close.
         
         *
         */


        static void Main(string[] args)
        {
            CConverter converter = new CConverter();

            converter.MainMenu();

            

        }

    }

    public class CConverter
    {
        public int menuOption, chooseCurrency, convertToOption, youSure, withdrawFundsOp, anotherOp;
        
        public double amountToExchange, amountResult = 0, totalWithdraw, percentageOfCom = 0.01, comissionTotal;






        public void MainMenu()
        {
            Console.WriteLine(" ---------------------------------------------- ");
            Console.WriteLine("| Welcome to DCC (Downtown Currency Converter) |");
            Console.WriteLine("|           Choose an Option                   |");
            Console.WriteLine("|         1. Exchange Currency                 |");
            Console.WriteLine("|         2. Exit the DCC                      |");
            Console.WriteLine(" ---------------------------------------------- ");
           

            do
            {
                menuOption = Convert.ToInt32(Console.ReadLine());

                if (menuOption == 1)
                {
                   Console.WriteLine("Exchange");
                    Exchange();
                    menuOption = 0; 
                }
                else if (menuOption == 2)
                {
                    Goodbye();
                    menuOption = 0;
                    Console.ReadKey();
                }
                else
                {
                    Console.WriteLine("Invalid! Please type a valid option between 1 and 2 ***");
                }

            } while ((menuOption != 1) || (menuOption !=2));

        }

        public void Exchange()
        {
            //Limpiamos Consola
            Console.Clear();
            Console.WriteLine("You've choosed Exchange your Funds");

            //Pedimos que seleccione el primer tipo de moneda
            Console.WriteLine("Now, please select the initial currency type");
            Console.WriteLine("1. CLP (Chilean Peso)\n2. ARS (Argentinian Peso)\n3. USD(US Dollar)\n4. EUR(Euro)\n" +
                             "5. TRY(Turkish Lire)\n6. GBP(Pound Sterling)\n7. Go Back");
            do
            {
                chooseCurrency = Convert.ToInt32(Console.ReadLine());

                if ((chooseCurrency <= 0) || (chooseCurrency >= 8))
                {
                    Console.WriteLine("Invalid. Please select a valid option from the menu.");
                }
                else
                {
                    switch (chooseCurrency)
                    {
                        case 1:
                            Console.WriteLine("You sure you want to choose CLP?");
                            Console.WriteLine("1. YES\n2. NO");
                            youSure = Convert.ToInt32(Console.ReadLine());
                            if (youSure == 1)
                            {
                                CLPTo();
                                youSure = 0;
                            }
                            else if (youSure == 2)
                            {
                                Console.Clear();
                                Exchange();
                                youSure = 0;
                            }
                            break;
                        case 2:
                            Console.WriteLine("You sure you want to choose ARS?");
                            Console.WriteLine("1. YES\n2. NO");
                            youSure = Convert.ToInt32(Console.ReadLine());
                            if (youSure == 1)
                            {
                                ARSTo();
                                youSure = 0;
                            }
                            else if (youSure == 2)
                            {
                                Console.Clear();
                                Exchange();
                                youSure = 0;
                            }
                            break;
                        case 3:
                            Console.WriteLine("You sure you want to choose USD?");
                            Console.WriteLine("1. YES\n2. NO");
                            youSure = Convert.ToInt32(Console.ReadLine());
                            if (youSure == 1)
                            {
                                USDTo();
                                youSure = 0;
                            }
                            else if (youSure == 2)
                            {
                                Console.Clear();
                                Exchange();
                                youSure = 0;
                            }
                            break;
                        case 4:
                            Console.WriteLine("You sure you want to choose EUR?");
                            Console.WriteLine("1. YES\n2. NO");
                            youSure = Convert.ToInt32(Console.ReadLine());
                            if (youSure == 1)
                            {
                                EURTo();
                                youSure = 0;
                            }
                            else if (youSure == 2)
                            {
                                Console.Clear();
                                Exchange();
                                youSure = 0;
                            }
                            break;
                        case 5:
                            Console.WriteLine("You sure you want to choose TRY?");
                            Console.WriteLine("1. YES\n2. NO");
                            youSure = Convert.ToInt32(Console.ReadLine());
                            if (youSure == 1)
                            {
                                TRYTo();
                                youSure = 0;
                            }
                            else if (youSure == 2)
                            {
                                Console.Clear();
                                Exchange();
                                youSure = 0;
                            }
                            break;
                        case 6:
                            Console.WriteLine("You sure you want to choose GBP?");
                            Console.WriteLine("1. YES\n2. NO");
                            youSure = Convert.ToInt32(Console.ReadLine());
                            if (youSure == 1)
                            {
                                GBPTo();
                                youSure = 0;
                            }
                            else if (youSure == 2)
                            {
                                Console.Clear();
                                Exchange();
                                youSure = 0;
                            }
                            break;
                        case 7:
                            Console.Clear();
                            MainMenu();
                            break;
                    }
                }

            } while ((chooseCurrency <=0) || (chooseCurrency>=8));

            

            void CLPTo()
            {
                /*
                * CLP to ARS - 1 CLP = 0.88 ARS
                * CLP to USD - 1 CLP = 0.0010 USD
                * CLP to EUR - 1 CLP = 0,00094 EUR
                * CLP to TRY - 1 CLP = 0,033 TRY
                * CLP to GBP - 1 CLP = 0,00081 GBP
               */

                //Limpiamos Consola
                Console.Clear();
                Console.WriteLine("You have choosed CLP (Chilean Peso)\n");

                //Pedimos la cantidad a convertir
                Console.WriteLine("Please type the amount that you want to convert.\n" +
                    "For CLP you have to enter an amount greater than 10 CLP");

                //Ejecuta este codigo mientras la cantidad a cambiar no sea igual o menor que 0 
                // ni que sea menor que 10
                do
                {
                    amountToExchange = Convert.ToDouble(Console.ReadLine());

                    if(amountToExchange <= 0)
                    {
                        Console.WriteLine("Invalid Amount. Please enter a valid amount");
                    }
                    else if (amountToExchange <10)
                    {
                        Console.WriteLine("Not Enough, you must enter an amount greater than 10 CLP");

                    }
                    else if (amountToExchange >100000)
                    {
                        Console.WriteLine("Too much, you must enter an amount less than 100000 CLP");
                    }
                    else
                    {
                        NewCurrencyType();
                    }

                } while ((amountToExchange <= 0 ) || (amountToExchange <10) || (amountToExchange >100000));

                void NewCurrencyType()
                {
                    Console.Clear();
                    Console.WriteLine("The Amount typed is: $" + amountToExchange);
                    //Pedimos el tipo de moneda en la que queremos convertir
                    Console.WriteLine("Now, please select the new currency type");
                    Console.WriteLine("1. ARS (Argentinian Peso)\n2. USD(US Dollar)\n3. EUR(Euro)\n" +
                                        "4. TRY(Turkish Lire)\n5. GBP(Pound Sterling)");
                    do
                    {
                        convertToOption = Convert.ToInt32(Console.ReadLine());

                        if ((convertToOption <=0) || (convertToOption >=6))
                        {
                            Console.WriteLine("Invalid. Please select a valid option from the menu.");
                        }
                        else
                        {
                            switch (convertToOption)
                            {
                                //CLP TO ARS
                                case 1:
                                    Console.WriteLine("You sure you want to convert it to ARS?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.88;
                                        Console.WriteLine("$"+amountToExchange+" CLP to ARS == $"+amountResult+" ARS");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");
                                        
                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <=0) || (withdrawFundsOp >=3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }                                    
                                    break;

                                //CLP TO USD
                                case 2:
                                    Console.WriteLine("You sure you want to convert it to USD?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.0010;
                                        Console.WriteLine("$" + amountToExchange + " CLP " +"== $"+amountResult+ " USD.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");
                                        
                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;
                                //CLP TO EUR
                                case 3:
                                    Console.WriteLine("You sure you want to convert it to EUR?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.00094;
                                        Console.WriteLine("$" + amountToExchange + " CLP " +
                                            "== $" + "{0:N4}", amountResult + " EUR.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");
                                        
                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //CLP TO TRY
                                case 4:
                                    Console.WriteLine("You sure you want to convert it to TRY?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.033;
                                        Console.WriteLine("$" + amountToExchange + " CLP " +
                                            "== $" + "{0:N4}", amountResult + " TRY.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");
                                        
                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //CLP TO GBP
                                case 5:
                                    Console.WriteLine("You sure you want to convert it to GBP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.00081;
                                        Console.WriteLine("$" + amountToExchange + " CLP " +
                                            "== $" + "{0:N4}", amountResult + " GBP.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");
                                        
                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }

                                    break;
                            } //end switch
                        } // end of the if (else)

                    } while ((convertToOption <= 0) || (convertToOption >= 6));
                    
                } //NewCurrencyType
             
            } // void CLPto

            void ARSTo()
            {
                /*
                * ARS to CLP - 1 ARS = 1,14 CLP
                * ARS to USD - 1 ARS = 0,0012 USD
                * ARS to EUR - 1 ARS = 0,0011 EUR
                * ARS to TRY - 1 ARS = 0,038 TRY
                * ARS to GBP - 1 ARS = 0,00092 GBP
               */

                //Limpiamos Consola
                Console.Clear();
                Console.WriteLine("You have choosed ARS (Argentinian Peso)\n");

                //Pedimos la cantidad a convertir
                Console.WriteLine("Please type the amount that you want to convert.\n" +
                    "For ARS you have to enter an amount greater than 10 ARS and less than 100000");

                //Ejecuta este codigo mientras la cantidad a cambiar no sea igual o menor que 0 
                // ni que sea menor que 10
                do
                {
                    amountToExchange = Convert.ToDouble(Console.ReadLine());

                    if (amountToExchange <= 0)
                    {
                        Console.WriteLine("Invalid Amount. Please enter a valid amount");
                    }
                    else if (amountToExchange < 10)
                    {
                        Console.WriteLine("Not Enough, you must enter an amount greater than 10 ARS");

                    }
                    else if (amountToExchange > 100000)
                    {
                        Console.WriteLine("Too much, you must enter an amount less than 100000 ARS");
                    }
                    else
                    {
                        NewCurrencyType();
                    }

                } while ((amountToExchange <= 0) || (amountToExchange < 10) || (amountToExchange > 100000));

                void NewCurrencyType()
                {
                    Console.Clear();
                    Console.WriteLine("The Amount typed is: $" + amountToExchange);
                    //Pedimos el tipo de moneda en la que queremos convertir
                    Console.WriteLine("Now, please select the new currency type");
                    Console.WriteLine("1. CLP (Chilean Peso)\n2. USD(US Dollar)\n3. EUR(Euro)\n" +
                                        "4. TRY(Turkish Lire)\n5. GBP(Pound Sterling)");
                    do
                    {
                        convertToOption = Convert.ToInt32(Console.ReadLine());

                        if ((convertToOption <= 0) || (convertToOption >= 6))
                        {
                            Console.WriteLine("Invalid. Please select a valid option from the menu.");
                        }
                        else
                        {
                            switch (convertToOption)
                            {
                                //ARS TO CLP
                                case 1:
                                    Console.WriteLine("You sure you want to convert it to CLP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 1.14;
                                        Console.WriteLine("$" + amountToExchange + " ARS to CLP == $" + amountResult + " ARS");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //ARS TO USD
                                case 2:
                                    Console.WriteLine("You sure you want to convert it to USD?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.0012;
                                        Console.WriteLine("$" + amountToExchange + " ARS " + "== $" + amountResult + " USD.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;
                                //ARS TO EUR
                                case 3:
                                    Console.WriteLine("You sure you want to convert it to EUR?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.0011;
                                        Console.WriteLine("$" + amountToExchange + " ARS " +
                                            "== $" + "{0:N4}", amountResult + " EUR.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //ARS TO TRY
                                case 4:
                                    Console.WriteLine("You sure you want to convert it to TRY?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.038;
                                        Console.WriteLine("$" + amountToExchange + " ARS " +
                                            "== $" + "{0:N4}", amountResult + " TRY.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //ARS TO GBP
                                case 5:
                                    Console.WriteLine("You sure you want to convert it to GBP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.00092;
                                        Console.WriteLine("$" + amountToExchange + " ARS " +
                                            "== $" + "{0:N4}", amountResult + " GBP.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }

                                    break;
                            } //end switch
                        } // end of the if (else)

                    } while ((convertToOption <= 0) || (convertToOption >= 6));

                } //NewCurrencyType

            } // void ARSto

            void USDTo()
            {
                /*
                * USD to CLP - 1 USD = 980,96 CLP
                * USD to ARS - 1 USD = 858,25 ARS
                * USD to EUR - 1 USD = 0,93 EUR
                * USD to TRY - 1 USD = 32,37 TRY
                * USD to GBP - 1 USD = 0,79 GBP
               */

                //Limpiamos Consola
                Console.Clear();
                Console.WriteLine("You have choosed USD (United States Dollar)\n");

                //Pedimos la cantidad a convertir
                Console.WriteLine("Please type the amount that you want to convert.\n" +
                    "For USD you have to enter an amount greater than 10 USD and less than 5000");

                //Ejecuta este codigo mientras la cantidad a cambiar no sea igual o menor que 0 
                // ni que sea menor que 10
                do
                {
                    amountToExchange = Convert.ToDouble(Console.ReadLine());

                    if (amountToExchange <= 0)
                    {
                        Console.WriteLine("Invalid Amount. Please enter a valid amount");
                    }
                    else if (amountToExchange < 10)
                    {
                        Console.WriteLine("Not Enough, you must enter an amount greater than 10 USD");

                    }
                    else if (amountToExchange > 5000)
                    {
                        Console.WriteLine("Too much, you must enter an amount less than 5000 USD");
                    }
                    else
                    {
                        NewCurrencyType();
                    }

                } while ((amountToExchange <= 0) || (amountToExchange < 10) || (amountToExchange > 5000));

                void NewCurrencyType()
                {
                    Console.Clear();
                    Console.WriteLine("The Amount typed is: $" + amountToExchange);
                    //Pedimos el tipo de moneda en la que queremos convertir
                    Console.WriteLine("Now, please select the new currency type");
                    Console.WriteLine("1. CLP (Chilean Peso)\n2. ARS(Argentinian Peso)\n3. EUR(Euro)\n" +
                                        "4. TRY(Turkish Lire)\n5. GBP(Pound Sterling)");
                    do
                    {
                        convertToOption = Convert.ToInt32(Console.ReadLine());

                        if ((convertToOption <= 0) || (convertToOption >= 6))
                        {
                            Console.WriteLine("Invalid. Please select a valid option from the menu.");
                        }
                        else
                        {
                            switch (convertToOption)
                            {
                                //USD TO CLP
                                case 1:
                                    Console.WriteLine("You sure you want to convert it to CLP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 980.96;
                                        Console.WriteLine("$" + amountToExchange + " USD to CLP == $" + amountResult + " CLP");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //USD TO ARS
                                case 2:
                                    Console.WriteLine("You sure you want to convert it to ARS?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 858.25;
                                        Console.WriteLine("$" + amountToExchange + " USD " + "== $" + amountResult + " ARS.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //USD TO EUR
                                case 3:
                                    Console.WriteLine("You sure you want to convert it to EUR?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.93;
                                        Console.WriteLine("$" + amountToExchange + " USD " +
                                            "== $" + "{0:N4}", amountResult + " EUR.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //USD TO TRY
                                case 4:
                                    Console.WriteLine("You sure you want to convert it to TRY?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 32.37;
                                        Console.WriteLine("$" + amountToExchange + " USD " +
                                            "== $" + "{0:N4}", amountResult + " TRY.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //USD TO GBP
                                case 5:
                                    Console.WriteLine("You sure you want to convert it to GBP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.79;
                                        Console.WriteLine("$" + amountToExchange + " USD " +
                                            "== $" + "{0:N4}", amountResult + " GBP.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }

                                    break;
                            } //end switch
                        } // end of the if (else)

                    } while ((convertToOption <= 0) || (convertToOption >= 6));

                } //NewCurrencyType

            } // void USDto

            void EURTo()
            {
                /*
                * EUR to CLP - 1 EUR = 1056,90 CLP
                * EUR to ARS - 1 EUR = 925,04 ARS
                * EUR to USD - 1 EUR = 1,08 USD
                * EUR to TRY - 1 EUR = 34,88 TRY
                * EUR to GBP - 1 EUR = 0,85 GBP
               */

                //Limpiamos Consola
                Console.Clear();
                Console.WriteLine("You have choosed EUR (EUR)\n");

                //Pedimos la cantidad a convertir
                Console.WriteLine("Please type the amount that you want to convert.\n" +
                    "For EUR you have to enter an amount greater than 10 and less than 5000");

                //Ejecuta este codigo mientras la cantidad a cambiar no sea igual o menor que 0 
                // ni que sea menor que 10
                do
                {
                    amountToExchange = Convert.ToDouble(Console.ReadLine());

                    if (amountToExchange <= 0)
                    {
                        Console.WriteLine("Invalid Amount. Please enter a valid amount");
                    }
                    else if (amountToExchange < 10)
                    {
                        Console.WriteLine("Not Enough, you must enter an amount greater than 10 EUR");

                    }
                    else if (amountToExchange > 5000)
                    {
                        Console.WriteLine("Too much, you must enter an amount less than 5000 EUR");
                    }
                    else
                    {
                        NewCurrencyType();
                    }

                } while ((amountToExchange <= 0) || (amountToExchange < 10) || (amountToExchange > 5000));

                void NewCurrencyType()
                {
                    Console.Clear();
                    Console.WriteLine("The Amount typed is: $" + amountToExchange);
                    //Pedimos el tipo de moneda en la que queremos convertir
                    Console.WriteLine("Now, please select the new currency type");
                    Console.WriteLine("1. CLP (Chilean Peso)\n2. ARS(Argentinian Peso)\n3. USD(United States Dollar)\n" +
                                        "4. TRY(Turkish Lire)\n5. GBP(Pound Sterling)");
                    do
                    {
                        convertToOption = Convert.ToInt32(Console.ReadLine());

                        if ((convertToOption <= 0) || (convertToOption >= 6))
                        {
                            Console.WriteLine("Invalid. Please select a valid option from the menu.");
                        }
                        else
                        {
                            switch (convertToOption)
                            {
                                //EUR TO CLP
                                case 1:
                                    Console.WriteLine("You sure you want to convert it to CLP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 1056.90;
                                        Console.WriteLine("$" + amountToExchange + " EUR to CLP == $" + amountResult + " CLP");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //EUR TO ARS
                                case 2:
                                    Console.WriteLine("You sure you want to convert it to ARS?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 925.04;
                                        Console.WriteLine("$" + amountToExchange + " EUR " + "== $" + amountResult + " ARS.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //EUR TO USD
                                case 3:
                                    Console.WriteLine("You sure you want to convert it to USD?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 1.08;
                                        Console.WriteLine("$" + amountToExchange + " EUR " +
                                            "== $" + "{0:N4}", amountResult + " USD.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //EUR TO TRY
                                case 4:
                                    Console.WriteLine("You sure you want to convert it to TRY?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 34.88;
                                        Console.WriteLine("$" + amountToExchange + " EUR " +
                                            "== $" + "{0:N4}", amountResult + " TRY.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //EUR TO GBP
                                case 5:
                                    Console.WriteLine("You sure you want to convert it to GBP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.85;
                                        Console.WriteLine("$" + amountToExchange + " EUR " +
                                            "== $" + "{0:N4}", amountResult + " GBP.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }

                                    break;
                            } //end switch
                        } // end of the if (else)

                    } while ((convertToOption <= 0) || (convertToOption >= 6));

                } //NewCurrencyType

            } // void EURTo

            void TRYTo()
            {
                /*
                * TRY to CLP - 1 TRY = 30,26 CLP
                * TRY to ARS - 1 TRY = 26,45 ARS
                * TRY to USD - 1 TRY = 0,031 USD
                * TRY to EUR - 1 TRY = 0,029 EUR
                * TRY to GBP - 1 TRY = 0,024 GBP
               */

                //Limpiamos Consola
                Console.Clear();
                Console.WriteLine("You have choosed TRY (Turkish Lira)\n");

                //Pedimos la cantidad a convertir
                Console.WriteLine("Please type the amount that you want to convert.\n" +
                    "For TRY you have to enter an amount greater than 10 and less than 10000");

                //Ejecuta este codigo mientras la cantidad a cambiar no sea igual o menor que 0 
                // ni que sea menor que 10
                do
                {
                    amountToExchange = Convert.ToDouble(Console.ReadLine());

                    if (amountToExchange <= 0)
                    {
                        Console.WriteLine("Invalid Amount. Please enter a valid amount");
                    }
                    else if (amountToExchange < 10)
                    {
                        Console.WriteLine("Not Enough, you must enter an amount greater than 10 TRY");

                    }
                    else if (amountToExchange > 10000)
                    {
                        Console.WriteLine("Too much, you must enter an amount less than 10000 TRY");
                    }
                    else
                    {
                        NewCurrencyType();
                    }

                } while ((amountToExchange <= 0) || (amountToExchange < 10) || (amountToExchange > 10000));

                void NewCurrencyType()
                {
                    Console.Clear();
                    Console.WriteLine("The Amount typed is: $" + amountToExchange);
                    //Pedimos el tipo de moneda en la que queremos convertir
                    Console.WriteLine("Now, please select the new currency type");
                    Console.WriteLine("1. CLP (Chilean Peso)\n2. ARS(Argentinian Peso)\n3. USD(United States Dollar)\n" +
                                        "4. EUR(Euro)\n5. GBP(Pound Sterling)");
                    do
                    {
                        convertToOption = Convert.ToInt32(Console.ReadLine());

                        if ((convertToOption <= 0) || (convertToOption >= 6))
                        {
                            Console.WriteLine("Invalid. Please select a valid option from the menu.");
                        }
                        else
                        {
                            switch (convertToOption)
                            {
                                //TRY TO CLP
                                case 1:
                                    Console.WriteLine("You sure you want to convert it to CLP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 30.26;
                                        Console.WriteLine("$" + amountToExchange + " TRY to CLP == $" + amountResult + " CLP");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //TRY TO ARS
                                case 2:
                                    Console.WriteLine("You sure you want to convert it to ARS?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 26.45;
                                        Console.WriteLine("$" + amountToExchange + " TRY " + "== $" + amountResult + " ARS.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //TRY TO USD
                                case 3:
                                    Console.WriteLine("You sure you want to convert it to USD?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.031;
                                        Console.WriteLine("$" + amountToExchange + " TRY " +
                                            "== $" + "{0:N4}", amountResult + " USD.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //TRY TO EUR
                                case 4:
                                    Console.WriteLine("You sure you want to convert it to EUR?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.029;
                                        Console.WriteLine("$" + amountToExchange + " TRY " +
                                            "== $" + "{0:N4}", amountResult + " EUR.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //TRY TO GBP
                                case 5:
                                    Console.WriteLine("You sure you want to convert it to GBP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 0.024;
                                        Console.WriteLine("$" + amountToExchange + " TRY " +
                                            "== $" + "{0:N4}", amountResult + " GBP.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }

                                    break;
                            } //end switch
                        } // end of the if (else)

                    } while ((convertToOption <= 0) || (convertToOption >= 6));

                } //NewCurrencyType

            } // void TRYTo

            void GBPTo()
            {
                /*
                * GBP to CLP - 1 GBP = 1237,04 CLP
                * GBP to ARS - 1 GBP = 1081,30 ARS
                * GBP to USD - 1 GBP = 1,26 USD
                * GBP to EUR - 1 GBP = 1,17 EUR
                * GBP to TRY - 1 GBP = 40,88 TRY
               */

                //Limpiamos Consola
                Console.Clear();
                Console.WriteLine("You have choosed GBP (Pound Sterling)\n");

                //Pedimos la cantidad a convertir
                Console.WriteLine("Please type the amount that you want to convert.\n" +
                    "For GBP you have to enter an amount greater than 10 and less than 5000");

                //Ejecuta este codigo mientras la cantidad a cambiar no sea igual o menor que 0 
                // ni que sea menor que 10
                do
                {
                    amountToExchange = Convert.ToDouble(Console.ReadLine());

                    if (amountToExchange <= 0)
                    {
                        Console.WriteLine("Invalid Amount. Please enter a valid amount");
                    }
                    else if (amountToExchange < 10)
                    {
                        Console.WriteLine("Not Enough, you must enter an amount greater than 10 GBP");

                    }
                    else if (amountToExchange > 5000)
                    {
                        Console.WriteLine("Too much, you must enter an amount less than 5000 GBP");
                    }
                    else
                    {
                        NewCurrencyType();
                    }

                } while ((amountToExchange <= 0) || (amountToExchange < 10) || (amountToExchange > 5000));

                void NewCurrencyType()
                {
                    Console.Clear();
                    Console.WriteLine("The Amount typed is: $" + amountToExchange);
                    //Pedimos el tipo de moneda en la que queremos convertir
                    Console.WriteLine("Now, please select the new currency type");
                    Console.WriteLine("1. CLP (Chilean Peso)\n2. ARS(Argentinian Peso)\n3. USD(United States Dollar)\n" +
                                        "4. EUR(Euro)\n5. TRY(Turkis Lira)");
                    do
                    {
                        convertToOption = Convert.ToInt32(Console.ReadLine());

                        if ((convertToOption <= 0) || (convertToOption >= 6))
                        {
                            Console.WriteLine("Invalid. Please select a valid option from the menu.");
                        }
                        else
                        {
                            switch (convertToOption)
                            {
                                //GBP TO CLP
                                case 1:
                                    Console.WriteLine("You sure you want to convert it to CLP?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 1237.04;
                                        Console.WriteLine("$" + amountToExchange + " GBP to CLP == $" + amountResult + " CLP");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //GBP TO ARS
                                case 2:
                                    Console.WriteLine("You sure you want to convert it to ARS?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 1081.30;
                                        Console.WriteLine("$" + amountToExchange + " GBP " + "== $" + amountResult + " ARS.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //GBP TO USD
                                case 3:
                                    Console.WriteLine("You sure you want to convert it to USD?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 1.26;
                                        Console.WriteLine("$" + amountToExchange + " GBP " +
                                            "== $" + "{0:N4}", amountResult + " USD.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //GBP TO EUR
                                case 4:
                                    Console.WriteLine("You sure you want to convert it to EUR?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 1.17;
                                        Console.WriteLine("$" + amountToExchange + " GBP " +
                                            "== $" + "{0:N4}", amountResult + " EUR.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }
                                    break;

                                //GBP TO TRY
                                case 5:
                                    Console.WriteLine("You sure you want to convert it to TRY?");
                                    Console.WriteLine("1. YES\n2. NO");
                                    youSure = Convert.ToInt32(Console.ReadLine());
                                    if (youSure == 1)
                                    {
                                        amountResult = amountToExchange * 40.88;
                                        Console.WriteLine("$" + amountToExchange + " GBP " +
                                            "== $" + "{0:N4}", amountResult + " TRY.");
                                        youSure = 0;

                                        Console.WriteLine("Do you want to withdraw your funds?");
                                        Console.WriteLine("1. YES\n2. NO");

                                        do
                                        {
                                            withdrawFundsOp = Convert.ToInt32(Console.ReadLine());

                                            if ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3))
                                            {
                                                Console.WriteLine("Invalid. Please type a valid option from the menu");
                                            }
                                            else if (withdrawFundsOp == 1)
                                            {
                                                Withdraw();
                                            }
                                            else if (withdrawFundsOp == 2)
                                            {
                                                Goodbye();
                                            }
                                        } while ((withdrawFundsOp <= 0) || (withdrawFundsOp >= 3));

                                    }
                                    else if (youSure == 2)
                                    {
                                        Console.Clear();
                                        youSure = 0;
                                        NewCurrencyType();
                                    }

                                    break;
                            } //end switch
                        } // end of the if (else)

                    } while ((convertToOption <= 0) || (convertToOption >= 6));

                } //NewCurrencyType

            } // void GBPTo

        } //public void Exchange

        public void Withdraw()
        {

            Console.WriteLine("\nThe system will charge a 1% commission.");
            Console.WriteLine("Your actual funds are: $" + amountResult + ".");
            comissionTotal = amountResult * percentageOfCom;
            totalWithdraw = amountResult - comissionTotal;
            Console.WriteLine("Your withdrawn funds are: $" + totalWithdraw);

            Console.WriteLine("Do you want to perform another operation?");
            Console.WriteLine("1. YES\n2. NO");
            

            do
            {

                anotherOp = Convert.ToInt32(Console.ReadLine());


                if ((anotherOp <= 0) || (anotherOp >= 3))
                {
                    Console.WriteLine("Invalid. Please type a valid option from the menu");
                }
                else if (anotherOp == 1)
                {
                    amountToExchange = 0;
                    amountResult = 0;
                    totalWithdraw = 0;
                    comissionTotal = 0;
                    Exchange();
                }
                else if (anotherOp == 2)
                {
                    Goodbye();
                }


            } while ((anotherOp <= 0) || (anotherOp >= 3));
        }
        public void Goodbye()
        {
            Console.Clear();
            Console.WriteLine("Thanks for using the Downtown Currency Converter\nSee you soon!");
            Console.ReadKey();
            Environment.Exit(0);
        }
    }



}
