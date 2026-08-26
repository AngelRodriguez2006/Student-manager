import json
import os
from datetime import date


expenses = list()
source = "expenses.json"
separator = "-" * 10
run_menu = False

def load_data ():

    with open(source,"r",encoding="utf-8") as f:
       return json.loads(f.read())
    
if os.path.exists(source):
   if os.path.getsize(source) > 0:
      print("Loading data")
      run_menu = True
      expenses = load_data()
      print("Data has been loaded")

   else:
      print("No previous data found")
      

def save_data ():
   with open(source,"w",encoding="utf-8") as f:
      f.write(json.dumps(expenses, indent=2))

def clear_data ():
   open(source,"w",encoding="utf-8").close()

def add_expense (description,amount,category):

   date_time = str(date.today())
   match category:
      case "1":
         category = "Food"
      case "2":
         category = "Transport"
      case "3":
         category = "Health"
      case "4":
         category = "Entertainment"
      case "5":
         category = "Education"
      case "6":
         category = "Other"
      case _:
         category = "Undefined"

   expenses.append({"Description": description, "Amount": amount, "Category":category, "Date": date_time})

def find_expense (value):
   
   if expenses:
    for expense in expenses:
       if expense["Description"] == value:
          return True
    return False
      
def delete_expenses (description):

   if find_expense(description):
      for i,expense in enumerate(expenses):
         if expense["Description"] == description:
           expenses.pop(i)
           save_data()
           break
      return f"{description}- has been deleted"

   else:
            return f"{description} was not found"

def search_expense (description):

   if find_expense(description):
      for i,expense in enumerate(expenses,start=1):
         if expense["Description"] == description:
            break
      return f"{description}- was found in position-{i}. Amount:{expense["Amount"]}"
         
   else:
            return f"{description}- was not found"

def total_expenses ():

   total = 0
   if expenses:
      for expense in expenses:
         total += expense["Amount"]
      return f"Total: {total}"
   else:
      return "No expenses were found"

def empty_list (yes_no):

   match yes_no:
      case "1":
         expenses.clear()
         clear_data()
         return "All expenses have been erased"

      case _:
         return "No expenses were deleted"

def menu():

   while True:

      print("Options.")
      print("1.Add expense.")
      print("2.Show expenses.")
      print("3.Delete expense.")
      print("4.Search expense.")
      print("5.Show total.")
      print("6.Clear all expenses.")
      print("7.Exit.")

      option = input("Enter an option. ")

      match option:
         case "1":
            description = input("Expense name. ")
            amount = float(input("Expense amount. "))
            print("Caregories")
            print("1.Food")
            print("2.Transport")
            print("3.Health")
            print("4.Entertainment")
            print("5.Education")
            print("6.Other")
            category = input("Choose a category. ")

            add_expense(description,amount,category)
            save_data()
         case "2":

            if expenses:
               for i,expense in enumerate(expenses,start=1):
                  print(separator)
                  print(f"{i}. Description: {expense["Description"]}")
                  print(f"Amount: {expense["Amount"]}")
                  print(f"Category: {expense["Category"]}")
                  print(f"Date: {expense["Date"]}")

         case "3":

            expense_to_remove = input("Which expense you'd like to delete?. ")
            print(delete_expenses(expense_to_remove))

         case "4":

            search = input("What expense ur looking for?. ")
            print(search_expense(search))
         case "5":
            print(total_expenses())
         case "6":
            print("You sure you want to delete all expenses?")
            print("1.Yes")
            print("2.No")
            yes_no = input("Enter your option")
            print(empty_list(yes_no))
         case "7":
            print("Closing menu")
            break
            

if run_menu:
   menu()
else:
    open(source,"w",encoding="utf-8").close()
    menu()


