package cursojava.curso.dao;

import cursojava.curso.models.Usuario;

public interface BancoDao {

    String  verSaldo(Usuario usuario);

    public void depositar(String monto, Usuario usuario);

    public String extraer(String monto, Usuario usuario);

    public String transferir(Usuario usuario,Usuario usuarioDestino, String monto);

}
