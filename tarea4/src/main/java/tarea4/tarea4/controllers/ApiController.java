package tarea4.tarea4.controllers;

import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import tarea4.tarea4.models.Actividad;
import tarea4.tarea4.models.ActividadTema;
import tarea4.tarea4.services.ApiService;

@RestController
public class ApiController {
    private final ApiService apiService;
    public ApiController(ApiService apiService) {
        this.apiService = apiService;
    }

    @GetMapping("/get-act")
    public Map<String, List<Actividad>> getActividadEndpoint() {
        List<Actividad> actividades = apiService.getActividades();
        return Map.of("data", actividades);
    }

    @GetMapping("/get-act-tema")
    public Map<String, List<ActividadTema>> getActividadTemaEndpoint() {
        List<ActividadTema> actividadesTemas = apiService.getActividadesTemas();
        return Map.of("data", actividadesTemas);
    }
}
