package com.example.universityenrollment.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Table(name="usuarios")
@Entity
@ToString
public class Usuario {

    @Getter
    @Setter
    @Column(name = "usuario")
    public String usuario;

    @Getter
    @Setter
    @Column(name = "password")
    public String password;

    @Getter
    @Setter
    @Column(name = "status")
    public String status;

    @Id
    @Getter
    @Setter
    @Column(name = "id")
    private Long id;

}
