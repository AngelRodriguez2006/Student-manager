estudiantes = []
repeater = 0
while repeater<1:
 
 options = input("Opciones = 1 = add student, 2 =show students, 3=delete students, 4=exit")
 if options == "1":
  add_student = input("Add student")
  estudiantes.append(add_student)
 elif options == "2":
  print(f"Lista de estudiantes actuales = {estudiantes}")
 elif options == "3":
   #Aqui podemos usar el if remove_student in estudiantes podemos remover, de lo contrario no
   remove_student = input("Remove student by name")
   estudiantes.remove(remove_student)

 elif options == "4":
  repeater = 1
 else:
  print("Error not a valid option")