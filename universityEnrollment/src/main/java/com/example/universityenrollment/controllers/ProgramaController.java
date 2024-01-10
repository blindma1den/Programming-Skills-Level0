package com.example.universityenrollment.controllers;

import com.example.universityenrollment.dao.ProgramaDao;
import com.example.universityenrollment.dao.UsuarioDao;
import com.example.universityenrollment.models.Campus;
import com.example.universityenrollment.models.Programa;
import com.example.universityenrollment.models.User_Programa;
import com.example.universityenrollment.models.Usuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class ProgramaController {

    @Autowired
    private static UsuarioDao usuarioDao;

    @Autowired
    private static ProgramaDao programaDao;


    @RequestMapping(value = "api/deposit",method = RequestMethod.POST)
    public static String registrarPrograma(String name,String apellidos,String programa,String campus){

        Usuario user = usuarioDao.obtenerUsuarioXNombre(name);
        Programa p = programaDao.obtenerProgramaXNombre(programa);
        Campus c = programaDao.obtenerCampusXNombre(campus);

        return programaDao.aplicarAPrograma(p,c,user);

     //   Usuario user = usuarioDao.obtenerUsuario(datos.getEmail());
      //  bancoDao.depositar(datos.getMonto(),user);

    }
//
//
//    @RequestMapping(value = "api/withdraw",method = RequestMethod.POST)
//    public String extraer(@RequestBody BancoDTO datos){
//        Usuario user = usuarioDao.obtenerUsuario(datos.getEmail());
//        return bancoDao.extraer(datos.getMonto(),user);
//    }
//
//    @RequestMapping(value = "api/view",method = RequestMethod.GET)
//    public String verSaldo(@RequestParam String email){
//        Usuario user = usuarioDao.obtenerUsuario(email);
//        return String.valueOf(bancoDao.verSaldo(user));
//    }
//
//    @RequestMapping(value = "api/transfer",method = RequestMethod.POST)
//    public String transferir(@RequestBody BancoDTO datos){
//
//      Usuario user = usuarioDao.obtenerUsuario(datos.getEmail());
//      Usuario userDestino = usuarioDao.obtenerUsuario(datos.getEmailUsuarioDestino());
//
//      return bancoDao.transferir(user,userDestino, datos.getMonto());
//
//    }


}
