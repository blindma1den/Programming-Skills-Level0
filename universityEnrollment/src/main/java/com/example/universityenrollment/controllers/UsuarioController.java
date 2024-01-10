package com.example.universityenrollment.controllers;


import com.example.universityenrollment.dao.UsuarioDao;
import com.example.universityenrollment.models.Usuario;
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


    @RequestMapping(value = "api/usuarios")
    public List<Usuario> getUsuarios(@RequestHeader(value="Authorization") String token) {

     return usuarioDao.getUsuarios();
    }


    @RequestMapping(value = "api/usuarios",method = RequestMethod.POST)
    public String registrarUsuario(@RequestBody Usuario usuario) {

        usuario.setPassword(usuario.getPassword());

       return usuarioDao.registrar(usuario);
    }


    @RequestMapping(value = "api/usuario/delete/{id}",method = RequestMethod.DELETE)
    public void eliminar(@PathVariable Long id,@RequestHeader(value="Authorization") String token) {

        usuarioDao.eliminar(id);
    }

}
