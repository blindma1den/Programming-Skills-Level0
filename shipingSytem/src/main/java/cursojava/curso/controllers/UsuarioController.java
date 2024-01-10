package cursojava.curso.controllers;

import cursojava.curso.models.Usuario;
import cursojava.curso.dao.UsuarioDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class UsuarioController {

    @Autowired
    private UsuarioDao usuarioDao;



    @RequestMapping(value = "usuario/{id}")
    public Usuario getUsuario(@PathVariable long id) {
        Usuario user = new Usuario();
        user.setId(id);
        user.setNombre("Thais");
        user.setApellido("Thais");
        user.setEmail("alonsothais@gmail.com");
        user.setTelefono("50578750549");

      return user;
    }

    @RequestMapping(value = "api/usuarios")
    public List<Usuario> getUsuarios(@RequestHeader(value="Authorization") String token) {


     return usuarioDao.getUsuarios();
    }



    @RequestMapping(value = "api/usuarios",method = RequestMethod.POST)
    public String registrarUsuario(@RequestBody Usuario usuario) {
        usuario.setPassword(usuario.getPassword());

       return usuarioDao.registrar(usuario);
    }


    @RequestMapping(value = "api/usuario/edit")
    public Usuario editar() {
        Usuario user = new Usuario();
        user.setNombre("Thais");
        user.setApellido("Thais");
        user.setEmail("alonsothais@gmail.com");
        user.setTelefono("50578750549");

        return user;
    }

    @RequestMapping(value = "api/usuario/delete/{id}",method = RequestMethod.DELETE)
    public void eliminar(@PathVariable Long id,@RequestHeader(value="Authorization") String token) {
        usuarioDao.eliminar(id);
    }

    @RequestMapping(value = "api/usuario/search")
    public Usuario buscar(@RequestHeader(value="Authorization") String token) {

        Usuario user = new Usuario();
        user.setNombre("Thais");
        user.setApellido("Thais");
        user.setEmail("alonsothais@gmail.com");
        user.setTelefono("50578750549");
        user.setStatus("active");

        return user;
    }


}
