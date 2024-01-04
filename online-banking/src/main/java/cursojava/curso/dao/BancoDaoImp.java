package cursojava.curso.dao;

import cursojava.curso.models.Banco;
import cursojava.curso.models.Usuario;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Objects;

@Repository
@Transactional
public class BancoDaoImp implements BancoDao {

    @PersistenceContext
    private EntityManager entityManager;
    @Override
    public String verSaldo(Usuario usuario) {
        String query = "FROM Banco WHERE user_id=:id";
        List<Banco> lista = entityManager.createQuery(query)
                .setParameter("id",usuario)
                .getResultList();

        return lista.get(0).getSaldo();
    }

    @Override
    public void depositar(String monto, Usuario usuario) {

        String query = "FROM Banco WHERE user_id=:id";
        List<Banco> lista = entityManager.createQuery(query)
                .setParameter("id",usuario)
                .getResultList();

        int saldoNuevo = Integer.parseInt(lista.get(0).getSaldo()) + Integer.parseInt(monto);
        lista.get(0).setSaldo(String.valueOf(saldoNuevo));

    }

    @Override
    public String extraer(String monto, Usuario usuario) {
        String query = "FROM Banco WHERE user_id=:id";
        List<Banco> lista = entityManager.createQuery(query)
                .setParameter("id",usuario)
                .getResultList();


        if(Integer.parseInt(lista.get(0).getSaldo()) != 0) {
            int saldoNuevo = Integer.parseInt(lista.get(0).getSaldo()) - Integer.parseInt(monto);

            lista.get(0).setSaldo(String.valueOf(saldoNuevo));

            return "ok";
        }
        return "fail";
    }

    @Override
    public String transferir(Usuario usuario,Usuario usuarioDestino, String monto) {

       String estadoOperacion = this.extraer(monto,usuario);

       if (Objects.equals(estadoOperacion, "ok")) {
           this.depositar(monto,usuarioDestino);
           return "ok";
       }
        return "fail";
    }
}
