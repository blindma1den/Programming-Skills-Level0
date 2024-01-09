package cursojava.curso.controllers;

import cursojava.curso.dao.UsuarioDao;
import cursojava.curso.models.Usuario;
import cursojava.curso.utils.JWTUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.Objects;

@RestController
public class AuthController {

    @Autowired
    private UsuarioDao usuarioDao;

    @Autowired
    private JWTUtil jwtUtil;

    @RequestMapping(value = "api/login",method = RequestMethod.POST)
    public String iniciarSesion(@RequestBody Usuario usuario) {

       Usuario user = usuarioDao.obtenerUsuarioXCredenciales(usuario);
       if(user != null) {

           if(!Objects.equals(user.getStatus(), "blocked")){
               String tokenJwt =  jwtUtil.create(String.valueOf(user.getId()),user.getEmail());

               return tokenJwt;
           } else {
               return "Usuario bloqueado";
           }

       }

           return "Fail";

    }

    @RequestMapping(value = "api/blockUser",method = RequestMethod.POST)
    public String blockUser(@RequestBody Usuario usuario) {

        if(usuarioDao.blockUser(usuario)) {

        return "ok";
        }

        return "Fail";

    }
}
