# 5.1 En una consulta, obtener todos los cursos.
# 5.2 Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso (con otra consulta), y presentar el promedio de calificaciones de las entregas

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from clases import *

# crear una sesion
Session = sessionmaker(bind=engine)
session = Session()

# 5.1 Consultar todos los cursos disponibles en la base de datos
promedio = session.query(Curso).all()

# 5.2 Para cada curso, obtener sus entregas, calcular el promedio de calificaciones y mostrarlo
for curso in promedio:
    # Se realiza una consulta de las entregas relacionadas al curso actual, utilizando join con la tabla Tarea
    entregas = session.query(Entrega).join(Tarea).filter(Tarea.curso_id == curso.id).all()

    if entregas:
        # Se calcula el promedio de calificaciones de las entregas
        promedio = sum(e.calificacion for e in entregas) / len(entregas)

        # Mostrar el curso y el promedio de calificaciones
        print(f"nombre del curso: {curso.titulo} -> Promedio: {promedio}")