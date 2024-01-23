package programmingBlind.Level0;

import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Punto 1 - Crear un homeBanking con las siguientes características:
		// Usuarios deben poder hacer logín con usuario y contraseña.

		/*
		 * Por defecto elijo un user y contraseña, para hacerlo más sencillo y poder
		 * avanzar
		 */
		// user: Petruza - pass: Petruza

		try (Scanner scanner = new Scanner(System.in)) {
			String user = "Petruza";
			String password = "Petruza";

			int intentos = 0;
			int paso = 0;
			int opcionDelUsuario;

			double fondosDelCliente = 2000;

			/* While que pregunta las 3 veces por el usuario y contraseña */

			while (intentos < 3 && paso == 0) {

				System.out.println("Por favor ingrese su usuario: ");
				String userIngresado = scanner.nextLine();
				System.out.println("Por favor ingrese su contraseña: ");
				String passIngresado = scanner.nextLine();

				// If donde solicito al usuario que ingrese nuevamente las credenciales porque
				// alguna fue erronea
				if ((!userIngresado.equals(user) || (!passIngresado.equals(password)))) {
					System.out.println(userIngresado);
					System.out.println(passIngresado);
					System.out.println("Usuario y/o contraseña incorrecto, intente nuevamente");

					intentos++;
					// Si no entré al if, entonces las credenciales fueron correctas y activo la
					// variable de control
				} else {

					paso = 1;

				}

			}

			// pregunto por el motivo de la salida del while:
			// Si fué por alcanzar el máximo de intentos (if) o por haber ingresado las
			// credenciales correctas (else)

			if (intentos == 3) {
				System.out.println("Usuario bloqueado por alcanzar la cantidad máxima de intentos");

			} else {

				System.out.println("Bienvenido al programa sarlanga");

				// Menu con las opciones que el cliente puede realizar

				do {

					System.out.println("Por favor elija una de las siguientes opciones: ");
					System.out.println("[1] - Para depositar fondos. ");
					System.out.println("[2] - Para retiro de fondos. ");
					System.out.println("[3] - Ver Saldo de cuenta. ");
					System.out.println("[4] - Realizar una transferencia. ");
					System.out.println("[0] - Para salir del sistema. ");

					opcionDelUsuario = scanner.nextInt();

					// Lógica para cada una de las opciones que el usuario puede elegir:

					switch (opcionDelUsuario) {

					case 1:
						// double deposito = 0;
						System.out.println("Usted eligió la opción 1: Depósito de fondos.");
						System.out.println("Actualmente dispone de " + fondosDelCliente + " Pesos");
						System.out.println("Por favor ingrese el monto que quiere depositar: ");

						// Sumo a los fondos actuales del cliente, el monto a depositar:

						double deposito = scanner.nextDouble();
						fondosDelCliente += deposito;

						System.out.println("Fondos depositados con éxito.");
						System.out.println("Ahora dispone de: " + fondosDelCliente + " Pesos");

						break;

					case 2:

						// Resto a los fondos actuales del cliente, el monto ingresado por el usuario.
						System.out.println("Usted eligió la opción 2: Retiro de fondos.");
						System.out.println("Actualmente dispone de " + fondosDelCliente + " Pesos");
						System.out.println("Por favor ingrese el monto que quiere retirar: ");

						double retiro = scanner.nextDouble();

						if (retiro > fondosDelCliente) {

							System.out.println("No posee fondos suficientes para realizar un retiro por ese monto");

						} else {

							fondosDelCliente -= retiro;

							System.out.println(
									"Se retiró el monto con exito, su saldo actualizado es: " + fondosDelCliente);
						}

						break;

					case 3:
						System.out.println("Eligió la opción 3 - Ver saldo de cuenta.");
						System.out.println("El saldo de su cuenta es: " + fondosDelCliente);
						break;

					case 4:

						System.out.println("Eligió la opción 4 - Transferencias.");
						System.out.println("El saldo actual de su cuenta es " + fondosDelCliente);
						System.out.println("Por favor seleccione el monto a transferir: ");

						double montoTransferencia = scanner.nextDouble();

						if (montoTransferencia < fondosDelCliente) {

							System.out.println(
									"Ingrese el numero de cuenta destino a la cual realizar la transferencia.");
							String cuentaDestino = scanner.next();

							fondosDelCliente -= montoTransferencia;

							// Ticket de la transferencia
							System.out.println("Transferencia realizada con exito, detalles de la transacción: ");
							System.out.println("Monto transferido: " + montoTransferencia);
							System.out.println("Cuenta destino: " + cuentaDestino);
							System.out.println("Saldo disponible, luego de la transferencia:" + fondosDelCliente);

						} else {

							System.out.println("No es posible realizar la transferencia, fondos insuficientes");

						}

						break;
					}

				} while (opcionDelUsuario != 0 && opcionDelUsuario > 4);
			}
		}
	}

}
