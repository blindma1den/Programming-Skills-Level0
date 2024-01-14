#region Creamos usuarios de prueba

User userTest1 = new User
{
    Name = "luis",
    Password = "1234",
    Balance = 2000
};
User userTest2 = new User
{
    Name = "pedro",
    Password = "1234",
    Balance = 2000
};
List<User> ltUser = new List<User>();
ltUser.Add(userTest1);
ltUser.Add(userTest2);
#endregion
bool flagLogin = false;
int countErrorsLogin = 0;
string pressedKey = "";
int optionMenu = 0;
string userName = "";
string password = "";
User userLogged;
while (!flagLogin)
{
    countErrorsLogin++;
    Console.Clear();
    Console.WriteLine("Login Banco");
    Console.WriteLine("Ingrese Usuario");
    userName = Console.ReadLine();
    Console.WriteLine("Ingrese password");
    password = Console.ReadLine();
    if (ltUser.Where(x => x.Name == userName && x.Password == password).Count() == 1)
    {

        flagLogin = true;
    }
    if (countErrorsLogin == 3)
        break;
}
userLogged = userLogged = ltUser.FirstOrDefault(x => x.Name == userName && x.Password == password);
if (flagLogin)
{
    do
    {
        Console.Clear();
        Console.WriteLine("Elija alguna de las siguientes opciones");
        Console.WriteLine("1 - Depositar");
        Console.WriteLine("2 - Retirar");
        Console.WriteLine("3 - Ver");
        Console.WriteLine("4 - Transferir");
        Console.WriteLine("5 - Salir");
        pressedKey = Console.ReadLine();
    } while (!int.TryParse(pressedKey, out optionMenu) || optionMenu <= 0 || optionMenu >= 6);
    switch (optionMenu)
    {
        case 1:
            DepositMoneyUser(userLogged); break;
        case 2:
            WithDrawMoneyUser(userLogged); break;
        case 3:
            ViewMoneyUser(userLogged); break;
        case 4:
            DepositMoneyOtherUser(userLogged); break;
        default:
            break;
    }
}

Console.WriteLine("Adios!!");
#region Funciones
void DepositMoneyOtherUser(User userLogged)
{
    Console.Clear();
    Console.WriteLine("Ingrese el nombre de la persona a la que enviara dinero");
    string userNameToTransfer = Console.ReadLine();
    User userToTransfer = ltUser.FirstOrDefault(x => x.Name == userNameToTransfer);
    string mountToDeposit = "";
    int mount = 0;
    do
    {
        Console.WriteLine($"Usted puede enviar un maximo de ${userLogged.Balance}");
        mountToDeposit = Console.ReadLine();
    } while (!int.TryParse(mountToDeposit, out mount) || userLogged.Balance < mount);
    userToTransfer.DepositMoneyUser(mount);
    userLogged.WithDrawMoneyUser(mount);
}

void ViewMoneyUser(User userLogged)
{
    Console.Clear();
    Console.WriteLine($"Usted cuenta con ${userLogged.Balance} en su balance");
}

void WithDrawMoneyUser(User userLogged)
{
    Console.Clear();
    Console.WriteLine("¿Cuanto dinero retirara?");
    string mountToDeposit = "";
    int mount = 0;
    do
    {
        if (userLogged.Balance < mount)
        {
            Console.WriteLine($"Usted puede retirar un maximo de ${userLogged.Balance}");
        }
        mountToDeposit = Console.ReadLine();
    } while (!int.TryParse(mountToDeposit, out mount) || userLogged.Balance < mount);
    userLogged.WithDrawMoneyUser(mount);
}

void DepositMoneyUser(User userLogged)
{

    Console.Clear();
    Console.WriteLine("¿Cuanto dinero depositara?");
    string mountToDeposit = "";
    int mount = 0;
    do
    {
        mountToDeposit = Console.ReadLine();
    } while (!int.TryParse(mountToDeposit, out mount) && mount < 1);
    userLogged.DepositMoneyUser(mount);
}
#endregion

