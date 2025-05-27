#2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 . 
# En función de los departamentos, presentar el nombre del departamento y el número de cursos que tiene cada departamento

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from clases import *

# crear una sesion
Session = sessionmaker(bind=engine)
session = Session()

# Join a las otras tablas para encontrar las calificaciones
dep_notas = (
    session.query(
        Departamento.nombre)
    .join(Departamento.cursos,
    	func.count(Curso.id).label("numero_cursos") # uso la funcion count para contar loscursos de los departamentos, tomando el id de los sursos.
    )     
    .join(Curso.tareas)            
    .join(Tarea.entregas)          
    .filter(Entrega.calificacion <= 0.3)
    .group_by(Departamento.id) #Agrupa los resultados por departamento
    .all()
)


#Presentar los departamentos


print("Departamentos que tienen notas menores o iguales a 0.3")
for dep, numero_cursos in dep_notas:
    print(f"Departamento: {dep}")
    print(f"Número de cursos: {numero_cursos}")