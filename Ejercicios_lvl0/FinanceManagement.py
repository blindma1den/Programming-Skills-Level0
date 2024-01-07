# Por Felipe (ZenTial)

# Ejercicio 5
# Develop a finance management application with the following features: The user records their total
# income. There are categories: Medical expenses, household expenses, leisure, savings, and education. The user can
# list their expenses within the categories and get the total for each category. The user can obtain the total of
# their expenses. If the user spends the same amount of money they earn, the system should display a message advising
# the user to reduce expenses in the category where they have spent the most money. If the user spends less than they
# earn, the system displays a congratulatory message on the screen. If the user spends more than they earn,
# the system will display advice to improve the user's financial health.
from os import system


# Función de lista de gastos del programa
def inicio(dic_gastos):
    gastos = {}
    for gasto in dic_gastos:
        gastos[gasto] = int(input(f'Ingrese el gasto para {gasto}: '))
    return gastos


# Función del menu del programa
def menu(nombres, valores, sueldo, dic):
    total_gastado = sum(valores)
    while True:
        system('cls')
        print('*' * 50)
        comparacion_gastos(sueldo, valores, dic)
        print('*' * 50)
        print(f'Su sueldo actual es: ${sueldo} CLP')
        print(f'Actualmente estas gastando: ${total_gastado}CLP')
        print('*' * 50)
        contador = 1
        for (nombre, valor) in zip(nombres, valores):
            print(f'[{contador}] {nombre} : ${valor} CLP')
            contador += 1
        print('[6] Salir del programa')
        print('*' * 50)
        try:
            eleccion = input('Elije una categoria para cambiar los gastos: ')
            ['1', '2', '3', '4', '5', '6'].index(eleccion)

        except ValueError:
            system('cls')
            print('Ingrese una opción correcta')
        else:
            return eleccion


# Función comparación gastos
def comparacion_gastos(sueldo, lista_total, dic):
    total = sum(lista_total)
    keys = list(dic.keys())
    values = list(dic.values())
    posicion = values.index(max(values))
    gasto_mayor = keys[posicion]
    if sueldo == total:
        print(f'Estas gastando lo mismo que lo que ganas, deberias reducir tus gastos en {gasto_mayor}')
    elif sueldo > total:
        print('Felicitaciones, administraste tu dinero de manera eficiente.')
    else:
        print('Estas gastando demasiado por lo que estas perdiendo dinero, revisa en donde puedes reducir tus gastos.')


# Función principal del programa
def main():
    dic_gastos = {'Gastos medicos': 0,
                  'Gastos del hogar': 0,
                  'Entretenimiento': 0,
                  'Ahorros': 0,
                  'Educación': 0}
    sueldo = int(input('Por favor, ingrese su sueldo: '))
    dic_gastos = inicio(dic_gastos)
    while True:
        print('*' * 50)
        accion = menu(dic_gastos.keys(), dic_gastos.values(), sueldo, dic_gastos)
        if accion == '1':
            system('cls')
            dic_gastos['Gastos medicos'] = int(input('Ingrese el valor nuevo: '))
            system('cls')
            continue
        elif accion == '2':
            system('cls')
            dic_gastos['Gastos del hogar'] = int(input('Ingrese el valor nuevo: '))
            system('cls')
            continue
        elif accion == '3':
            system('cls')
            dic_gastos['Entretenimiento'] = int(input('Ingrese el valor nuevo: '))
            system('cls')
            continue
        elif accion == '4':
            system('cls')
            dic_gastos['Ahorros'] = int(input('Ingrese el valor nuevo: '))
            system('cls')
            continue
        elif accion == '5':
            system('cls')
            dic_gastos['Educación'] = int(input('Ingrese el valor nuevo: '))
            system('cls')
            continue
        else:
            system('cls')
            print('Su programa ha sido finalizado')
            return False


if __name__ == '__main__':
    main()
