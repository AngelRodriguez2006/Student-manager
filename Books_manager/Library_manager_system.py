import json
import os
from datetime import datetime


source = "books.json"
books = list()
separator = "-" * 10
not_found_msg = "Was not found."
archive_exists = False
enter_title = "Enter book's title."




def load_data():

    with open(source,"r",encoding="utf-8") as f:
        return json.load(f)

def save_data():

    with open(source,"w", encoding="utf-8") as f:
        json.dump(books,f,indent=2)

def clear_data():

    open(source,"w",encoding="utf-8").close()


if os.path.exists(source):

    archive_exists = True

    if os.path.getsize(source):

        print("Loading data...")
        books = load_data()
        print("Data has been loaded.")
        print(separator)

    else:

        print("No data was found.")
        print(separator)

else:

    print("Generating archive...")
    clear_data()
    print(separator)


def add_book(title,author,date):

    status = "Available"
    read = False

    books.append({"Title":title,"Author":author,"Status":status,"Read":read, "Date":date})
    save_data()
    return True

#This function was created to avoid repeating this process in all function that required finding a specific
#book
def find_book(book_title):

    if books:
        for i,book in enumerate(books):
              if book["Title"] == book_title:
                                
               return True,book,i
            
        return False,None,None


def search_book(title):    

    found,_,i = find_book(title)

    if found:
       return True, i
    return False, None


def delete_book(title):

    found,_,i = find_book(title)

    if found:
        books.pop(i)
        save_data()
        return True
    return False
             
def mark_as_read(title):

    found,book,_ = find_book(title)

    if found:
        book["Read"] = True
        save_data()
        return True
    return False


def borrow_book(title):

    found,book,_ = find_book(title)

    if found:
        if book["Status"] == "Available":
            book["Status"] = "Borrowed"
            save_data()
            return True
    return False


def return_book(title):

   found,book,_ = find_book(title)

   if found:
           if book["Status"] == "Borrowed":
               book["Status"] = "Available"
               save_data()
               return True
   return False

def is_borrowed_available_books (status):

    if books:
        for book in books:
            if book["Status"] == status:
                return True
        return False
    
    return False

def menu():

    while True:

        time_now = datetime.now()

        print("Options.")
        print("1.Add book.")
        print("2.Show books")
        print("3.Search book")
        print("4.Delete book")
        print("5.Read")
        print("6.Borrow book")
        print("7.Return book")
        print("8.Show available books")
        print("9.Show borrowed books")
        print("10.Exit")
        print(separator)

        options = input("Enter option. ")

        if options =="10":
            print("Closing app...")
            break


        try:

            match options:
                case "1":
                    title = input(enter_title)
                    author = input("Name of the author. ")
                    date = time_now.strftime("%Y-%m-%d %H:%M")
                    if add_book(title,author,date):
                        print(f"{title}- Is now available in the library.")
                        print(separator)
                case"2":

                    if books:

                      for i,book in enumerate(sorted(books, key=lambda x: x["Title"].lower()),start=1):
                          print(f"{i}.{book["Title"]}")
                          print(f"Author: {book["Author"]}")
                          print(f"Status: {book["Status"]}")
                          print(f"Read: {book["Read"]}")
                          print(f"Added on: {book["Date"]}")
                          print(separator)
                    else:
                        print("No books found.")
                        

                case "3":

                    book_to_search = input(enter_title)
                    check,_ = search_book(book_to_search)
                    if check:
                        _,i = search_book(book_to_search)
                        i+=1              
                        print(f"{book_to_search} was found in position.{i}")
                        print(separator)
                    else:
                        print(f"{book_to_search} {not_found_msg}")
                        print(separator)

                case "4":

                    book_to_delete = input(enter_title)

                    if delete_book(book_to_delete):
                        print(f"{book_to_delete} has been deleted.")
                        print(separator)
                    else:
                        print(f"{book_to_delete} {not_found_msg}")
                        print(separator)

                case "5":

                    book_to_read = input(enter_title)   
                    if mark_as_read(book_to_read):
                        print(f"{book_to_read} has been read.")
                        print(separator)
                    else:
                        print(f"Unable to read -{book_to_read}- Not found")
                        print(separator)

                case "6":

                    book_to_borrow = input(enter_title)
                    if borrow_book(book_to_borrow):
                        print(f"{book_to_borrow} successfully borrowed.")
                        print(separator)
                    else:
                        print(f"unable to borrow -{book_to_borrow}- can only borrow available books.")
                        print(separator)


                case "7":

                    book_to_return = input(enter_title)
                    if return_book(book_to_return):
                        print(f"{book_to_return}- successfully returned.")
                        print(separator)
                    else:
                        print(f"{book_to_return}- can only return borrowed books.")

                case "8":

                    if is_borrowed_available_books("Available"):

                        for i,book in enumerate(sorted(books, key =lambda x: x["Title"].lower()),start=1):
                            if book["Status"] == "Available":
                                print(f"{i}.{book["Title"]}")
                                print(f"Author: {book["Author"]}")
                                print(f"Status: {book["Status"]}")
                                print(f"Read: {book["Read"]}")
                                print(f"Added on: {book["Date"]}")
                                print(separator)

                    else:
                        print("There aro not available books.")
                        print(separator)

                case "9":

                     if  is_borrowed_available_books("Borrowed"):
                        for i,book in enumerate(sorted(books, key =lambda x: x["Title"].lower()),start=1):
                            if book["Status"] == "Borrowed":
                                print(f"{i}.{book["Title"]}")
                                print(f"Author: {book["Author"]}")
                                print(f"Status: {book["Status"]}")
                                print(f"Read: {book["Read"]}")
                                print(f"Added on: {book["Date"]}")
                                print(separator)
                     else:
                        print("There are not borrowed books.")   
                        print(separator)

                case _:
                  print(f"{options} is not a valid option. Select one from below")      
        except:
            print("Unable to run program. Error#223")
         
              
if __name__ == "__main__":
    menu()  