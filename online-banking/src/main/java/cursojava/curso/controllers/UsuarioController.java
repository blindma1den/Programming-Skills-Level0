package cursojava.curso.controllers;

import cursojava.curso.models.Usuario;
import cursojava.curso.dao.UsuarioDao;
import cursojava.curso.utils.JWTUtil;
import de.mkammerer.argon2.Argon2;
import de.mkammerer.argon2.Argon2Factory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@RestController
public class UsuarioController {

    @Autowired
    private UsuarioDao usuarioDao;

    @Autowired
    private JWTUtil jwtUtil;

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

    if(!validarToken(token)){
        return null;
    }

     return usuarioDao.getUsuarios();
    }

    private boolean validarToken(String token){
        String usuarioID = jwtUtil.getKey(token);

        return usuarioID != null;
    }

    @RequestMapping(value = "api/usuarios",method = RequestMethod.POST)
    public String registrarUsuario(@RequestBody Usuario usuario) {

        Argon2 argon2 = Argon2Factory.create(Argon2Factory.Argon2Types.ARGON2id);
        String hash =  argon2.hash(1,1024,1,usuario.getPassword());
        usuario.setPassword(hash);

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
        if(!validarToken(token)){
            return ;
        }
        usuarioDao.eliminar(id);
    }

    @RequestMapping(value = "api/usuario/search")
    public Usuario buscar(@RequestHeader(value="Authorization") String token) {

        if(!validarToken(token)){
            return null;
        }

        Usuario user = new Usuario();
        user.setNombre("Thais");
        user.setApellido("Thais");
        user.setEmail("alonsothais@gmail.com");
        user.setTelefono("50578750549");
        user.setStatus("active");

        return user;
    }


}
