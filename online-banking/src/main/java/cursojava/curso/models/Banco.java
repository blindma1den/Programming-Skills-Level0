package cursojava.curso.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Entity
@Getter
@Table(name="banco")
@ToString
public class Banco {

    @Id
    @Getter @Setter
    @Column(name = "id")
    private Long id;

    @Getter @Setter
    @Column(name = "saldo")
    private String saldo;

    @Getter @Setter
    @Column(name = "transferenciasRealizadas")
    private String transferenciasRealizadas;

    @Getter @Setter
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    private Usuario user_id;
}
