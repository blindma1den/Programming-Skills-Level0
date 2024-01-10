package com.example.universityenrollment.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Entity
@Getter
@Table(name="programa")
@ToString
public class Programa {

    @Id
    @Getter @Setter
    @Column(name = "id")
    private Long id;

    @Getter @Setter
    @Column(name = "nombre")
    private String nombre;

    @Getter @Setter
    @Column(name = "cupoDisponible")
    public String cupoDisponible;


}
