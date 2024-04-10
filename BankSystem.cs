using System;
using System.Diagnostics;

namespace L0E01
{
    internal class BankSystem
    {
        static void Main(string[] args)
        {
            //new object of the class register
            Banco banco = new Banco();
            Console.WriteLine("******** DOWNTOWN BANK SYSTEM ********");
            Console.WriteLine("Welcome to Downtown Bank Systems. \n What do you want to do?");
            Console.WriteLine("1. SIGN IN \n" + "2. EXIT THE DBS\n(Downtown Bank System).");
            Console.WriteLine("**************************************");
            int option = Convert.ToInt32(Console.ReadLine());

            switch (option)
            {
                case 1:
                    Console.Clear();
                    banco.CreateAcc();
                    break;
                case 2:
                    Console.WriteLine("Thanks for using Downtown Bank Systems. Have a nice day!");
                    Console.WriteLine("Press Enter to exit the Application...");
                    Console.ReadKey();
                    Environment.Exit(0);
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE");
                    break;
            }

        }

    }


    //Class Register with Create Acc. and Login
    public class Banco
    {
        //Declaración de Variables
        public string accName, accLastName, accUsername, accPassword, logUsername, logPassword;
        public int attemptsPass = 0, authPass = 0, authUsername = 0, attemptsUsername = 5;

        //Method Create Account
        public void CreateAcc()
        {
            Console.WriteLine("****** REGISTRATION ******");
            Console.WriteLine("Please, type your name: ");
            accName = Console.ReadLine();
            Console.WriteLine("Now, type your last name");
            accLastName = Console.ReadLine();

            Console.WriteLine("\n****** Username and Password Creation ******");
            Console.WriteLine("Welcome to our Bank System " + accName + " " + accLastName + ".\nTYPE YOUR USERNAME:");
            accUsername = Console.ReadLine();
            Console.WriteLine("\nTYPE YOUR PASSWORD: \nYou must use a minimum of 4 characters and a maximum of 10 characters." +
                " \nKeep in mind that you must NOT share your password with anyone");
            accPassword = Console.ReadLine();
            int passLength = accPassword.Length;

            if (passLength < 4)
            {
                System.Console.WriteLine("\nYour password must be a minimum of 4 characters. \nRestart the program to continue.");
                Console.WriteLine("Press Enter to close the program");
                Console.ReadKey();
                Environment.Exit(0);
            }
            else if (passLength > 10)
            {
                System.Console.WriteLine("\nYour password must be a maximum of 10 characters. \nRestart the program to continue.");
                System.Console.WriteLine("Press Enter to close the program");
                Console.ReadKey();
                Environment.Exit(0);
            }
            else
            {
                Console.Clear();
                Console.WriteLine("\nYou have created your account succesfully. Welcome to Downtown Bank Systems.");
                Console.WriteLine("1.LOGIN \n2.EXIT THE APP");
                int postRegOption = Convert.ToInt32(Console.ReadLine());
                switch (postRegOption)
                {
                    case 1:
                        Console.Clear();
                        Login();
                        break;
                    case 2:
                        Console.Clear();
                        Console.WriteLine("***************************************************");
                        Console.WriteLine("\nThank you for using Downtown Bank System. See ya!");
                        Console.WriteLine("***************************************************");
                        Console.ReadKey();
                        Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine("DEFAULT CASE POST REGISTER");
                        Console.ReadKey();
                        Environment.Exit(0);
                        break;
                }
            }
        }

        //Metodo LOGIN
        public void Login()
        {
            do
            {
                Console.WriteLine("****** LOG-IN ******");
                Console.WriteLine("Welcome to Downtown Bank System.");
                Console.WriteLine("TYPE YOUR USERNAME:");
                logUsername = Console.ReadLine();

                if (logUsername == accUsername)
                {
                    authUsername = 1;
                    attemptsUsername = 5;
                }
                else
                {
                    Console.WriteLine("\nThe username entered is incorrect or does not exist. Try again.");
                    Console.WriteLine("You have " + attemptsUsername + " attempts left.");
                    authUsername = 0;
                    attemptsUsername--;
                }

            } while ((logUsername != accUsername) && (attemptsUsername != 0));

            if (authUsername == 0)
            {
                Console.WriteLine("\nToo many tries! The Downtown Bank System has been blocked.\nPlease restart the program.");
                Console.WriteLine("****** PRESS ENTER TO EXIT THE APPLICATION ******");
                Console.ReadKey();
                Environment.Exit(0);
            }
            else if (authUsername == 1)
            {
                do
                {
                    Console.WriteLine("\nTYPE YOUR PASSWORD:");
                    logPassword = Console.ReadLine();

                    if (logPassword == accPassword)
                    {
                        authPass = 1;
                        attemptsPass = 0;
                    }
                    else
                    {
                        Console.WriteLine("The password entered is incorrect. Try again.");
                        authPass = 0;
                        attemptsPass++;
                    }

                } while ((logPassword != accPassword) && (attemptsPass != 3));

                if (authPass == 0)
                {
                    Console.WriteLine("\nToo many tries! YOUR ACCOUNT HAS BEEN BLOCKED for the safety of the funds.");
                    Console.WriteLine("****** PRESS ENTER TO EXIT THE APPLICATION ******");
                    Console.ReadKey();
                    Environment.Exit(0);
                }
                else if (authPass == 1)
                {
                    Console.Clear();
                    Console.WriteLine("\nWelcome to Downtown Bank Systems " + accName + " " + accLastName + "!");
                    Console.WriteLine("This is the Main Menu. Here you can choose what do you want to do with your account.");
                    Menu();

                }
            }

        }


        public double totalAmount = 2000;
        public double depositFunds = 0;
        public double transferFunds = 0;
        public double withdrawFunds = 0;
        public int optionSelected = 0;
        public int goBack = 0;
        public int confirmOrCancel;

        public void Menu()
        {
            Console.WriteLine("\n****** MENU ******");
            Console.WriteLine("1.VIEW FUNDS \n2.DEPOSIT FUNDS \n3.WITHDRAW FUNDS \n4.TRANSFER FUNDS\n5.EXIT APP");
            optionSelected = Convert.ToInt32(Console.ReadLine());

            switch (optionSelected)
            {
                case 1:
                    View();
                    optionSelected = 0;
                    break;

                case 2:
                    Deposit();
                    optionSelected = 0;
                    break;

                case 3:
                    if ((totalAmount <= 0))
                    {
                        Console.WriteLine("\nThere are no funds in your account. \n" +
                    "Please deposit money to your account first in order to withdraw it.");
                        Console.WriteLine("PRESS ENTER TO DEPOSIT FUNDS");
                        Console.ReadKey();
                        Deposit();
                    }
                    else
                    {
                        Withdraw();
                        optionSelected = 0;
                    }
                    break;

                case 4:
                    Transfer();
                    optionSelected = 0;
                    break;

                case 5:

                    ExitApp();

                    break;

                default:
                    break;
            }
        }

        public void View()
        {
            Console.Clear();
            Console.WriteLine("****** VIEW ******");
            Console.WriteLine("" + accName + " " + accLastName + " , your Total Amount right now is: \n$" + totalAmount + " USD.");
            Console.WriteLine("1. GO BACK \n2. EXIT APP");
            goBack = Convert.ToInt32(Console.ReadLine());

            if (goBack == 1)
            {
                Console.Clear();
                Menu();
                goBack = 0;
            }
            else if (goBack == 2)
            {
                Console.WriteLine("**************************************");
                Console.WriteLine("Thanks for using Downtown Bank System.");
                Console.WriteLine("***************************************");
                Console.WriteLine("\n***** PRESS ENTER TO EXIT THE APPLICATION *****");
                Console.ReadKey();
                goBack = 0;
            }
        }

        public void Deposit()
        {
            Console.Clear();
            Console.WriteLine("\n****** DEPOSIT ******");
            do
            {
                Console.WriteLine("Please, type the amount what you want to deposite.");
                Console.WriteLine("---IF YOU DON'T TYPE A NUMBER, THE PROGRAM WILL SHUTDOWN ITSELF---");
                Console.WriteLine("KEEP IN MIND: Dont use dots, comas or anything. Just type the numbers.");
                depositFunds = Convert.ToDouble(Console.ReadLine());
                if (depositFunds > 0)
                {
                    Console.WriteLine("\nYou are going to deposite: $" + depositFunds + ".");
                    Console.WriteLine("1.CONTINUE \n2.CANCEL");
                    confirmOrCancel = Convert.ToInt32(Console.ReadLine());
                    if (confirmOrCancel == 1)
                    {
                        totalAmount = depositFunds + totalAmount;
                        Console.WriteLine("\nDEPOSITE COMPLETE.");
                        Console.WriteLine("Do you want to make another deposite?");
                        Console.WriteLine("1.YES \n2.NO");
                        optionSelected = Convert.ToInt32(Console.ReadLine());
                        if (optionSelected == 1)
                        {
                            Console.Clear();
                            Deposit();
                            optionSelected = 0;
                        }
                        else if (optionSelected == 2)
                        {
                            Console.WriteLine("\nYou decided not to make another Deposite");
                            Console.WriteLine("PRESS ENTER TO GO BACK TO MENU");
                            Console.ReadKey();
                            Console.Clear();
                            Menu();
                            optionSelected = 0;
                        }
                    }
                    else if (confirmOrCancel == 2)
                    {
                        Console.WriteLine("\nDEPOSITE CANCELED. GOING BACK.");
                        Deposit();
                    }
                }
                else if (depositFunds < 0)
                {
                    Console.WriteLine("The amount typed is invalid, please, type a valid amount \n");
                    depositFunds = 0;
                }
                else if (depositFunds == 0)
                {
                    Console.WriteLine("The amount typed is invalid, please, type a valid amount \n");
                    depositFunds = 0;
                }

            } while ((depositFunds == 0));
            optionSelected = 0;

        }

        public void Withdraw()
        {
            Console.Clear();
            Console.WriteLine("****** WITHDRAW ******");
            do
            {
                Console.WriteLine("Please, type the amount what you want to Witdraw.");
                Console.WriteLine("---IF YOU DON'T TYPE A NUMBER, THE PROGRAM WILL SHUTDOWN ITSELF---");
                Console.WriteLine("KEEP IN MIND: Dont use dots, comas or anything. Just type the numbers.");
                withdrawFunds = Convert.ToDouble(Console.ReadLine());

                if ((withdrawFunds > 0) && (withdrawFunds <= totalAmount) && (totalAmount >= 1))
                {
                    Console.WriteLine("\nYou are going to Withdraw: $" + withdrawFunds + ". And your current amount is: $" + totalAmount);
                    Console.WriteLine("1.CONTINUE \n2.CANCEL");
                    confirmOrCancel = Convert.ToInt32(Console.ReadLine());

                    switch (confirmOrCancel)
                    {
                        //CONFIRMAR RETIRO
                        case 1:

                            confirmOrCancel = 0;
                            totalAmount = totalAmount - withdrawFunds;
                            Console.WriteLine("\nWITHDRAW COMPLETE.");
                            Console.WriteLine("Do you want to make another withdraw?");
                            Console.WriteLine("1.YES \n2.NO");
                            optionSelected = Convert.ToInt32(Console.ReadLine());
                            //CONFIRMAR OTRO RETIRO
                            if ((optionSelected == 1) && (totalAmount > 0))
                            {
                                Console.Clear();
                                Withdraw();
                                optionSelected = 0;
                            }
                            //CANCELAR OTRO RETIRO Y VOLVER AL MENU
                            else if (optionSelected == 2)
                            {
                                Console.WriteLine("\nYou decided not to make another Withdraw");
                                Console.WriteLine("PRESS ENTER TO GO BACK TO MENU");
                                Console.ReadKey();
                                Console.Clear();
                                Menu();
                                optionSelected = 0;
                            }
                            else if ((optionSelected == 1) && (totalAmount <= 0))
                            {
                                Console.WriteLine("There are no funds in your account. \n" +
                    "Please deposit money to your account first in order to withdraw it.");
                                Console.WriteLine("PRESS ENTER TO DEPOSITE FUNDS");
                                Console.ReadLine();
                                Deposit();
                            }
                            break;

                        //CANCELAR RETIRO
                        case 2:

                            confirmOrCancel = 0;
                            Console.WriteLine("\nWITHDRAW CANCELED. GOING BACK.");
                            Console.ReadKey();
                            Withdraw();
                            break;

                        default:
                            Console.WriteLine("DEFAULT-------------------------------");
                            break;
                    }

                }
                else if ((withdrawFunds <= 0))
                {
                    Console.WriteLine("The amount typed is invalid, please, type a valid amount.\n");
                    withdrawFunds = 0;
                }
                else if ((withdrawFunds > totalAmount))
                {
                    Console.WriteLine("The amount deposited is greater than the amount of total funds in your account: $" + totalAmount);
                    Console.WriteLine("Please, type an amount less than your total amount. \n");
                    
                    withdrawFunds = 0;
                }
                else if ((totalAmount < 0))
                {
                    Console.WriteLine("There are no funds in your account. \n" +
                        "Please deposit money to your account first in order to withdraw it.");
                    Console.WriteLine("PRESS ENTER TO DEPOSITE FUNDS");
                    Deposit();
                    withdrawFunds = 0;
                }

            } while ((withdrawFunds == 0));
            optionSelected = 0;
        }




        public string accOne = "unkn0wn", accTwo = "raru1z";
        public int accOneID = 220055854, accTwoID = 658299872;
        public int accToTransfer = 0;

        public void Transfer()
        {
            //cuentas[0] = new Banco { user = "unkn0wn", accId = 220055854 };
            //cuentas[1] = new Banco { user = "blindma1den", accId = 586321641 };
            // cuentas[2] = new Banco { user = "raru1z", accId = 658299872 };

            Console.Clear();
            Console.WriteLine("****** TRANSFER ******");
            Console.WriteLine("\nAccounts available for transfer.");
            Console.WriteLine("User: " + accOne + ". Account ID: " + accOneID);
            Console.WriteLine("User: " + accTwo + ". Account ID: " + accTwoID);

            Console.WriteLine("Do you want to do a Transfer?");
            Console.WriteLine("1. YES\n2.NO");
            optionSelected = Convert.ToInt32(Console.ReadLine());

            switch (optionSelected)
            {
                case 1:

                    do
                    {
                        optionSelected = 0;
                        Console.WriteLine("Please, type the Account ID you want to make the transfer to.");
                        accToTransfer = Convert.ToInt32(Console.ReadLine());

                        //Si alguna de las dos cuentas coincide y el monto total es mas de 0 entonces, proseguir.
                        if ((accToTransfer == accOneID) && (totalAmount > 0) || (accToTransfer == accTwoID) && (totalAmount > 0))
                        {
                            do
                            {
                                Console.WriteLine("Type the amount to transfer");
                                transferFunds = Convert.ToInt32(Console.ReadLine());

                                //Si el monto de transferencia es mayor a 0, es menor o igual a el monto total y el monto total es igual o mayor a 1
                                //entonces proseguir
                                if ((transferFunds > 0) && (transferFunds <= totalAmount) && (totalAmount >= 1))
                                {
                                    Console.WriteLine("\nYou are going to Transfer: $" + transferFunds + ". And your current amount is: $" + totalAmount);
                                    Console.WriteLine("1.CONTINUE \n2.CANCEL");
                                    confirmOrCancel = Convert.ToInt32(Console.ReadLine());

                                    switch (confirmOrCancel)
                                    {
                                        case 1:
                                            confirmOrCancel = 0;
                                            optionSelected = 0;
                                            totalAmount = totalAmount - transferFunds;
                                            Console.WriteLine("\nTRANSFER COMPLETE.");
                                            Console.WriteLine("Do you want to make another Transfer?");
                                            Console.WriteLine("1.YES \n2.NO");
                                            optionSelected = Convert.ToInt32(Console.ReadLine());
                                            //SI DESEA HACER OTRA TRANSFERENCIA Y EL MONTO TOTAL ES MAYOR A 0
                                            if ((optionSelected == 1) && (totalAmount > 0))
                                            {
                                                Console.Clear();
                                                Transfer();
                                                optionSelected = 0;
                                            }
                                            //CANCELAR OTRA TRANSFERENCIA Y VOLVER AL MENU
                                            else if (optionSelected == 2)
                                            {
                                                Console.WriteLine("\nYou decided not to make another Transfer");
                                                Console.WriteLine("PRESS ENTER TO GO BACK TO MENU");
                                                Console.ReadKey();
                                                Console.Clear();
                                                Menu();
                                                optionSelected = 0;
                                            }
                                            else if ((optionSelected == 1) && (totalAmount <= 0))
                                            {
                                                optionSelected = 0;
                                                Console.WriteLine("There are no funds in your account. \n" +
                                    "Please deposit money to your account first in order to transfer it.");
                                                Console.WriteLine("PRESS ENTER TO DEPOSITE FUNDS");
                                                Console.ReadLine();
                                                Deposit();
                                            }
                                            break;

                                        case 2:
                                            confirmOrCancel = 0;
                                            Console.WriteLine("\nTRANSFER CANCELED. GOING BACK.");
                                            Console.ReadKey();
                                            Menu();
                                            break;

                                        default:
                                            confirmOrCancel = 0;
                                            Console.WriteLine("CASE DEFAULT INSIDE IF'S");
                                            break;
                                    }

                                }
                                else if ((transferFunds <= 0))
                                {
                                    Console.WriteLine("The amount typed is invalid, please, type a valid amount.\n");
                                    transferFunds = 0;
                                }
                                else if ((transferFunds > totalAmount))
                                {
                                    Console.WriteLine("The amount typed is greater than the amount of total funds in your account: $" + totalAmount);
                                    Console.WriteLine("Please, type an amount less than your total amount. \n");
                                    transferFunds = 0;
                                }
                                else if ((totalAmount < 0))
                                {
                                    Console.WriteLine("There are no funds in your account. \n" +
                                        "Please deposit money to your account first in order to withdraw it.");
                                    Console.WriteLine("PRESS ENTER TO DEPOSITE FUNDS");
                                    Deposit();
                                    transferFunds = 0;
                                }
                            } while (transferFunds == 0);
                            

                        }
                        //Si ninguna de las cuentas coincide, imprimir que NINGUNA COINCIDE.
                        else if ((accToTransfer != accOneID) || (accToTransfer != accTwoID))
                        {
                            Console.WriteLine("The account typed does not exist. Type an existing one.");
                            transferFunds = 0;
                        }
                        //Si alguna de las cuentas coincide pero el monto total es menor que 0, enviar a DEPOSITAR.
                        else if ((accToTransfer == accOneID) && (totalAmount <= 0) || (accToTransfer == accTwoID) && (totalAmount <= 0))
                        {
                            Console.WriteLine("There are no funds in your account. \n" + 
                                "Please deposit money to your account first in order to withdraw it.");
                            Console.WriteLine("PRESS ENTER TO DEPOSITE FUNDS");
                            Deposit();
                            transferFunds = 0;
                        }

                    } while ((accToTransfer != accOneID) || (accToTransfer != accTwoID));

                    break;

                case 2:
                    optionSelected = 0;
                    Console.WriteLine("Transfer Canceled, going back to Menu");
                    Console.WriteLine("PRESS ENTER TO GO BACK TO MENU");
                    Console.ReadKey();
                    Menu();

                    break;

                default:
                    Console.WriteLine("DEFAULT CASE TRANSFER SWITCH");
                    break;
            }


        }

        public void ExitApp()
        {
            Console.Clear();
            Console.WriteLine("**************************************");
            Console.WriteLine("Thanks for using Downtown Bank System.");
            Console.WriteLine("***************************************");
            Console.WriteLine("\n***** PRESS ENTER TO EXIT THE APPLICATION *****");
            Console.ReadKey();
        }

    }

}
