package com.example.universityenrollment.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Table(name="campus")
@Entity
@ToString
public class User_Programa {

    @Id
    @Getter @Setter
    @Column(name = "id")
    private Long id;

    @Getter
    @Setter
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    private Usuario user_id;

    @Getter @Setter
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "campus_id", referencedColumnName = "id")
    private Campus campus_id;

    @Getter @Setter
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "programa_id", referencedColumnName = "id")
    private Programa programa_id;
}
