import sys
from datetime import datetime
import os
import json

# Función principal
def main():
    # sys.argv es la fila que se va creando
    # app.py = [0]
    # [1] = lo que se requiere hacer (add, to do, done) = request

    # pregunta si hay menos de 2 datos, te brinda ayuda para usar el script
    if len(sys.argv) < 2:
        print("Usage: python app.py <command>")
        # Regresa a main
        return
    
    # Igualamos variable command al request
    command = sys.argv[1]

    # si command es igual a add
    if command == "add":
        # sys.argv < 3     e.g. sys.argv =["app.py", "add"]
        # no estas declarando que add quieres añadir, por eso dice "provide a task description"
        if len(sys.argv)<3:
            print("Please provide a task description")
            return
        # añade la task que se asignó en el espacio [2]
        # e.g. ["app.py", "add", "task added"]
        add_task(sys.argv[2])
    
    elif command == "list": # si sys.argv[1] es igual a list
        if len(sys.argv)>2: # por ejemplo sys.argv = ["app.py", "list", "todo"] 
            list_tasks(sys.argv[2]) # va a mostrar tareas to do
        else:
            list_tasks() # muestra todas las tareas
    
    # marcar como done las task
    elif command == "mark-done": # si command = done
        if len(sys.argv)<3: # si sys.argv < 3 escribe que proporcione una task id
            print("Please provide a task ID")
            return
        update_status(int(sys.argv[2]), "done") # escribe "done"

    # Marcar como in progress las task
    elif command == "mark-in-progress": # si command = inprogress
        if len(sys.argv)<3: # si sys.argv < 3 escribe que proporcione una task id
            print("Please provide a task ID")
            return
        update_status(int(sys.argv[2]), "in-progress") # Imprime in progress
    
    # Eliminar task
    elif command == "delete":
        if len(sys.argv)<3:
            print("Proporciona una task ID")
            return
        delete_task(int(sys.argv[2]))
    
    # Update task
    elif command == "update":
        if len(sys.argv)<4:
            print("Proporciona una task ID y una nueva descripción")
            return
        update_task(int(sys.argv[2]), sys.argv[3])
    

    else:
        print(f"Unknown command: {command}") # desconocido

    


FILE = "tasks.json" # almacena tasks.json en la variable FILE

def load_tasks(): # lee tarea
    if not os.path.exists(FILE): # si no existe el archivo
        return [] # regresa un array vacio
    
    with open(FILE, "r") as f: # Abre el archivo en lectura
        try:
            return json.load(f) # archivo lo pasa a python
        except: 
            return [] # array vacio
        
def save_tasks(tasks): # guarda tarea
    with open(FILE, "w") as f: # Abre el archivo en escritura
        json.dump(tasks, f, indent=2) # Python → JSON

# añade task description
def add_task(description):
    
    tasks = load_tasks() # guarda json en tasks
    now = datetime.now().isoformat() # obtener fecha actual

    # Llenado de task
    task = {
        "id": len(tasks) + 1, # ID ultima task + 1
        "description": description, 
        "status": "todo",
        "createdAt": now,
        "updatedAt": now

    }

    tasks.append(task) # añade task a tasks
    save_tasks(tasks) # guarda tasks
    
    print(f"Task added successfully (ID: {task['id']})") # Genera texto que se guardó la tarea

def update_task(task_id, new_description):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break

    if not found:
        print("Task not found")
        return

    save_tasks(tasks)
    print("Task updated successfully")

# listar task
def list_tasks(filter_status=None):
    tasks = load_tasks() # lee el json

    if filter_status:
        if filter_status == "not-done":
            tasks = [t for t in tasks if t["status"] != "done"]
        else:
            tasks = [t for t in tasks if t["status"] == filter_status]
    
    if not tasks: # si hay lista vacia
        print("No tasks found")
        return
    
    for task in tasks: # Recorre cada tarea
        print(f"{task['id']}. {task['description']} [{task['status']}]")

# actualizar status
def update_status(task_id, new_status): # parámetros (task ID, nuevo estado -> "done", "in-progress")
    tasks = load_tasks() # lee JSON y obtiene lista
    found = False # sirve para saber si encontramos la tarea

    for task in tasks: # Recorre cada tarea, va una por una, primero task 1 y luego task 2
        if task["id"] == task_id: # Busca por ID
            task["status"] = new_status # Actulizar datos "todo" -> "done"
            task["updatedAt"] = datetime.now().isoformat() # Actualiza fecha
            found = True # Indica que si se encontró
            break # sale del loop, ya no sigue buscando
    
    if not found: # Si nunca encontró la tarea
        print("Task not found") # Imprime Task not found
        return # Regresa al principal
    
    save_tasks(tasks) # Guarda lista actualizada en JSON
    print(f"Task {task_id} updated to {new_status}") # Ejemplo: Task 1 updated to done

def delete_task(task_id):
    tasks = load_tasks() # Cargar tareas, obtienes lista actual

    new_tasks = [t for t in tasks if t["id"] != task_id] # quedate con todas las tareas menos la que quiero borrar

    if len(tasks) == len(new_tasks): # si no cambió el tamaño, significa que no encontró ese ID
        print("Task not found") # Imprime Task not found
        return # Regresa a principal
    
    save_tasks(new_tasks) # Guarda task actual
    print(f"Task {task_id} deleted successfully") # Imrpime task Id deleted


if __name__ == "__main__":
    main()



"""
json.load()	JSON → Python
json.dump()	Python → JSON

load_tasks()  ->	leer datos
for	          ->    recorrer
if id	      ->    buscar
status =	  ->    modificar
save_tasks()  ->	guardar
found	      ->    validar

"""