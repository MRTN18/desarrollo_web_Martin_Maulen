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
public class ActividadTema {
    @Id
    @SequenceGenerator(
        name = "actividadTema_sequence",
        sequenceName = "actividadTema_sequence",
        allocationSize = 1
    )
    @GeneratedValue(
        strategy = GenerationType.SEQUENCE,
        generator = "actividadTema_sequence"
    )
    private Long id;

    @NotNull
    private String tema;

    @NotNull
    @Column(name = "actividad_id")
    private long actividad_id;

    private String glosa_otro;

    public ActividadTema() {
    }
    
    public ActividadTema(Long id, String tema, long actividad_id, String glosa_otro) {
        this.id = id;
        this.tema = tema;
        this.actividad_id = actividad_id;
        this.glosa_otro = glosa_otro;
    }

    public Long getId() {
        return id;
    }
    public String getTema() {
        return tema;
    }
    public long getActividad_id() {
        return actividad_id;
    }
    public String getGlosa_otro() {
        return glosa_otro;
    }
}
