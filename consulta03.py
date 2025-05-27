# Obtener todas las tareas asignadas a los siguientes estudiantes 

# Jennifer Bolton 
# Elaine Perez
# Heather Henderson
# Charles Harris

# En función de cada tarea, presentar el número de entregas que tiene

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from clases import *

# crear una sesion
Session = sessionmaker(bind=engine)
session = Session()

estudiantes = [
    "Jennifer Bolton",
    "Elaine Perez",
    "Heather Henderson",
    "Charles Harris"
]

# Join a las tablas verificando id de cada estudiante para verificar que los objetos le pertenezcan a ese estudiante
tareas_entregas = (
    session.query(
        Tarea.titulo,
        func.count(Entrega.id).label("numero_entregas") # count -> oara contar el numero de entregas por estudiantes
    )
    .join(Entrega, Entrega.tarea_id == Tarea.id)
    .join(Estudiante, Estudiante.id == Entrega.estudiante_id)
    .filter(Estudiante.nombre.in_(estudiantes))
    .group_by(Tarea.id)
    .all()
)

# Mostrar resultados
print("Tareas y numero de entregas de los estudiantes")
for titulo, numero_entregas in tareas_entregas:
    print(f"Tarea: {titulo} - Entregas: {numero_entregas}")