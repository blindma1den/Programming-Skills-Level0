package programmingBlind.Level0;

import java.util.Scanner;

import java.util.Random;

public class Ejercicio4 {

	private static final String NOMBREUSUARIO = "Garlopa";
	private static final String PASSWORD = "Garlopa";
	private static final int CANTMAXINTENTOSLOGIN = 3;
	private static final double COSTOCARGOPORKILO = 2;
	private static int intentosLogin = 0;
	private static String optNuevaOperacion;
	private static double pesoPaquete;
	private static Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) {
		login();

		boolean salidaDelSistema = false;

		do {
			System.out.println("Bienvenido al sistema de envio de paquetes.");
			System.out.println("Por favor elija la opción de lo que desea hacer:");
			System.out.println("[1] - Para enviar un paquete.");
			System.out.println("[2] - Para salir del sistema");

			int eleccion = scanner.nextInt();

			switch (eleccion) {

			case 1:

				enviarPaquete();
				break;

			case 2:

				salidaDelSistema = true;
				break;

			default:

				System.out.println("Opcion no válida, por favor intente nuevamente");

			}

			if (!salidaDelSistema) {

				System.out.println("Desea realizar una nueva operación? [S]I / [N]O");
				optNuevaOperacion = scanner.next();

				if (!optNuevaOperacion.equalsIgnoreCase("s")) {

					salidaDelSistema = true;

				}

			}

		} while (!salidaDelSistema);

		System.out.println("Gracias por enviar paquetes a través de nosotros, que tenga buen dia!!!");

	}

	private static void login() {

		do {

			System.out.println("Por favor ingrese usuario y contraseña.");

			System.out.print("Usuario: ");
			String nombreUsuario = scanner.next();

			System.out.print("Contraseña: ");
			String contraseña = scanner.next();

			if (nombreUsuario.equals(NOMBREUSUARIO) && contraseña.equals(PASSWORD)) {

				System.out.println("Login realizado con exito...");
				break;
			} else {

				System.out.println("Nombre de usuario y/o contraseña incorrectos, por favor intente nuevamente");
				intentosLogin++;

				if (intentosLogin == CANTMAXINTENTOSLOGIN) {

					System.out.println("Se alcanzó la cantidad máxima de intentos, salida del sistema");
					System.exit(0);
				}
			}

		} while (true);

	}

	private static void enviarPaquete() {

		double costoPaquete;
		String remitente;
		String destinatario;

		System.out.println("Por favor, ingrese el peso en KG del paquete a enviar: ");
		pesoPaquete = scanner.nextDouble();

		costoPaquete = pesoPaquete * COSTOCARGOPORKILO;
		System.out.println("El costo por envíar el paquete será de: " + costoPaquete);

		System.out.println("Ingrese el nombre del remitente");
		remitente = scanner.next();

		System.out.println("Ingrese el nombre del destinatario");
		destinatario = scanner.next();

		System.out.println("Datos necesarios completados con exito. Detalles del paquete a enviar:");
		System.out.println("Se enviará un paquete nro. " + generarNumeroPaquete());
		System.out.println("Cuyo Remitente es: " + remitente);
		System.out.println("El Destinatario será: " + destinatario);
		System.out.println("El costo de envio del mismo será: " + costoPaquete);

	}

	private static int generarNumeroPaquete() {

		Random random = new Random();

		int numeroPaquete = random.nextInt(1000) + 1;

		return numeroPaquete;

	}

}
