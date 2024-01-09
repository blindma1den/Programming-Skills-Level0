package com.example.universityenrollment;

import com.example.universityenrollment.controllers.AuthController;
import com.example.universityenrollment.controllers.ProgramaController;
import com.example.universityenrollment.models.Usuario;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.ArrayList;
import java.util.Scanner;

@SpringBootApplication
public class UniversityEnrollmentApplication {

    public static String main(String[] args) {

        var usuario = new ArrayList<Usuario>();


        System.out.print("Usuario: ");
        Scanner consola = new Scanner(System.in);
        var user = consola.nextLine();
        System.out.print("Contrasenna: ");
        var pass = consola.nextLine();

        System.out.println(AuthController.iniciarSesion(user,pass));

        if(AuthController.intentosInicioSesion == 3){
            System.out.println("Su usuario ha sido bloqueado por poner la contrasenna mal 3 veces");
            return user;
        }

        System.out.println("Bienvenido: "+user);
        System.out.println("Programas disponibles: Computer Science, Medicine, Marketing, and Arts.");
        System.out.println("Por favor rellene los datos que se piden a continuacion:");
        System.out.println("Nombre:");
        var name = consola.nextLine();
        System.out.println("Apellidos:");
        var apellidos = consola.nextLine();
        System.out.println("Programa: ");
        var programa = consola.nextLine();
        System.out.println("Campus: ");
        var campus = consola.nextLine();

        return ProgramaController.registrarPrograma(name,apellidos,programa,campus);

    }

}
