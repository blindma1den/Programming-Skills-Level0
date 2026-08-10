//2- Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
//*The user must choose their initial currency and the currency they want to exchange to.
//*The user can choose whether or not to withdraw their funds. If they choose not to withdraw,
//it should return to the main menu.
//*If the user decides to withdraw the funds, the system will charge a 1% commission.
//*Set a minimum and maximum amount for each currency, it can be of your choice.
//*The system should ask the user if they want to perform another operation. If they choose to do so,
//it should restart the process; otherwise, the system should close.
using System;
class Program
{
    static void Main()
    { 
        double saldoInicial = 1000.0;
        double comision = 0.01; // 1%
        bool realizarOtraOperacion = true;

        while (realizarOtraOperacion)
        {
            MenuDeDivisas();

            string divisaInicial = LeerDivisa("Ingrese su divisa inicial: ");
            string divisaDestino = LeerDivisa("Ingrese la divisa a la que desea cambiar: ");

            Console.Write("Ingrese la cantidad a cambiar: ");
            double cantidad = Convert.ToDouble(Console.ReadLine());

            Console.Write("¿Desea retirar los fondos? (Sí/No): ");
            string respuestaRetiro = Console.ReadLine().ToLower();

            if (respuestaRetiro == "si")
            {
                double montoConComision = CalcularMontoConComision(cantidad, comision);
                if (VerificarLimites(divisaDestino, montoConComision))
                {
                    RealizarCambioDivisas(ref saldoInicial, divisaInicial, divisaDestino, montoConComision);
                    realizarOtraOperacion = PreguntarOtraOperacion();
                }
                else
                {
                    Console.WriteLine($"El monto con comisión excede los límites permitidos para {divisaDestino}. Operación cancelada.");
                }
            }
            else
            {
                realizarOtraOperacion = PreguntarOtraOperacion();
            }
        }
    }
    static void MenuDeDivisas()
    {
        Console.WriteLine("=== Menú de Divisas ===");
        Console.WriteLine("CLP - Pesos Chilenos");
        Console.WriteLine("ARS - Pesos Argentinos");
        Console.WriteLine("USD - Dólares Americanos");
        Console.WriteLine("EUR - Euros");
        Console.WriteLine("TRY - Liras Turcas");
        Console.WriteLine("GBP - Libras Esterlinas");
    }
    static string LeerDivisa(string mensaje)
    {
        Console.Write(mensaje);
        return Console.ReadLine().ToUpper();
    }

    static double CalcularMontoConComision(double cantidad, double comision)
    {
        return cantidad * (1 - comision);
    }
    static bool VerificarLimites(string divisa, double monto)
    {
        switch (divisa)
        {
            case "CLP":
                return monto >= 100 && monto <= 10000;
            case "ARS":
                return monto >= 10 && monto <= 1000;
            case "USD":
                return monto >= 1 && monto <= 100;
            case "EUR":
                return monto >= 1 && monto <= 100;
            case "TRY":
                return monto >= 5 && monto <= 500;
            case "GBP":
                return monto >= 1 && monto <= 100;
            default:
                return false;
        }
    }
    static void RealizarCambioDivisas(ref double saldo, string divisaInicial, string divisaDestino, double monto)
    {
        switch (divisaDestino)
        {
            case "CLP":
                saldo -= monto * 700;
                break;
            case "ARS":
                saldo -= monto * 100;
                break;
            case "USD":
                saldo -= monto;
                break;
            case "EUR":
                saldo -= monto * 0.85;
                break;
            case "TRY":
                saldo -= monto * 10;
                break;
            case "GBP":
                saldo -= monto * 0.75;
                break;
            default:
                break;
        }

        Console.WriteLine($"Cambio de {monto} {divisaInicial} a {monto} {divisaDestino} realizado con éxito.");
        Console.WriteLine($"Nuevo saldo: {saldo} {divisaInicial}");
    }

    static bool PreguntarOtraOperacion()
    {
        Console.Write("¿Desea realizar otra operación? (Sí/No): ");
        string respuesta = Console.ReadLine().ToLower();
        return respuesta == "si";
    }
}