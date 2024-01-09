package com.example.universityenrollment.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Table(name="campus")
@Entity
@ToString
public class Campus {

    @Id
    @Getter
    @Setter
    @Column(name = "id")
    public Long id;

    @Getter
    @Setter
    @Column(name = "name")
    public String name;

    @Getter
    @Setter
    @Column(name = "cupoDisponible")
    public String cupoDisponible;
}
