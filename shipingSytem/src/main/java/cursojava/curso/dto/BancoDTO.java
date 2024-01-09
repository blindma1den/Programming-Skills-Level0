package cursojava.curso.dto;

import lombok.Getter;
import lombok.Setter;

public class BancoDTO {
    @Getter @Setter
    private String monto;

    @Getter @Setter
    private String email;

    @Getter @Setter
    private String emailUsuarioDestino;

    public BancoDTO(String monto, String email, String emailUsuarioDestino) {
        this.monto = monto;
        this.email = email;
        this.emailUsuarioDestino = emailUsuarioDestino;
    }
}
