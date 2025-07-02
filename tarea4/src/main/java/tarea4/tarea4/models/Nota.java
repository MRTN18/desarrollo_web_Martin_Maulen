package tarea4.tarea4.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;

@Entity
@Table
public class Nota {
    @Id
    @SequenceGenerator(
        name = "nota_sequence",
        sequenceName = "nota_sequence",
        allocationSize = 1
    )
    @GeneratedValue(
        strategy = GenerationType.SEQUENCE,
        generator = "nota_sequence"
    )
    private Long id;

    @NotNull
    @Column(name = "actividad_id")
    private long actividad_id;

    @NotNull
    private String nota;

    public Nota() {
    }
    
    public Nota(Long id, long actividad_id, String nota) {
        this.id = id;
        this.actividad_id = actividad_id;
        this.nota = nota;
    }

    public Long getId() {
        return id;
    }
    public long getActividad_id() {
        return actividad_id;
    }
    public String getNota() {
        return nota;
    }
}
