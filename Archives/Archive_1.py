
#verificar si el archivo existe para que python no se vuelva loco 
import os

archive_route = "carpeta.txt"

archives_list = []



#Esta parte del codigo lo que hace es = una vez inicia visual estudio code, todo lo que esta 
#en el archivo, se lee y se pega a la lista, para que compartan "los mismos datos"
if os.path.exists(archive_route):
    print("Loading data...")
    with open(archive_route, "r", encoding="utf-8") as archive:
        
        #Este codigo de aca abajo, es comprension de listas, ni sabia que existia, pero ya aprendi que se puede usar B)
        archives_list = [nombre.strip() for nombre in archive.readlines()]
    print("Data has been loaded succesfully")

else:
    print("This archive does not exist")

#Aca usamos una funcion que agrega una nota a la lista, y a su vez open("a") la agrega al archivo de texto.
def add_note ():

    note = (input("Add note"))

    archives_list.append(note)

    with open(archive_route, "a", encoding="utf-8") as archive:
      archive.write(f"{note}\n")
    print(f"La nota -{note}- ha sido agregada a la lista de notas")

#Aca pues hacemos algo extremadamente simple, es literalmente recorrer la lista y imprimir los datos
def show_notes ():
    if not archives_list:

        print("The archive is empty")
    else:

       print("Notas:")

       for lista in archives_list:
           print(lista)

#Y aca pues, eliminamos todos los datos del archivo .txt, y para ir a la par, vaciamos la lista tambien
def delete_all_notes ():

    if not archives_list:
        print("There are no notes to delete.")
    else:
        print("Deleting data...")
        open(archive_route, "w", encoding="utf-8").close()
        archives_list.clear()
        print("Data has been erased succesfully")

def delete_note ():


    if not archives_list:
        print("Not able to delete notes, notepad empty")

    else:

        #usamos este codigo para pedir un str, y eliminamos la nota que se nos de de la lista
        delete = str(input("Escribe la nota para borrarla"))
       

        if delete not in archives_list:
            print(f"Esta nota -{delete}- no se encuentra en el notepad")

        else:

            archives_list.remove(delete)
            print(f"-{delete}- ha sido eliminado exitosamente")

            #aca limpiamos el archivo entero para poder usar "a" para rescribir las notas que no fueron eliminadas
            open(archive_route,"w",encoding="utf-8").close()

            with open(archive_route, "a", encoding="utf-8") as archive:
                    
                    for remaining_notes in archives_list:    
                        archive.write(f"{remaining_notes}\n")


#Funcion para buscar notas parcialmente, y escribir su contenido completo
def search_note ():

    found_notes =[]

    found_note = False

    
    if os.path.getsize(archive_route) <= 0:

        print("Unable to find any notes, no notes on notepad")

    else:

        find = input("Write the note you are looking for")
        for i,note in enumerate(archives_list):
            if find in note:
                found_notes.append(note)

                found_note = True

        if found_note:

            for found in found_notes:
                 print(found)


        elif not found_note:

            print(f"This note -{find}- was not found in the notepad")



def edit_note():

    found_note = False

    edit = input("Which note would u like to edit")

    for i,note in enumerate(archives_list):

        if edit == note:
            found_note = True
            break

    if found_note:

        print("note has been found...")

        new_note = input("Whats the new note: ")

        archives_list[i] = new_note
        print(i)

        open(archive_route, "w", encoding="utf-8").close()

        with open(archive_route, "a", encoding="utf-8") as archive:

             for note in archives_list:
                 archive.write(f"{note}\n")
    else:
        print(f"-{edit}- Was not found")



print("Loading menu...")

while True:

    print("Menu")

    options = input("Opciones. 1= Add note, 2= Show notes, 3= Delete all notes, 4= Exit, 5= delete note, 6= search note, 7=edit note. =")

    if options == "1":
        add_note()
    elif options == "2":
        show_notes()
    elif options == "3":
        delete_all_notes()
    elif options == "4":
        print("Closing menu...")
        break
    elif options == "5":
        delete_note()
    elif options == "6":
        search_note()
    elif options == "7":
        edit_note()
   