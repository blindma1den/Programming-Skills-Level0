# IMPORTS
import os

# CIUDADES
def escoger_ciudad(path, read_json_fn):
    data = read_json_fn(path)
    cities = []
    cities_index = {}

    for element in data:
        for city in element.keys():
            cities.append(city)

    print("Ciudades disponibles: \n")
    for index, city in enumerate(cities):
        index += 1
        print(f"{index}. {city}")
        cities_index[index] = city

    print("_" * len("Escoge una ciudad: "))
    option = int(input("Escoge una ciudad: "))
    city_chosen = cities_index[option]

    return city_chosen

# PROGRAMAS
def escoger_programas(path, read_json_fn):
    data = read_json_fn(path)
    programs = []
    programs_index = {}

    print("Programas disponibles: \n")

    for element in data:
        for program in element['londres'].keys():
            programs.append(program)

    for index, program in enumerate(programs):
        index += 1
        print(f"{index}- {program}")
        programs_index[index] = program

    print("-" * len("Escoge un programa: "))
    option = int(input("\nEscoge un programa: "))

    program_chosen = programs_index[option]

    return program_chosen


# ANALIZAR CUPOS
def analizar_opciones(usuario_logeado, program_chosen, city_chosen, path_programas, path_usuarios, read_json_fn, write_json_fn, escoger_ciudad, delete, attemps=3):
    os.system(delete)
    data_programas = read_json_fn(path_programas)
    data_usuarios = read_json_fn(path_usuarios)

    cupos_campus = data_programas[0][city_chosen][program_chosen]["cupos_campus"]
    cupos_programa = data_programas[0][city_chosen][program_chosen]["cupos_programa"]

    # Quisiera almacenar estas variables de manera independiente para saber cuál es el problema de cupos que se presenta
    # con el fin de presentar posibles soluciones
    estatus_campus = False if cupos_campus == 0 else True
    estatus_programa = False if cupos_programa == 0 else True

    if estatus_campus == True and estatus_programa == True:
        # Opciones escogidas
        print(f"Usuario: {usuario_logeado}")
        print(f"Programa: {program_chosen}")
        print(f"Ciudad: {city_chosen}\n")
        # Se restan los cupos
        data_programas[0][city_chosen][program_chosen]["cupos_campus"] -= 1
        data_programas[0][city_chosen][program_chosen]["cupos_programa"] -= 1

        write_json_fn(data_programas, path_programas)

        # Se inscribe al usuario
        for usuario in data_usuarios:
            if usuario['user'] == usuario_logeado:
                usuario['programa'] = program_chosen
                usuario['ciudad'] = city_chosen
                usuario['estatus_matricula'] = True
                write_json_fn(data_usuarios, path_usuarios)
                print("Usuario inscrito exitosamente")

    elif estatus_programa == False:
        print("Programa completo, lo lamentamos.")

    elif estatus_campus == False:
        attemps -= 1
        if attemps == 0:
            print("Numero de intentos agotados")
            return False
        print("Campus completo, ya no hay más cupos en este campus, lo lamentamos\n")
        print(f"Escoge otro campus          Intentos: {attemps}")
        nueva_ciudad = escoger_ciudad(path_programas, read_json_fn)
        analizar_opciones(usuario_logeado, program_chosen, city_chosen, path_programas,
                          path_usuarios, read_json_fn, write_json_fn, escoger_ciudad, delete, attemps)

    else:
        print("Ocurrío un error inesperado")
