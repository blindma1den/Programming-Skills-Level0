
using FinanceManagement;

Console.WriteLine("Ingrese su sueldo");
int earned = int.Parse(Console.ReadLine());
int opcion = 0;
List<FinanceUser> ltFu = [];

do
{
    Console.WriteLine("Menu de opciones");
    Console.WriteLine("1 - Gastos medicos");
    Console.WriteLine("2 - Gastos del hogar");
    Console.WriteLine("3 - Ahorro");
    Console.WriteLine("4 - Ocio");
    Console.WriteLine("5 - Educacion");
    Console.WriteLine("6 - Revisar gastos");
    Console.WriteLine("7 - Salir");
    opcion = int.Parse(Console.ReadLine());

    if (opcion != 6)
    {
        Console.WriteLine("Ingrese gastos medicos");
        int Expenses = int.Parse(Console.ReadLine());
        Console.WriteLine("Ingrese nombre o detalle del gasto");
        string details = Console.ReadLine();
        FinanceUser fm = new()
        {
            Amount = Expenses,
            Details = details,
            tipo = opcion
        };
        ltFu.Add(fm);
    }
    else
    {
        if (ltFu.Count() == 0)
        {
            Console.WriteLine("Aun no ingresa sus gastos");
        }
        else
        {
            int medicalExpenses = ltFu.Where(x => x.tipo == 1).Sum(x => x.Amount);
            int householdExpenses = ltFu.Where(x => x.tipo == 2).Sum(x => x.Amount);
            int leisureExpenses = ltFu.Where(x => x.tipo == 3).Sum(x => x.Amount);
            int savingsExpenses = ltFu.Where(x => x.tipo == 4).Sum(x => x.Amount);
            int educationExpenses = ltFu.Where(x => x.tipo == 5).Sum(x => x.Amount);
            Console.WriteLine($"Gastos en Medicina ${medicalExpenses}");
            Console.WriteLine($"Gastos en Medicina ${householdExpenses}");
            Console.WriteLine($"Gastos en Medicina ${leisureExpenses}");
            Console.WriteLine($"Gastos en Medicina ${savingsExpenses}");
            Console.WriteLine($"Gastos en Medicina ${educationExpenses}");
            if (ltFu.Sum(x => x.Amount) == earned)
            {
                Console.WriteLine("Tus sueldo y gastos son iguales.");
                var MaxExpenses = ltFu.GroupBy(x => x.tipo).Select(t => new
                {
                    tipo = t.Key,
                    Amount = t.Sum(ta => ta.Amount),
                }).OrderByDescending(x => x.Amount).ToList();
                string tipo = "";
                switch (MaxExpenses[0].tipo)
                {
                    case 1:
                        tipo = "Gastos medicos";
                        break;
                    case 2:
                        tipo = "Gastos del hogar";
                        break;
                    case 3:
                        tipo = "Ahorro";
                        break;
                    case 4:
                        tipo = "Ocio";
                        break;
                    case 5:
                        tipo = "Educacion";
                        break;
                    default:
                        break;
                }

                Console.WriteLine($"Tu gasto mayor es en {tipo} con un total de {MaxExpenses[0].Amount}");
            }
            else
            {
                if (ltFu.Sum(x => x.Amount) < earned)
                {
                    Console.WriteLine("Cuidado estan gastando mas de lo que ganas");
                }
                else
                {
                    Console.WriteLine("Felicidades tus finanzas estan sanas!!!");
                }
            }
        }
    }
} while (opcion != 7);
