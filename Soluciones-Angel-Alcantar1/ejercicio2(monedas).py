#ejercicio 2
"""
2. Cree un conversor de moneda entre CLP, ARS, USD, EUR, TRY, GBP con las siguientes características:
* El usuario debe elegir su moneda inicial y la moneda a la que desea cambiar.
* El usuario puede elegir si desea retirar o no sus fondos. Si deciden no retirarse, debería volver al menú principal.
*Si el usuario decide retirar los fondos, el sistema cobrará una comisión del 1%.
* Establece un monto mínimo y máximo para cada moneda, puede ser de tu elección.
* El sistema debe preguntar al usuario si desea realizar otra operación. Si deciden hacerlo, debería reiniciar el proceso; de lo contrario, el sistema debería cerrarse.
"""
#Angel Alcántar
#diccionario de monedas y sus valores base con respecto a una, en este caso el usd
monedas = {
		"clp": 0.0014,
		"ars": 0.010,
		"usd": 1,
		"eur": 1.21,
		"try": 0.12,
		"gbp": 1.39
}
#establecer montos mínimos y máximos para cada moneda
montos = {
		"clp": [1000, 1000000],
		"ars": [10, 100000],
		"usd": [1, 10000],
		"eur": [1, 10000],
		"try": [1, 10000],
		"gbp": [1, 10000]
}#función para convertir monedas de una a otra
def convertir_monedas(monto, moneda_inicial, moneda_final):
	if moneda_inicial == moneda_final:
		return monto
	else:
		return monto * monedas[moneda_final] / monedas[moneda_inicial]
#función para calcular la comisión
def calcular_comision(monto):
	return monto * 0.01
def verificar_monto(monto, moneda):
	minimo, maximo = montos[moneda]
	try:
		monto_numerico = float(monto)
		return minimo <= monto_numerico <= maximo
	except ValueError:
		return False
#función para el menú y todo lo que se necesita

def menu():
	while(True):
		moneda_origen = input("Ingrese la moneda de origen (CLP, ARS, USD, EUR, TRY, GBP): ").lower()
		moneda_destino = input("Ingrese la moneda de destino (CLP, ARS, USD, EUR, TRY, GBP): ").lower()
		monto = input("Ingrese el monto a convertir: ")
		try:
			monto_numerico = float(monto)
		except ValueError:
			print("El monto ingresado no es válido.")
			continue
		if not verificar_monto(monto_numerico, moneda_origen):
			print("El monto ingresado no es válido.")
			continue
		monto_convertido = convertir_monedas(float(monto), moneda_origen, moneda_destino)
		print(f"El monto convertido es: {monto_convertido}")
		retirar = input("¿Desea retirar sus fondos? (S/N): ").lower()
		if retirar == "s":
			monto_convertido = monto_convertido - calcular_comision(monto_convertido)
			print(f"El monto a retirar es: {monto_convertido}")
		else:
			print("Gracias por usar nuestro servicio.")
		realizar_otra = input("¿Desea realizar otra operación? (S/N): ").lower()
		if realizar_otra != "s":
			break
if __name__ == "__main__":
	menu()