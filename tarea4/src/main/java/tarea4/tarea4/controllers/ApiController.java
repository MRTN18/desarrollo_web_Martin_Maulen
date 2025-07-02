package tarea4.tarea4.controllers;

import java.util.List;
import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import tarea4.tarea4.models.Nota;
import tarea4.tarea4.services.ApiService;

@RestController
public class ApiController {
    private final ApiService apiService;
    public ApiController(ApiService apiService) {
        this.apiService = apiService;
    }

    @GetMapping("/get-notas/{title_substring}")
    public Map<String, List<Nota>> getNotasEndpoint(@PathVariable("title_substring") String titleSubstring) {
        List<Nota> notas = apiService.getNotas(Long.parseLong(titleSubstring));
        return Map.of("data", notas);
    }
}
