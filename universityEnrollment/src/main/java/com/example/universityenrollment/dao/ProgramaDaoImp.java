package com.example.universityenrollment.dao;


import com.example.universityenrollment.models.Campus;
import com.example.universityenrollment.models.Programa;
import com.example.universityenrollment.models.User_Programa;
import com.example.universityenrollment.models.Usuario;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Objects;

@Repository
@Transactional
public class ProgramaDaoImp implements ProgramaDao {

    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public boolean consultarDisponibilidadPrograma(Programa nombrePrograma) {

        String query = "FROM Programa WHERE nombre=:nombreP";
        List<Programa> lista = entityManager.createQuery(query)
                .setParameter("nombreP",nombrePrograma)
                .getResultList();

      if(!lista.isEmpty() && Integer.parseInt(lista.get(0).getCupoDisponible())!=0) {
          return true;
      }

        return false;
    }

    @Override
    public boolean consultarDisponibilidadCampus(Campus nombreCampus) {

        String query = "FROM Campus WHERE name=:nombreC";
        List<Programa> lista = entityManager.createQuery(query)
                .setParameter("nombreC",nombreCampus)
                .getResultList();

        if(!lista.isEmpty() && Integer.parseInt(lista.get(0).getCupoDisponible())!= 0) {
            return true;
        }

        return false;
    }

    @Override
    public String aplicarAPrograma(Programa nombrePrograma, Campus nombreCampus, Usuario usuario) {
      String mensaje = "";

        if (this.consultarDisponibilidadPrograma(nombrePrograma)) {

         if (this.consultarDisponibilidadCampus(nombreCampus)) {
             User_Programa nuevoRegistro = new User_Programa();
             nuevoRegistro.setPrograma_id(nombrePrograma);
             nuevoRegistro.setCampus_id(nombreCampus);
             entityManager.merge(nuevoRegistro);

             mensaje = "La aplicacion se completo exitosamente";
         }
          else {
             mensaje = "El campus seleccionado ya no tiene cupos disponibles para registrarse";
         }

       } else {
            mensaje = "El programa seleccionado ya no tiene cupos disponibles para registrarse";
        }

        return mensaje;
    }


    @Override
    public Programa obtenerProgramaXNombre(String n) {

        String query = "FROM Programa WHERE nombre=:nombreP";
        List<Programa> lista = entityManager.createQuery(query)
                .setParameter("nombreP",n)
                .getResultList();

        if(lista.isEmpty()) {
            return null;
        }
        else {
            return lista.get(0);
        }
    }

    @Override
    public Campus obtenerCampusXNombre(String n) {
        String query = "FROM Programa WHERE nombre=:nombreP";
        List<Campus> lista = entityManager.createQuery(query)
                .setParameter("nombreP",n)
                .getResultList();

        if(lista.isEmpty()) {
            return null;
        }
        else {
            return lista.get(0);
        }
    }
}
