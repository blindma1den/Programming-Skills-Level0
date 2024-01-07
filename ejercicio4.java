

import java.util.Random;
import java.util.Scanner;

public class Registro {
    static Scanner teclado = new Scanner(System.in);
    static Random r1 = new Random();
    static String[] categorias = { "Medicina", "Hogar", "Ocio", "Ahorros", "Educación" };
    static double[] array = new double[5];
    static double gastos;

    public static void main(String[] args) {
        if (login()) {
            realizarEnvio();
        }
    }

    public static boolean login() {
        int totalAttemps = 0;
        String username = "Pepito";
        String password = "123";

        while (totalAttemps < 3) {
            System.out.println("Ingrese su usuario");
            String user = teclado.nextLine();
            System.out.println("Ingrese su contrasenia");
            String pass = teclado.nextLine();
            if (!username.equals(user) || !password.equals(pass)) {
                System.out.println("El nombre de usuario o contraseña ingresados son incorrectos");
                totalAttemps = totalAttemps + 1;
            } else {
                System.out.println("Ha iniciado sesion correctamente!");
                return true;
            }
        }
        return false;
    }

    public static void realizarEnvio() {
        System.out.println("Ingrese nombre del destinatario:");
        String destinatario = teclado.nextLine();
        System.out.println("Ingrese nombre del remitente");
        String remitente = teclado.nextLine();
        System.out.println("Ingrese direccion del destinatario: ");
        String direccion = teclado.nextLine();
        int numPaquete = r1.nextInt(1000);
        System.out.println("Numero de envio " + numPaquete);
        System.out.println("Ingrese el peso del paquete en kg: ");
        double pesoPaquete = teclado.nextDouble();
        double pagarPeso = calcularCosto(pesoPaquete);
        System.out.println("El precio total a pagar por el envio es de " + pagarPeso);
        System.out.println("Que desea hacer?  1-Enviar paquete  2-Salir del sistema");
        int opcion = teclado.nextInt();
        manejarOpcion(opcion);
    }

    public static double calcularCosto(double pesoPaquete) {
        return pesoPaquete * 2;
    }

    public static void manejarOpcion(int opcion) {
        if (opcion == 1) {
            realizarEnvio();
        } else if (opcion == 2) {
            System.out.println("Ha salido del sistema");
        }
    }
}
