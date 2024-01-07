//1.Create an online banking system with the following features:

//*Users must be able to log in with a username and password.
//* If the user enters the wrong credentials three times, the system must lock them out.
//* The initial balance in the bank account is $2000.
//* The system must allow users to deposit, withdraw, view, and transfer money.
//* The system must display a menu for users to perform transactions.

class Program
{
    static void Main()
    {
        string username = "jordiAvalos";
        string password = "Reto1@";
        decimal initialBalance = 2000.0m;
        int remainingAttempts = 3;
        bool loggedIn = false;
        while (true)
        {
            Console.WriteLine("Bienvenido al Sistema Bancario");
            if (!loggedIn)
            {
                LogIn(ref remainingAttempts, username, password, ref loggedIn);
                if (!loggedIn) continue;
            }
            Menu();
            Console.Write("Ingrese la opción deseada: ");
            string option = Console.ReadLine();
            switch (option)
            {
                case "1":
                    ShowBalance(initialBalance);
                    break;
                case "2":
                    Deposit(ref initialBalance);
                    break;
                case "3":
                    Withdraw(ref initialBalance);
                    break;
                case "4":
                    Transfer(ref initialBalance);
                    break;
                case "5":
                    LogOut(ref loggedIn);
                    break;
                default:
                    Console.WriteLine("Opción no válida. Inténtelo de nuevo.");
                    break;
            }
        }
    }

    static void LogIn(ref int remainingAttempts, string username, string password, ref bool loggedIn)
    {
        Console.Write("Ingrese nombre de usuario: ");
        string inputUsername = Console.ReadLine();
        Console.Write("Ingrese contraseña: ");
        string inputPassword = Console.ReadLine();

        if (inputUsername == username && inputPassword == password)
        {
            Console.WriteLine("Inicio de sesión exitoso. ¡Bienvenido!");
            remainingAttempts = 3;
            loggedIn = true;
        }
        else
        {
            remainingAttempts--;
            Console.WriteLine($"Inicio de sesión fallido. Intentos restantes: {remainingAttempts}");

            if (remainingAttempts == 0)
            {
                Console.WriteLine("Demasiados intentos fallidos. El sistema está bloqueado.");
                Environment.Exit(0);
            }
        }
    }

    static void Menu()
    {
        Console.WriteLine("=== Menú ===");
        Console.WriteLine("1. Ver saldo");
        Console.WriteLine("2. Depositar dinero");
        Console.WriteLine("3. Retirar dinero");
        Console.WriteLine("4. Transferir dinero");
        Console.WriteLine("5. Cerrar sesión");
    }

    static void ShowBalance(decimal balance)
    {
        Console.WriteLine($"Saldo actual: ${balance}");
    }


    static void Deposit(ref decimal balance)
    {
        Console.Write("Ingrese la cantidad a depositar: $");
        decimal deposit = Convert.ToDecimal(Console.ReadLine());

        balance += deposit;
        Console.WriteLine($"Depósito exitoso. Nuevo saldo: ${balance}");
    }

    static void Withdraw(ref decimal balance)
    {
        Console.Write("Ingrese la cantidad a retirar: $");
        decimal cashWithdrawal = Convert.ToDecimal(Console.ReadLine());

        if (cashWithdrawal > balance)
        {
            Console.WriteLine("Fondos insuficientes. Operación cancelada.");
        }
        else
        {
            balance -= cashWithdrawal;
            Console.WriteLine($"Retiro exitoso. Nuevo saldo: ${balance}");
        }
    }

    static void Transfer(ref decimal balance)
    {
        Console.Write("Ingrese la cantidad a transferir: $");
        decimal transfer = Convert.ToDecimal(Console.ReadLine());

        if (transfer > balance)
        {
            Console.WriteLine("Fondos insuficientes. Operación cancelada.");
        }
        else
        {
            Console.Write("Ingrese el destinatario: ");
            string recipient = Console.ReadLine();

            balance -= transfer;
            Console.WriteLine($"Transferencia exitosa a {recipient}. Nuevo saldo: ${balance}");
        }
    }

    static void LogOut(ref bool loggedIn)
    {
        Console.WriteLine("Cerrando sesión. ¡Hasta luego!");
        Console.WriteLine();
        Console.Clear();
        loggedIn = false;
    }
}