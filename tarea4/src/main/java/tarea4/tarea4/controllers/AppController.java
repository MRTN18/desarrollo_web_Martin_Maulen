package tarea4.tarea4.controllers;

import java.util.List;
import java.util.Map;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import tarea4.tarea4.services.AppService;

@Controller
public class AppController {
    private final AppService appService;
    public AppController(AppService appService) {
        this.appService = appService;
    }

    @GetMapping("/")
    public String indexRoute(Model model) {
        List<Map<String, String>> modelData = appService.getActividadesData(10);
        model.addAttribute("data", modelData);
        return "index";
    }

    @PostMapping("/post-nota")
    public String indexPostRoute(
        @RequestParam("nota") Integer nota,
        @RequestParam("actividad_id") Long actividad_id) throws Exception {

        appService.handlePostNota(nota, actividad_id);
        return "redirect:/";
    }
}
