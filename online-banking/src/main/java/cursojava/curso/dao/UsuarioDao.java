package cursojava.curso.dao;

import cursojava.curso.models.Usuario;

import java.util.List;

public interface UsuarioDao {

    List<Usuario> getUsuarios();

    void eliminar(Long id);

   String registrar(Usuario usuario);

   Usuario obtenerUsuarioXCredenciales(Usuario usuario);

   Usuario obtenerUsuarioXEmail(Usuario usuario);

    Usuario obtenerUsuario(String email);

   boolean blockUser(Usuario usuario);

}
