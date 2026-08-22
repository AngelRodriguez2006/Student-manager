import os
import json

finished = "Read"
source = "books.json"
books = list()
separator = "-" * 10
run_menu = False



#Here we check if the archive exists and if there is any content on it, so we can read it and
#write the content in the book list
if os.path.exists(source):
    run_menu = True

    source_size = os.path.getsize(source)
    if source_size > 0:

     print(f"Loading data from -{source}-...")
     with open(source, "r", encoding="utf-8") as f:
         books = json.loads(f.read())
     print("Data has been loaded successfully")
     print(separator)

    else:
      print("Failed to load data.")
      print("No content found")
 
print(separator)

def write_to_file ():

    with open(source,"w",encoding="utf-8") as f:
        f.write(json.dumps(books,indent=2))


def empty_file ():

    open(source,"w",encoding="utf-8").close()

def add_book (title,author,status):

    return({"Title": title, "Author": author, "Status":status})

def delete_book (title):

 delete = False

 if books:
   
    for i,book in enumerate((books)):
      if title == book["Title"]:
          delete = True
          break

    if delete:

        return f"{title}- has been removed{books.pop(i)}"

    else:
        return f"{title}- was not found"
 else:
     return"No books have been added"


def search_book (title):

    found_book = False

    for i,book in enumerate(books,start=1):
        if title == book["Title"]:
            found_book = True
            break

    if not found_book:

        return f"-{title}- Was not found"

    else:
        return f"{title}- Was found in position.{i}"

def mark_as_read (title):

    found = False

    if books:
     
     for book in books:

        if title == book["Title"]:
           found = True
           break

     if found:
         modify = book["Status"] = "Read"

         empty_file()

         write_to_file()

         return f"{title}- has been {modify}"
         
     else:

         return f"{title}- was not found"

def clear_data (condition):
        

        if condition == "1" and books:
         empty_file()
         return f"{books.clear()}- All books have been deleted"

        else:
            return"No books were deleted"
         

print(separator)
print("Loading menu")
print(separator)

def menu():
  while True:
     
     source_size = os.path.getsize(source)

     print("Options")
     print("1.Add book")
     print("2.Show books")
     print("3.Delete book")
     print("4.Search book")
     print("5.Mark book as read")
     print("6.Show read books")
     print("7.Clear book's list")
     print("8.Exit menu")

     options = input("Select an option. ")

     if options == "1":
         title = input("Book's Title. ")
         author = input("Book's Author. ")
         status = "Not read"

         add_to_list = add_book(title,author,status)
         books.append(add_to_list)
         
         write_to_file()

         print(separator)
         print(f"{title}-- Has been added")
         print(separator)  
         

     elif options == "2":
         
         source_size = os.path.getsize(source)

         if books:
             
             for i,show in enumerate(books, start=1):

                 print(separator)
                 print(f"{i}.Title: {show["Title"]}")
                 print(f"Author: {show["Author"]}")
                 print(f"Status: {show["Status"]}")
                 print(separator)
         else:
             
             print("No books have been added")
             print(separator)
          
         
     elif options == "3":
          
         del_book = input("Enter books title. ")
         print(separator)
         print(delete_book(del_book))
         print(separator)
         if books:
             write_to_file()
         else:
             empty_file()
    


     elif options == "4":

         search = input("Enter book's title. ")

         print(separator)
         print(search_book(search))
         print(separator)

     elif options == "5":

         title = input("Book to mark as read?. ")
         print(separator)
         print(mark_as_read(title))
         print(separator)

     elif options == "6":

         read_books = False

         if books:

            for i,read in enumerate(books, start=1):

              if read["Status"] == "Read":
                  read_books = True
                  print(separator)
                  print(f"{i}. Title: {read["Title"]}")
                  print(f"Author: {read["Author"]}")
                  print(f"Status: {read["Status"]}")
                  print(separator)

            if not read_books:
                print(separator)
                print("No books have been read yet")
                print(separator)
         else:
             print(separator)
             print("No books have been added")
             print(separator)

     elif options == "7":

         print("Are you sure you want to delete all the content?")
         print("1.Yes")
         print("2.No")

         yes_no = input("Enter your desicion. =")

         print(separator)
         print(clear_data(yes_no))
         print(separator)

     elif options == "8":
         
         print(separator)
         print("Closing menu...")
         break

if run_menu:
    menu()

else:
    print("Fatal Error:002. Arvhice was not found.")

        

    
             

         

                  

         

          

            



