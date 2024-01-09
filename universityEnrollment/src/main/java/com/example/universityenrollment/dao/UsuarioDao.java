package com.example.universityenrollment.dao;



import com.example.universityenrollment.models.Usuario;

import java.util.List;

public interface UsuarioDao {

    List<Usuario> getUsuarios();

    void eliminar(Long id);

   String registrar(Usuario usuario);

   Usuario obtenerUsuarioXCredenciales(String usuario);

   Usuario obtenerUsuarioXNombre(String usuario);

    Usuario obtenerUsuario(String email);

   boolean blockUser(String  usuario);

}
