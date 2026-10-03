import json
import os
books = []
read_books = []

source = "book_list.json"

if os.path.exists(source):
     if os.path.getsize(source) > 0:
          with open(source, "r", encoding="utf-8") as f:
               convert_to_python = json.loads(f.read())

          books.append(convert_to_python)




#Funcion para agregar libros
def add_book():

     title = input("Books title")
     author = input(f"Who's the author of -{title}-")
     status = "No leido"
     books.append({"Titulo": title, "Autor": author, "Leido": status})

     convert_to_json = json.dumps(books,indent=2)

     with open(source, "w", encoding="utf-8") as f:
          f.write(convert_to_json)

#Funcion para mostrar los libros agregados
def show_books():
     if not books:
          print("There are no books listed")
     else:
          for i , books_items in enumerate(books,start=1):
               print(f"{i}. {books_items["Titulo"]}")
               print(f"Autor: {books_items["Autor"]}")
               print(f"Estado: {books_items["Leido"]}")
               print("-" * 8)

          
#Funcion para marcar libros como leidos, los toma en una variable junto al indice del libro, usando enumerate
#Los elimina usando .pop() guarda el valor, y los envia a la lista correspondiente
def mark_as_read ():

     read = input("Which book you read?")

     found = False

     for check in books:

           if read == check["Titulo"]:
               found = True
               break

     if not found:
           
           print(f"Error -{read}- Was not found")

     elif found:
       
           for i, book in enumerate(books):
             if book["Titulo"] == read:
               check = books.pop(i)
               read_books.append(check)
               print(f"-{book["Titulo"]} - Has been marked as read")
         

#Funcion para mostrar los libros que han sido marcado como "Leidos", logramos esto cambiandole el valor a la clave "Leido"
#para que muestre que el libro ha sido leido
def show_read_books ():

     if not read_books:
          print("No books have been read yet")
     else:
          for i , readbooks in enumerate(read_books, start=1):
               readbooks["Leido"] = "Read"
               print(f"{i}. {readbooks["Titulo"]}")
               print(f"Author: {readbooks["Autor"]}")
               print(f"Status: {readbooks["Leido"]}")
               print("-" * 8)

def delete_books():

     if not books:
          open(source,"w", encoding="utf-8").close()
          print("No books have been added")
     else:
          delete = input("Which book would you like to delete?")

          found_book = False

          for i,book in enumerate(books):
               if delete == book["Titulo"]:
                    found_book = True
                    break

          if found_book:
               del books[i]
               print(f"{book["Titulo"]}- has been succesfully eliminated")
          else:
               print(f"This book -{delete}- was not found among your books")


          
print("Loading menu...")

while True:

     
       print("Menu")

       options = input("1 = Add book, 2 = Show books, 3 = Mark as read, 4 = Show read books 5 = Exit. 6 = Delete books, =")

       if options != "1" and options != "2" and options !="3" and options !="4" and options!="5" and options !="6":
          print(f"Error -{options}- is ot a valid option")

       elif options == "1":
          add_book()

       elif options == "2":
          show_books()

       elif options == "3":
             mark_as_read()

       elif options == "4":
          show_read_books()
 
       elif options == "5":
          print("Closing menu...")
          break
       elif options =="6":
            delete_books()

    

