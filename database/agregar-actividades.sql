-- Active: 1746137026576@@127.0.0.1@3306@tarea2
INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion)
VALUES (20304, '', 'Taller de Pintura', 'taller.pintura@example.com', '', '2023-11-01 10:00:00', '2023-11-01 12:00:00', 'Un taller para aprender técnicas básicas de pintura.');
INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion)
VALUES (20101, '', 'Clase de Yoga', 'clase.yoga@example.com', '', '2023-11-02 08:00:00', '2023-11-02 09:30:00', 'Sesión de yoga para principiantes y avanzados.');
INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion)
VALUES (20102, '', 'Charla de Tecnología', 'charla.tecnologia@example.com', '', '2023-11-03 15:00:00', '2023-11-03 17:00:00', 'Charla sobre las últimas tendencias en tecnología.');
INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion)
VALUES (40102, '', 'Taller de Cocina', 'taller.cocina@example.com', '', '2023-11-04 11:00:00', '2023-11-04 13:00:00', 'Aprende a preparar recetas saludables y deliciosas.');
INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion)
VALUES (50201, '', 'Concierto de Música', 'concierto.musica@example.com', '', '2023-11-05 19:00:00', '2023-11-05 21:00:00', 'Concierto de música en vivo con artistas locales.');

INSERT INTO actividad_tema (tema, glosa_otro, actividad_id) VALUES ('otro', 'arte', 4); 
INSERT INTO actividad_tema (tema, glosa_otro, actividad_id) VALUES ('deporte', NULL, 5);
INSERT INTO actividad_tema (tema, glosa_otro, actividad_id) VALUES ('tecnología', NULL, 6);
INSERT INTO actividad_tema (tema, glosa_otro, actividad_id) VALUES ('comida', NULL, 7);
INSERT INTO actividad_tema (tema, glosa_otro, actividad_id) VALUES ('musica', NULL, 8);

INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) VALUES ('/image/index-foto1.jpg', 'index-foto1', 4);
INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) VALUES ('/image/index-foto2.jpg', 'index-foto2', 5);
INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) VALUES ('/image/index-foto3.jpg', 'index-foto3', 6);
INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) VALUES ('/image/index-foto4.jpg', 'index-foto4', 7);
INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) VALUES ('/image/index-foto5.jpg', 'index-foto5', 8);