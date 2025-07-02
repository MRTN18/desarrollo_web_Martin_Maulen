package tarea4.tarea4.services;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import tarea4.tarea4.models.Actividad;
import tarea4.tarea4.models.ActividadRepository;
import tarea4.tarea4.models.ActividadTema;
import tarea4.tarea4.models.ActividadTemaRepository;
import tarea4.tarea4.models.Nota;
import tarea4.tarea4.models.NotaRepository;

@Service
public class AppService {
    private String pathStatic;
    private final ActividadRepository actividadRepository;
    private final ActividadTemaRepository actividadTemaRepository;
    private final NotaRepository notaRepository;

    public AppService(ActividadRepository actividadRepository, ActividadTemaRepository actividadTemaRepository, 
                      NotaRepository notaRepository) {
        this.notaRepository = notaRepository;
        this.actividadRepository = actividadRepository;
        this.actividadTemaRepository = actividadTemaRepository;
        // Dynamically resolve the absolute path for the static directory
        this.pathStatic = "classpath:static";
        System.out.println("Static path resolved to: " + this.pathStatic);
    }

    public List<Map<String, String>> getActividadesData(Integer pageSize) {
        List<Actividad> actividades = actividadRepository.findAllByOrderByIdDesc(PageRequest.of(0, pageSize)).getContent();
        List<Map<String, String>> actividadesData = new ArrayList<>();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        for (Actividad act : actividades) {
            ActividadTema tema = actividadTemaRepository.findByActividadId(act.getId());
            Map<String, String> actData = new HashMap<>();
            actData.put("id", act.getId().toString());
            actData.put("nombre", act.getNombre());
            actData.put("email", act.getEmail());
            actData.put("comuna_id", String.valueOf(act.getComuna_id()));

            LocalDateTime fechaInicio = act.getDia_hora_inicio();
            String formattedFechaInicio = (fechaInicio != null) ? fechaInicio.format(formatter) : "";
            actData.put("fecha_inicio", formattedFechaInicio);

            LocalDateTime fechaTermino = act.getDia_hora_termino();
            String formattedFechaTermino = (fechaTermino != null) ? fechaTermino.format(formatter) : "";
            actData.put("fecha_termino", formattedFechaTermino);

            actData.put("celular", act.getCelular() != null ? act.getCelular() : "");
            actData.put("descripcion", act.getDescripcion() != null ? act.getDescripcion() : "");
            actData.put("sector", act.getSector() != "" ? act.getSector() : "--");
            actData.put("tema", tema.getGlosa_otro() == null ? tema.getTema() : tema.getGlosa_otro());
            actividadesData.add(actData);
        }
        return actividadesData;
    }

    public void handlePostNota(Integer nota, Long actividad_id) throws Exception {
        if (nota < 1 || nota > 7) {
            throw new IllegalArgumentException("La nota debe estar entre 1 y 7");
        }

        Nota nuevaNota = new Nota(
            actividad_id, 
            nota);
        
        notaRepository.save(nuevaNota);
    }
}
