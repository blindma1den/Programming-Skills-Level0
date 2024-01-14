#region variables
var currencyValues = new Dictionary<string, double>()
{
    { "USD", 1.00},
    { "CLP", 887.48 },
    { "ARG", 811.74  },
    { "EUR", 0.91  },
    { "TRY",29.85 },
    { "GBP", 0.79  }
};
int optionMenu = 0, optionMenuSecundary = 0, initialCurrency = 0, finalCurrency = 0;
string pressedKeySecundaryMenu;
#endregion
Console.WriteLine("Bienvenido al convertidor de moneda del Grupo de estudio!!!");
while (optionMenu != 2)
{
    Console.WriteLine("Menu de opciones");
    Console.WriteLine("------------------------------------------");
    Console.WriteLine("1 - Cambiar moneda");
    Console.WriteLine("2 - Salir del programa");
    Console.WriteLine("------------------------------------------");
    string pressedKey = Console.ReadLine();
    if (int.TryParse(pressedKey, out optionMenu) && (optionMenu == 1 || optionMenu == 2))
    {
        if (optionMenu == 2)
        {
            Console.Clear();
            Console.WriteLine("Hasta la proxima");
        }
        initialCurrency = showMenuSecundary("Elija una moneda");
        finalCurrency = showMenuSecundary("Elija la moneda que desea obtener");

        int mountToChange = readMountToChange();
        double valueConverted = resultConvert(currencyValues.ElementAt(initialCurrency - 1).Value, currencyValues.ElementAt(finalCurrency - 1).Value, mountToChange);
        Console.WriteLine($"Felicidades tu cambio es {Math.Floor(valueConverted * 0.99)}");

        //int optionfinalcurrency = readoptionfinal();
        //if (optionfinalcurrency == 2)
        //{
        //    break;
        //}
    }
    else
    {
        Console.WriteLine("La opcion ingresada no es valida");
    }
    #region Volvemos valores a 0 por si el usuario desea hacer otra operacion
    optionMenu = 0;
    optionMenuSecundary = 0;
    initialCurrency = 0;
    finalCurrency = 0;
    #endregion
}
#region Funciones
int readOptionFinal()
{
    int optionFinal = 0;
    string pressKeyOptionFinal = "";
    Console.WriteLine("¿Desea salir del programa o desea hacer otra conversion?");
    Console.WriteLine("1 - Realizar otra operacion");
    Console.WriteLine("2 - Salir del programa");
    do
    {
        pressKeyOptionFinal = Console.ReadLine();
    } while (!int.TryParse(pressKeyOptionFinal, out optionFinal) && (optionFinal == 1 || optionFinal == 2));
    return optionFinal;
}
int readMountToChange()
{
    int mountToChange = 0;
    string pressKeyMount = "";
    Console.WriteLine("¿Cuanto dinero quiere cambiar?");
    while (!int.TryParse(pressKeyMount, out mountToChange) || mountToChange < 1000 || mountToChange > 5700)
    {
        Console.WriteLine($"---Recuerda que el minimo a cambiar es 1000 y el maximo es 5700---");
        pressKeyMount = Console.ReadLine();
    }
    return mountToChange;
}
int showMenuSecundary(string messageMenu)
{
    do
    {
        Console.Clear();
        int count = 0;
        Console.WriteLine(messageMenu);
        foreach (var index in currencyValues)
        {
            count++;
            if (initialCurrency != count)
                Console.WriteLine($"{count} - {index.Key}");
        }
        pressedKeySecundaryMenu = Console.ReadLine();
    } while (!validateOptionMenuSecundary(pressedKeySecundaryMenu));
    return Convert.ToInt32(pressedKeySecundaryMenu);
}
bool validateOptionMenuSecundary(string pressedKeySecundaryMenu)
{
    return int.TryParse(pressedKeySecundaryMenu, out optionMenuSecundary) == true
            && optionMenuSecundary >= 1
            && optionMenuSecundary <= 6;
}
double resultConvert(double initialCurrency, double currencyToConvert, double mountToConvert)
{
    return (mountToConvert * currencyToConvert) / initialCurrency;
}
#endregion
