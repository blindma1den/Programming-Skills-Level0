#ejercicio3
#Angel Alcántar
"""
3. Create an university enrollment system with the following characteristics:
* 		The system has a login with a username and password.
* 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
* 		The user must input their first name, last name, and chosen program.
* 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 		If login information is incorrect three times, the system should be locked.
* 		The user must choose a campus from three cities: London, Manchester, Liverpool.
* 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
* 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
"""

#guardaremos los datos en un diccionario
#datos de usuarios y contraseñas.
usuarios = {"admin": "admin123"}
# Programas y cupos por campus
programas_cupos = {
    "Informática": {"Londres": 1, "Manchester": 3, "Liverpool": 1},
    "Medicina": {"Londres": 1, "Manchester": 3, "Liverpool": 1},
    "Marketing": {"Londres": 1, "Manchester": 3, "Liverpool": 1},
    "Artes": {"Londres": 1, "Manchester": 3, "Liverpool": 1}
}
#alumnos registrados
alumnos_registrados = []
def login(usuarios):
    intentos = 0
    while(intentos <3):
      usuario = input("Ingrese su usuario: ")
      contraseña = input("Ingrese su contraseña: ")
      if usuarios.get(usuario) == contraseña:
        return True
      else:
        intentos += 1
        print("Usuario o contraseña incorrectos.")
    return False

def registrar_alumno():
  nombre = input("Ingrese su nombre: ")
  apellido = input("Ingrese su apellido: ")
  print("programas disponibles: Informática, Medicina, Marketing, Artes")
  programa = input("Ingrese el programa al que desea inscribirse: ")
  campus = input("Elija un campus (Londres, Manchester, Liverpool): ")
  return {"nombre": nombre, "apellido": apellido, "programa": programa, "campus": campus}

def verificar_cupo(programa, campus):
  if programas_cupos[programa][campus] > 0:
      programas_cupos[programa][campus] -= 1
      return True
  return False

def sistema_matricula():
  if login(usuarios):
    alumno = registrar_alumno()
    if verificar_cupo(alumno["programa"], alumno["campus"]):
      alumnos_registrados.append(alumno)
      print("Matrícula exitosa.")
    else:
      print("No hay cupos disponibles en el programa y campus seleccionados.")
  else:
    print("Ha excedido el número de intentos.")
    


if __name__ == "__main__":
    sistema_matricula()