# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, 
# nombre de instructor y nombre del departamento

from sqlalchemy.orm import sessionmaker
#from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega
from clases import *

Session = sessionmaker(bind=engine)
session = Session()

entregas_arte = (
    session.query(Entrega)
    .join(Entrega.tarea)
    .join(Tarea.curso)
    .join(Curso.departamento)
    .filter(Departamento.nombre == 'Arte').all()
)

print("Entregas de los estudiantes en el Departamento de Arte")

for entrega in entregas_arte:
	print("-------------------------------------------")
	print(f"Nombre de la tarea: {entrega.tarea.titulo}")
	print(f"Nombre del estudiante: {entrega.estudiante.nombre}")
	print(f"Calificacion: {entrega.calificacion}")
	print(f"Nombre del Instructor: {entrega.tarea.curso.instructor.nombre}")
	print(f"Nombre del Departamento: {entrega.tarea.curso.departamento.nombre}")
	print("-------------------------------------------")
