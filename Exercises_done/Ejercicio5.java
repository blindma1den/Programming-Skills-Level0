package programmingBlind.Level0;

import java.util.Scanner;

public class Ejercicio5 {

	private static Scanner scanner = new Scanner(System.in);
	private static double ingresosMensuales;
	private static String[] categorias = { "Medicina", "Familia", "Esparcimiento", "Ahorros", "Educación" };
	private static double[] gastosPorCategoria = new double[5];
	private static int catMayorGasto;
	private static double gastosTotales;

	public static void main(String[] args) {

		// Usuario ingresa sus ingresos totales
		System.out.println("Bienvenido al programa de calculo de finanzas personales.");
		System.out.print("Por favor ingrese el monto de sus ingresos mensuales: ");
		ingresosMensuales = scanner.nextDouble();

		// Categorías de gastos: Medicos, Familia, Esparcimiento, Ahorros, Educación
		// El usuario puede ingresar cuáles fueron sus gastos en cada categoría, y luego
		// obtener el total de cada categoría.

		System.out.println("Por favor, para cada categoría, ingrese los gastos correspondientes: ");

		for (int i = 0; i < categorias.length; i++) {

			System.out.print("ingrese los gastos para la categoría " + categorias[i] + ":");
			double gasto = scanner.nextDouble();
			System.out.println();
			
			gastosPorCategoria[i] = gasto; // cargo en el array de gastos, el gasto actual para la categoría
											// correspondiente

			double mayorGasto = 0;

			// Si el gasto ingresado, es mayor al que está guardado como el gasto más
			// grande, entonces actualizao el valor y la categoría correspondiente.
			if (gasto > mayorGasto) {

				mayorGasto = gasto;
				catMayorGasto = i;

			}

		}

		System.out.print("Desea ver los gastos que ingresó para cada categoría? [S]i / [N]o: ");
		String opcion = scanner.next();

		if (opcion.equalsIgnoreCase("s")) {

			for (int i = 0; i < categorias.length; i++) {

				System.out.println("Categoría: " + categorias[i] + "--->  $" + gastosPorCategoria[i]);

			}
		}

		// El usuario puede pedir conocer el monto total de sus gastos (gastos sumados
		// de cada categoría)
		System.out.println("Desea conocer el monto total de sus gastos? [S]i / [N]o");
		opcion = scanner.next();

		if (opcion.equalsIgnoreCase("s")) {

			for (int i = 0; i < gastosPorCategoria.length; i++) {

				gastosTotales += gastosPorCategoria[i];

			}

			System.out.println("Sus gastos totales ascienden a: $" + gastosTotales);

		}

		// si el usuario gasta lo mismo que le ingresa: mostrar advertencia de que
		// debería reducir los gastos de la categoría donde más estpa gastando.

		if (ingresosMensuales == gastosTotales) {

			System.out.println(
					"Está al límite, debería reducir los gastos de la categoría donde más está gastando, que es: "
							+ categorias[catMayorGasto]);

			// Si el usuario gasta menos de lo que le ingresa: cartel felicitando
		} else if (ingresosMensuales > gastosTotales) {

			System.out.println("Felicitaciones, sus cuentas están en orden...");

			// Si el usuario gasta más de lo que le ingresa: cartel recomendando que mejore
			// sus finanzas.

		} else {

			System.out.println(
					"Le recomendamos tomar algun curso de finanzas personales, porque sino va a vivir dentro de poco, debajo de un puente");

		}

	}

}
