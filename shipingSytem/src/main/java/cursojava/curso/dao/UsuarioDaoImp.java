package cursojava.curso.dao;

import cursojava.curso.models.Banco;
import cursojava.curso.models.Usuario;
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

        String query = "FROM Usuario WHERE email=:email";
        List<Usuario> lista = entityManager.createQuery(query)
                .setParameter("email",usuario.getEmail())
                .getResultList();
        usuario.setStatus("active");

        if(!lista.isEmpty()) {
            return "email duplicado";
        }

        entityManager.merge(usuario); //no pone el id de la entidad automaticamente

        //registra saldo inicial y asocia usuario
        Banco mibanco = new Banco();
        mibanco.setId(0L);
        mibanco.setSaldo(String.valueOf(2000));
        mibanco.setTransferenciasRealizadas(String.valueOf(0));
        mibanco.setUser_id(usuario);
        entityManager.merge(mibanco); //no pone el id de la entidad automaticamente

        return "ok";
    }

    public boolean blockUser(Usuario user) {

       Usuario usuario = obtenerUsuarioXEmail(user);
        if (usuario !=null) {
            usuario.setStatus("blocked");

            return true;
        }
        return false;
    }

    @Override
    public Usuario obtenerUsuarioXCredenciales(Usuario usuario) {

        String query = "FROM Usuario WHERE email=:email";
            List<Usuario> lista = entityManager.createQuery(query)
                .setParameter("email",usuario.getEmail())
                .getResultList();

            if(lista.isEmpty()) {
                return null;
            }

//          if(usuario.getPassword() === usuario.getPassword()){
//              return lista.get(0);
//          }
         return  null;

    }

    @Override
    public Usuario obtenerUsuarioXEmail(Usuario usuario) {
        String query = "FROM Usuario WHERE email=:email";
        List<Usuario> lista = entityManager.createQuery(query)
                .setParameter("email",usuario.getEmail())
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
