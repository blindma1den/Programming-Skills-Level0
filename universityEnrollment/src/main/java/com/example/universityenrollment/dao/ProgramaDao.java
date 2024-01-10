package com.example.universityenrollment.dao;


import com.example.universityenrollment.models.Campus;
import com.example.universityenrollment.models.Programa;
import com.example.universityenrollment.models.Usuario;

public interface ProgramaDao {

    boolean  consultarDisponibilidadPrograma(Programa nombrePrograma);

    boolean  consultarDisponibilidadCampus(Campus nombreCampus);

//    public String seleccionarCampus(Campus nombreCampus, Usuario usuario);
//
//    public String seleccionarPrograma(Programa nombrePrograma, Usuario usuario);

    public String aplicarAPrograma(Programa nombrePrograma,Campus nombreCampus, Usuario usuario);

    public Programa obtenerProgramaXNombre(String n);

    public Campus obtenerCampusXNombre(String n);
}
