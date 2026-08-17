import json
import os
exists = False
source = "archive.json"
students = list()

if os.path.exists(source):
 
 if os.path.getsize(source) <= 0:
     print("Empty archive")
 else:
  exists = True
  print("loading data...")
  with open(source, "r", encoding="utf-8") as f:
      source_content = f.read()
  convert_content = json.loads(source_content)
  
  students = [data for data in convert_content]
  

#Funcion para agregar estudiantes, y todos los valores que llevan
def add_student ():

    name = input("Nombre del estudiante")
    career = input("Carrera del estudiante")
    age = int((input("Edad del estudiante")))
    students.append({"Nombre": name, "Carrera": career, "Edad": age})

    if not students:  
     
     open(source,"w",encoding="utf-8").close()
    
    else:
        students_to_json = json.dumps(students, indent=2)

        with open(source, "w", encoding="utf-8") as f:
             f.write(students_to_json)

#Funcion para mostrar los estudiantes y sus debidas caracteristicas
def show_students ():

    if not students:

        print("No hay estudiantes enlistados aun")
    else:

        for i, show in enumerate(students, start=1):
             print(f"{i}.Nombre: {show["Nombre"]}")
             print(f" Carrera: {show["Carrera"]}")
             print(f" Edad: {show["Edad"]}")
             print("-" * 10)

#Funcion para buscar estudiantes que esten en la lista de estudiantes
def search_student ():

    if not students:
        print("No se ha agregado ningun estudiante")

    else:

     search = input("Que estudiante desea buscar?")

     found = False

     for  estudiante in students:

        if search == estudiante["Nombre"]:
            found = True
            break

     if found:
        print("Buscando estudiante en la base de datos...")
        print(f"Nombre: {estudiante["Nombre"]}")
        print(f"Carrera: {estudiante["Carrera"]}")
        print(f"Edad: {estudiante["Edad"]}")

     else:
    
        print(f"Este estudiante -{search}- No se encuentra en la lista")
    
                   


    #Funcion para remover estudiantes
def remove_student ():

        remove = input("Que estudiante deseas remover")

        is_here = False

        for i,student in enumerate(students):
            if remove == student["Nombre"]:
                is_here = True
                break

        if is_here:
            print("Removing student...")

            del students[i]

            print("El estudiante Ha sido removido con exito")
        else:
            print("El estudiante No se puede remover ya que no se hayo este estudiante")

        

#Funcion para modificar alguna caracteristica del estudiante
def modify_student ():

    modify = input("Nombre del estudiante que quiere modificar. =")

    was_found = False

    for nombre in students:
        if modify == nombre["Nombre"]:
            was_found = True
            break
    if was_found:

        what_modify = input("Que desea modificar del estudiante? 1= Nombre, 2= Carrera, 3=Edad. =")
        if what_modify == "1":
            new_name = input("Nuevo nombre:. ")
            nombre["Nombre"] = new_name
            print(f"El estdudiante -{modify}- ha sido modificado con exito")
        elif what_modify == "2":
             new_career = input("Nueva carrera? =")
             nombre["Carrera"] = new_career
             print(f"El estdudiante -{modify}- ha sido modificado con exito")
        elif what_modify == "3":
             new_age = input("Agegar nueva edad")
             nombre["Edad"] = int(new_age)
             print(f"El estdudiante -{modify}- ha sido modificado con exito")
         
    else:
        print(f"No se puede modificar -{modify}- debido a que no existe en la lista de estudiantes")
            
             

print("Loading menu...")

while True:



    print("Menu")

    options = input("Que deseas hacer. 1= Agregar nuevo estudiante, 2= Mostrar estudiantes, 3= Buscar estudiante, 4= Eliminar estudiante, 5= Modificar estudiantes, 6= salir")

    if options == "1":
        add_student()
    elif options == "2":
        show_students()
    elif options == "3":
        search_student()
    elif options == "4":
        remove_student()
    elif options == "5":
        modify_student()
    elif options == "6":
        print("Closing menu...")
        break

    








