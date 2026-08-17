tasks = {

      "tarea": [],
       "prioridad": [],
       "estado":[]
}

completed_tasks = {

    "tarea": [],
    "prioridad": [],
    "estado": []
}

def add_task ():
      
        task = input("Nombre de la tarea = ")
        priority = input("Prioridad de la tarea = ")
        tasks["tarea"].append(task)
        tasks["prioridad"].append(priority)
        tasks["estado"].append("Pendiente")

def show_tasks ():
    if not tasks["tarea"]:
        print("No se ha agregado ninguna tarea")
    else:
         print("Tareas pendientes")
         for i, (nombre,prioridad,status) in enumerate(zip(tasks["tarea"], tasks["prioridad"], tasks["estado"]),start=1):
          
           print(f"{i}-{nombre} | prioridad: {prioridad} | estado: {status}")

def complete_tasks ():
     
     completed = input("Que tarea deseas completar?")
     
     if completed not in tasks["tarea"]:
         print(f"Esta tarea -{completed}- No existe")
     else:  
         task_index = tasks["tarea"].index(completed)
         completed_tasks["tarea"].append(completed)
         delete = tasks["prioridad"].pop(task_index)
         completed_tasks["prioridad"].append(delete)
         del tasks["estado"][task_index]
         completed_tasks["estado"].append("completado")
         tasks["tarea"].remove(completed)
         print(f"{completed} - Ha sido completada correctamente")

def show_completed_tasks ():
    if not completed_tasks["tarea"]:
         print("No se ha completado ninguna tarea")
    else:
          print("Tareas Completadas")
          for i, (name, priority, status) in enumerate(zip(completed_tasks["tarea"], completed_tasks["prioridad"], completed_tasks["estado"]),start=1):
           print(f"{i}-{name} | Prioridad: {priority} | Estado: {status}")

while True:
      
      print("-Menu-")
      options = input("1 = add task, 2 = show tasks, 3 = complete task, 4 = show completed tasks, 5 = exit. =")
      if options == "1":
        add_task()
      elif options == "2":
        show_tasks()
      elif options == "3":
          complete_tasks()
      elif options == "4":
          show_completed_tasks()
      elif options == "5":
          print("Closing menu...")
          break