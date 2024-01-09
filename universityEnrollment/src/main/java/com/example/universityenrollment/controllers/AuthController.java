package com.example.universityenrollment.controllers;


import com.example.universityenrollment.dao.UsuarioDao;
import com.example.universityenrollment.models.Usuario;
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
    private static UsuarioDao usuarioDao;

    public static int intentosInicioSesion = 0;

    @RequestMapping(value = "api/login",method = RequestMethod.POST)
    public static String iniciarSesion(String usuario,String pass) {

       Usuario user = usuarioDao.obtenerUsuarioXCredenciales(usuario);
       if(user != null) {

           if(!Objects.equals(user.getStatus(), "blocked") && (Objects.equals(pass, user.getPassword()))){

               return "Usuario logueado";
           } else {
               intentosInicioSesion ++;
               return "Usuario bloqueado";

           }

       }

           return "Fail";

    }

    @RequestMapping(value = "api/blockUser",method = RequestMethod.POST)
    public String blockUser(@RequestBody Usuario usuario) {

        if(usuarioDao.blockUser(usuario.getUsuario())) {

        return "ok";
        }

        return "Fail";

    }
}
