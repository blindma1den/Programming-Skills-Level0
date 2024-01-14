#region Creamos usuarios de prueba y stocks

using UniversityEnrollment;

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

List<Programs> ltProgram = [];

List<User> ltUser = [];
ltUser.Add(userTest1);
ltUser.Add(userTest2);

Programs pr = new()
{
    citieId = 1,
    programId = 1,
    userId = 1
};
ltProgram.Add(pr);
#endregion
bool flagLogin = false;
int countErrorsLogin = 0;
string userName = "";
string password = "";
string pressedKey = "";
string pressedKeyCities = "";
int optionMenu = 0;
int optionMenuCities = 0;
User userLogged;
while (!flagLogin)
{
    countErrorsLogin++;
    Console.Clear();
    Console.WriteLine("Login Universidad");
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
      
        if (string.IsNullOrEmpty(userLogged.Name))
        {
            Console.WriteLine("Ingrese su nombre:");
            userLogged.Name = Console.ReadLine();
        }
        if (string.IsNullOrEmpty(userLogged.LastName))
        {
            Console.WriteLine("Ingrese su apellido:");
            userLogged.LastName = Console.ReadLine();
        }
        Console.WriteLine("Elija alguna de las siguientes materias");
        Console.WriteLine("1 - Computer Science");
        Console.WriteLine("2 - Medicine");
        Console.WriteLine("3 - Marketing");
        Console.WriteLine("4 - Arts");
        Console.WriteLine("5 - Salir");
        pressedKey = Console.ReadLine();
        Console.WriteLine("Elija alguna de los siguientes ciudades");
        Console.WriteLine("1 - London");
        Console.WriteLine("2 - Manchester");
        Console.WriteLine("3 - Liverpool");
        pressedKeyCities = Console.ReadLine();
    } while (!validateStocksProgram(pressedKey, pressedKeyCities));

}

bool validateStocksProgram(string pressedKey, string pressedKeyCities)
{
    if (!int.TryParse(pressedKey, out optionMenu))
    {
        return false;
    }
    if (!int.TryParse(pressedKeyCities, out optionMenuCities))
    {
        return false;
    }
    if (optionMenu <= 0 || optionMenu >= 6)
    {
        return false;
    }
    if (ltProgram.Where(x => x.programId == optionMenu).Count() == 5)
    {
        Console.Clear();
        Console.WriteLine("La materia ya tiene las 5 vacantes ocupadas.Reitentar con otra carrera");
        return false;
    }
    if (optionMenuCities == (int)Cities.London || optionMenuCities == (int)Cities.Liverpool)
    {
        if (ltProgram.Where(x => x.programId == optionMenu &&
                                 x.citieId == (int)Cities.London).Count() == 1)
        {
            Console.Clear();
            Console.WriteLine("El campus tiene todas las vacantes ocupadas para esta materia");
            return false;
        }
    }
    if (optionMenuCities == (int)Cities.Manchester)
    {
        if (ltProgram.Where(x => x.programId == optionMenu &&
                                 x.citieId == (int)Cities.Manchester).Count() == 3)
        {
            Console.Clear();
            Console.WriteLine("El campus tiene todas las vacantes ocupadas para esta materia");
            return false;
        }
    }
    Programs pr = new()
    {
        citieId = optionMenuCities,
        programId = optionMenu,
        userId = userLogged.Id
    };
    ltProgram.Add(pr);
    return true;
}
enum Cities
{
    London = 1,
    Manchester = 2,
    Liverpool = 3
}