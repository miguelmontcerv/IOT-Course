CREATE DATABASE curso_iot;

USE curso_iot;

CREATE TABLE opiniones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alumno VARCHAR(255),
    opinion TEXT,
    calificacion INT
);

INSERT INTO opiniones (alumno, opinion, calificacion)
VALUES
    ('Juan', 'Excelente curso, muy informativo.', 10),
    ('Maria', 'Buen contenido, pero podría mejorar la presentación.', 8),
    ('Carlos', 'Me gustaría ver más ejemplos prácticos.', 6);
