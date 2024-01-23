package programmingBlind.Level0;

import java.util.Scanner;

public class Ejercicio2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		double porcentajeComision = 0.01; // el 1% de comisión
		int opcMonedaOrigen;
		do {
			int opt;

			int opcMonedaDestino;
			double montoAConvertir;
			String opcRetiroFondos;

			// 1 USD = 811.76 ARS, 887.54 PLC, 0.91 EUR, 29.76 TRY, 0.79 LBR
			System.out.println("Por favor seleccione la moneda origen: ");
			System.out.println("[1] - USD - (Dólares Estadounidenses)");
			System.out.println("[2] - ARS - (Pesos Argentinos)");
			System.out.println("[3] - PLC - (Pesos Chilenos)");
			System.out.println("[4] - EUR - (Euros)");
			System.out.println("[5] - TRY - (Lira Turca");
			System.out.println("[6] - LBR - (Libra Esterlina)");
			System.out.println("[0] - salir del sistema");

			opcMonedaOrigen = scanner.nextInt();

			// chequeo que la eleccion de la moneda origen sea válida
			if (opcMonedaOrigen >= 1 && opcMonedaOrigen <= 6) {

				System.out.println("Por favor elija la moneda destino:");

				opcMonedaDestino = scanner.nextInt();
				// chequeo que la opción de la moneda destino sea válida
				if (opcMonedaDestino >= 1 && opcMonedaDestino <= 6) {

					System.out.println("Por favor ingrese el monto a convertir: ");

					montoAConvertir = scanner.nextDouble();

					// chequeo que el monto de la conversión sea el permitido

					if (esMontoValido(opcMonedaOrigen, montoAConvertir)) {

						double montoConvertido = convertirMoneda(opcMonedaOrigen, opcMonedaDestino, montoAConvertir);

						System.out.println("El monto convertido corresponde a: " + montoConvertido);
						System.out.println("Desea retirar sus fondos? [S]i / [N]o");
						opcRetiroFondos = scanner.next();

						if (opcRetiroFondos.equalsIgnoreCase("S")) {

							double comision = montoConvertido * porcentajeComision;
							double montoNeto = montoConvertido - comision; // montoNeto es el monto con el descuento de
																			// las comisiones

							System.out.println("Monto a retirar, descontando comisión: " + montoNeto);

						}

						System.out.println("Desea realizar otra operación? [S]i / [N]o:");

						String otraOperacion = scanner.next();

						if (!otraOperacion.equalsIgnoreCase("S")) {

							break; // Salgo del do while porque no quiero realizar ninguna operación

						}
					} else {

						System.out.println("El monto no es válido, para la moneda a convertir");

					}

				}

			} /*
				 * else if(opcMonedaOrigen == 0) {
				 * 
				 * System.out.println("Gracias, vuelva pronto (no usaste el sistema"); break;
				 * 
				 * }
				 */

		} while (opcMonedaOrigen != 0); // valor anterior: true

		System.out.println("Gracias por usar el sistema");

	}

	private static double convertirMoneda(int opcMonedaOrigen, int opcMonedaDestino, double montoAConvertir) {
		// 1 USD = 811.76 ARS, 887.54 PLC, 0.91 EUR, 29.76 TRY, 0.79 LBR
		switch (opcMonedaOrigen) {

		case 1: { // caso donde la moneda origen es U$D, agrego todas las posibles elecciones de
					// moneda destino.

			if (opcMonedaDestino == 1) {

				montoAConvertir *= 1;

			} else if (opcMonedaDestino == 2) {

				montoAConvertir *= 811.76;

			} else if (opcMonedaDestino == 3) {

				montoAConvertir *= 887.54;

			} else if (opcMonedaDestino == 4) {

				montoAConvertir *= 0.91;

			} else if (opcMonedaDestino == 5) {

				montoAConvertir *= 29.76;

			} else if (opcMonedaDestino == 6) {

				montoAConvertir *= 0.79;

			}
		}
			break;

		case 2: { // caso donde la moneda origen es ARS, agrego todas las posibles elecciones de
					// moneda destino.

			if (opcMonedaDestino == 1) {

				montoAConvertir /= 811.76;

			} else if (opcMonedaDestino == 2) {

				montoAConvertir *= 1;

			} // hasta acá estpa bien, para abajo....seguir haciendo los if como corresponde.

			else if (opcMonedaDestino == 3) {

				montoAConvertir /= 811.76; // lo paso a U$D
				montoAConvertir *= 887.54;// Los dólares los paso a PLC

			} else if (opcMonedaDestino == 4) {

				montoAConvertir /= 811.76; // lo paso a U$D
				montoAConvertir *= 0.91; // Convierto los dólares a Euros

			} else if (opcMonedaDestino == 5) {

				montoAConvertir /= 811.76; // lo paso a U$D
				montoAConvertir *= 29.76; // convierto los dólares a TRY

			} else if (opcMonedaDestino == 6) {
				montoAConvertir /= 811.76; // lo paso a U$D
				montoAConvertir *= 0.79; // Convierto los dólares a LBR

			}

		}
			break;

		case 3: { // caso donde la moneda origen es PLC, agrego todas las posibles elecciones de
			// moneda destino.

			if (opcMonedaDestino == 1) {

				montoAConvertir /= 887.54;

			} else if (opcMonedaDestino == 2) {

				montoAConvertir /= 887.54; // lo paso a U$D
				montoAConvertir *= 811.76;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 3) {

				montoAConvertir *= 1;// Mismo monto

			} else if (opcMonedaDestino == 4) {

				montoAConvertir /= 887.54; // lo paso a U$D
				montoAConvertir *= 0.91; // Los dólares los paso a EUR

			} else if (opcMonedaDestino == 5) {

				montoAConvertir /= 887.54; // lo paso a U$D
				montoAConvertir *= 29.76;// Los dólares los paso a TRY

			} else if (opcMonedaDestino == 6) {

				montoAConvertir /= 887.54; // lo paso a U$D
				montoAConvertir *= 0.79;// Los dólares los paso a LBR

			}

		}
			break;

		case 4: {

			if (opcMonedaDestino == 1) {

				montoAConvertir /= 0.91;

			} else if (opcMonedaDestino == 2) {

				montoAConvertir /= 0.91; // lo paso a U$D
				montoAConvertir *= 811.76;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 3) {

				montoAConvertir /= 0.91; // lo paso a U$D
				montoAConvertir *= 887.54;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 4) {

				montoAConvertir *= 1;

			} else if (opcMonedaDestino == 5) {

				montoAConvertir /= 0.91; // lo paso a U$D
				montoAConvertir *= 27.76;// Los dólares los paso a TRY

			} else if (opcMonedaDestino == 6) {

				montoAConvertir /= 0.91; // lo paso a U$D
				montoAConvertir *= 0.79; // Los dólares los paso a LBR

			}

		}
			break;

		case 5: {

			if (opcMonedaDestino == 1) {

				montoAConvertir /= 29.76;

			} else if (opcMonedaDestino == 2) {

				montoAConvertir /= 29.76; // lo paso a U$D
				montoAConvertir *= 811.76;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 3) {

				montoAConvertir /= 29.76; // lo paso a U$D
				montoAConvertir *= 887.54;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 4) {

				montoAConvertir /= 29.76; // lo paso a U$D
				montoAConvertir *= 0.91; // los dólares los paso a EUR

			} else if (opcMonedaDestino == 5) {

				montoAConvertir *= 1;

			} else if (opcMonedaDestino == 6) {

				montoAConvertir /= 29.76; // lo paso a U$D
				montoAConvertir *= 0.79; // Los dólares los paso a LBR

			}

		}
			break;

		case 6: {

			if (opcMonedaDestino == 1) {

				montoAConvertir /= 0.79;

			} else if (opcMonedaDestino == 2) {

				montoAConvertir /= 0.79; // lo paso a U$D
				montoAConvertir *= 811.76;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 3) {

				montoAConvertir /= 0.79; // lo paso a U$D
				montoAConvertir *= 887.54;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 4) {

				montoAConvertir /= 0.79; // lo paso a U$D
				montoAConvertir *= 0.91;// Los dólares los paso a ARS

			} else if (opcMonedaDestino == 5) {

				montoAConvertir /= 0.79; // lo paso a U$D
				montoAConvertir *= 29.76;// Los dólares los paso a TRY

			} else if (opcMonedaDestino == 6) {

				montoAConvertir *= 1; // lo paso a U$D

			}

		}
			break;

		}
		return montoAConvertir;
	}

	private static boolean esMontoValido(int opcMonedaOrigen, double montoAConvertir) {

		boolean rangoMinMax = false;

		switch (opcMonedaOrigen) {

		case 1:

			rangoMinMax = montoAConvertir >= 100 && montoAConvertir <= 1000;
			break;

		case 2:
			rangoMinMax = montoAConvertir >= 10000 && montoAConvertir <= 1000000;
			break;
		case 3:
			rangoMinMax = montoAConvertir >= 10000 && montoAConvertir <= 1000000;
			break;
		case 4:
			rangoMinMax = montoAConvertir >= 100 && montoAConvertir <= 1000;
			break;
		case 5:
			rangoMinMax = montoAConvertir >= 1000 && montoAConvertir <= 100000;
			break;
		case 6:
			rangoMinMax = montoAConvertir >= 100 && montoAConvertir <= 10000;
			break;
		}

		return rangoMinMax;
	}
}
