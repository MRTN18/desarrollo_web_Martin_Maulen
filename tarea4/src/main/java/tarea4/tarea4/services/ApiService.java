package tarea4.tarea4.services;

import java.util.List;
import org.springframework.stereotype.Service;
import tarea4.tarea4.models.Actividad;
import tarea4.tarea4.models.ActividadRepository;
import tarea4.tarea4.models.ActividadTema;
import tarea4.tarea4.models.ActividadTemaRepository;

@Service
public class ApiService {
    private final ActividadRepository actividadRepository;
    private final ActividadTemaRepository actividadTemaRepository;

    public ApiService(ActividadRepository actividadRepository, ActividadTemaRepository actividadTemaRepository) {
        this.actividadRepository = actividadRepository;
        this.actividadTemaRepository = actividadTemaRepository;
    }

    public List<Actividad> getActividades() {
        List<Actividad> actividades = actividadRepository.findAll();
        return actividades;
    }

    public List<ActividadTema> getActividadesTemas() {
        List<ActividadTema> actividadesTemas = actividadTemaRepository.findAll();
        return actividadesTemas;
    }
}
