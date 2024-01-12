#ejercicio5
# Autor: Angel Alcántar
"""
5. Desarrollar una aplicación de gestión financiera con las siguientes características:
* El usuario registra sus ingresos totales.
* Hay categorías: Gastos médicos, gastos del hogar, ocio, ahorro y educación.
* El usuario puede enumerar sus gastos dentro de las categorías y obtener el total de cada categoría.
* El usuario podrá obtener el total de sus gastos.
* Si el usuario gasta la misma cantidad de dinero que gana, el sistema debería mostrar un mensaje advirtiendo al usuario que reduzca gastos en la categoría donde ha gastado más dinero.
* Si el usuario gasta menos de lo que gana, el sistema muestra un mensaje de felicitación en pantalla.
* Si el usuario gasta más de lo que gana, el sistema mostrará consejos para mejorar la salud financiera del usuario.
"""
#función para registrar ingresos.
def registrar_ingresos():
  return float(input("Ingrese sus ingresos totales: "))
#función para registrar gastos.
def registrar_gastos(categorias):
  gastos = {}
  for categoria in categorias:
    gastos[categoria] = float(input(f"Ingrese los gastos para {categoria}: "))
  return gastos
def calcular_total_gastos(gastos):
  return sum(gastos.values())

def comparar_ingresos_gastos(ingresos, gastos):
  total_gastos = calcular_total_gastos(gastos)
  if total_gastos == ingresos:
    categoria_mayor = max(gastos, key=gastos.get)
    print(f'Reduce tus gastos en {categoria_mayor}, estás gastando lo mismo que ganas. En total gastas {total_gastos} y tus ingresos son: {ingresos}.')
  elif total_gastos < ingresos:
    print("Felicidades, estás gastando menos de lo que ganas. En total gastas ", total_gastos, " y tus ingresos son: ", ingresos, ".")
  else:
    print("Debes mejorar tu salud financiera, estás gastando más de lo que ganas. En total gastas: ", total_gastos, " y tus ingresos son: ", ingresos, ".")
    
def gestion_financiera():
  ingresos = registrar_ingresos()
  categorias = ["Gastos médicos", "Gastos del hogar", "Ocio", "Ahorro", "Educación"]
  gastos = registrar_gastos(categorias)
  comparar_ingresos_gastos(ingresos, gastos)
  
  #arrancar el programa.
gestion_financiera()