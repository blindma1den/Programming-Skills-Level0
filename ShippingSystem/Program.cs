#region Creamos usuarios de prueba y stocks

using System.Reflection;

User userTest1 = new User
{
    Id = 1,
    UserName = "luis",
    Password = "1234"
};
User userTest2 = new User
{
    Id = 2,
    UserName = "pedro",
    Password = "1234"
};
List<User> ltUser = [];
ltUser.Add(userTest1);
ltUser.Add(userTest2);
List<Packages> ltPck = [];
#endregion
bool flagLogin = false;
int countErrorsLogin = 0;
string userName = "";
string password = "";
string pressedKey = "";
string sender = "";
string recipient = "";
int optionMenu = 0;
int weight = 0;
string weightPressed = "";
int accepted = 0;
string acceptedPressed = "";
User userLogged;
while (!flagLogin)
{
    countErrorsLogin++;
    Console.Clear();
    Console.WriteLine("Login Shipping");
    Console.WriteLine("Ingrese Usuario");
    userName = Console.ReadLine();
    Console.WriteLine("Ingrese password");
    password = Console.ReadLine();
    if (ltUser.Where(x => x.UserName == userName && x.Password == password).Count() == 1)
    {
        flagLogin = true;
    }
    if (countErrorsLogin == 3)
        break;
}
userLogged = ltUser.FirstOrDefault(x => x.UserName == userName && x.Password == password);
if (flagLogin)
{
    do
    {
        Console.WriteLine("Elija alguna de las siguientes opciones");
        Console.WriteLine("1 - Enviar Paquete");
        Console.WriteLine("2 - Salir");
        pressedKey = Console.ReadLine();
        Console.WriteLine("Ingrese los datos del remitente");
        sender = Console.ReadLine();
        Console.WriteLine("Ingrese los datos del destinatario");
        recipient = Console.ReadLine();
    } while (!validate(pressedKey, sender, recipient));
}

bool validate(string pressedKey, string sender, string recipient)
{
    if (!int.TryParse(pressedKey, out optionMenu))
    {
        return false;
    }
    Random random = new Random();
    do
    {
        Console.WriteLine("Ingrese peso del paquete");
        weightPressed = Console.ReadLine();
    } while (!int.TryParse(weightPressed, out weight));
    Console.WriteLine($"Usted debe pagar ${weight * 2} pesos");
    Packages pck = new()
    {
        id = random.Next(),
        RecipientDetails = recipient,
        Sender = sender,
        Weight = weight
    };
    ltPck.Add(pck);
    Console.WriteLine($"Su numero de atencion es {pck.id}");
    do
    {
        Console.WriteLine("Desea realizar otra operacion");
        Console.WriteLine("1- Si");
        Console.WriteLine("1- No");
        acceptedPressed = Console.ReadLine();
    } while (!int.TryParse(acceptedPressed, out accepted));

    if (accepted == 1)
    {
        return false;
    }
    Console.Clear();
    return true;
}
