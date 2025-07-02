package tarea4.tarea4.models;

import java.time.LocalDateTime;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;

@Entity
@Table
public class Actividad {

    @Id
    @SequenceGenerator(
        name = "actividad_sequence",
        sequenceName = "actividad_sequence",
        allocationSize = 1
    )
    @GeneratedValue(
        strategy = GenerationType.SEQUENCE,
        generator = "actividad_sequence"
    )
    private Long id;

    @NotNull
    private String nombre;

    @NotNull
    private String email;

    @NotNull
    private long comuna_id;

    @NotNull
    private LocalDateTime dia_hora_inicio;

    private LocalDateTime dia_hora_termino;

    private String celular;

    private String descripcion;

    private String sector;

    public Actividad() {
    }

    public Actividad(Long id, String nombre, String tema, LocalDateTime fecha_inicio, String sector) {
        this.id = id;
        this.nombre = nombre;
        this.dia_hora_inicio = fecha_inicio;
        this.sector = sector;
    }

    public Long getId() {
        return id;
    }
    public String getNombre() {
        return nombre;
    }
    public String getEmail() {
        return email;
    }
    public long getComuna_id() {
        return comuna_id;
    }
    public LocalDateTime getDia_hora_inicio() {
        return dia_hora_inicio;
    }
    public LocalDateTime getDia_hora_termino() {
        return dia_hora_termino;
    }
    public String getCelular() {
        return celular;
    }
    public String getDescripcion() {
        return descripcion;
    }
    public String getSector() {
        return sector;
    }
}
