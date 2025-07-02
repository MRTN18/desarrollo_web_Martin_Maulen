package tarea4.tarea4.models;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface NotaRepository extends JpaRepository<Nota, Long> {
    Page<Nota> findAllByOrderByIdDesc(Pageable pageable);

    @Query("SELECT a FROM Nota a WHERE a.actividad_id = :actividad_id")
    Nota findByActividadId(@Param("actividad_id") Long actividad_id);
}
