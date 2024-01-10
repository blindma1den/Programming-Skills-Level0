package com.example.universityenrollment.dao;


import com.example.universityenrollment.models.Usuario;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Repository
@Transactional
public class UsuarioDaoImp implements UsuarioDao{

   @PersistenceContext
    private EntityManager entityManager;

    @Override
    public List<Usuario> getUsuarios() {
        String query = "FROM Usuario";
        return entityManager.createQuery(query).getResultList();
    }

    @Override
    public void eliminar(Long id) {
        Usuario usuario = entityManager.find(Usuario.class,id);
        entityManager.remove(usuario);
    }

    @Override
    public String registrar(Usuario usuario) {

        String query = "FROM Usuario WHERE usuario=:usuario";
        List<Usuario> lista = entityManager.createQuery(query)
                .setParameter("usuario",usuario.getUsuario())
                .getResultList();
        usuario.setStatus("active");

        if(!lista.isEmpty()) {
            return "email duplicado";
        }

        entityManager.merge(usuario); //no pone el id de la entidad automaticamente

//        //registra saldo inicial y asocia usuario
//        Banco mibanco = new Banco();
//        mibanco.setId(0L);
//        mibanco.setSaldo(String.valueOf(2000));
//        mibanco.setTransferenciasRealizadas(String.valueOf(0));
//        mibanco.setUser_id(usuario);
//        entityManager.merge(mibanco); //no pone el id de la entidad automaticamente

        return "ok";
    }

    @Override
    public Usuario obtenerUsuarioXCredenciales(String usuario) {
        String query = "FROM Usuario WHERE usuario=:nombre";
        List<Usuario> lista = entityManager.createQuery(query)
                .setParameter("nombre",usuario)
                .getResultList();

        if(lista.isEmpty()) {
            return null;
        } else {
            return lista.get(0);
        }
    }

    public boolean blockUser(String user) {

       Usuario usuario = obtenerUsuarioXNombre(user);
        if (usuario !=null) {
            usuario.setStatus("blocked");

            return true;
        }
        return false;
    }

    @Override
    public Usuario obtenerUsuarioXNombre(String usuario) {
        String query = "FROM Usuario WHERE usuario=:nombre";
        List<Usuario> lista = entityManager.createQuery(query)
                .setParameter("nombre",usuario)
                .getResultList();

        if(lista.isEmpty()) {
            return null;
        } else {
            return lista.get(0);
        }
    }

    @Override
    public Usuario obtenerUsuario(String email) {
        String query = "FROM Usuario WHERE email=:email";
        List<Usuario> lista = entityManager.createQuery(query)
                .setParameter("email",email)
                .getResultList();

        if(lista.isEmpty()) {
            return null;
        } else {
            return lista.get(0);
        }
    }
}
