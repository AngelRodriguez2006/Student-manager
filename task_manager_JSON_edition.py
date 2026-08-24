import os
import json

tasks = list()
source = "tasks.json"
run_menu = False
separator = "-" * 10

def load_data ():

    with open(source,"r",encoding="utf-8") as f:
         return json.loads(f.read())

if os.path.exists(source):

    run_menu = True

    if os.path.getsize(source) > 0:
        print("Loading data...")
        tasks = load_data()
        print("Data's been successfully loaded")
        print(separator)

    else:

        print("Unable to load data, empty archive. Error:001")
        print(separator)


def save_tasks ():

    with open(source,"w",encoding="utf-8") as f:
        f.write(json.dumps(tasks, indent=2))

def clear_archive ():

    open(source,"w",encoding="utf-8").close()
     
        
def add_task (task_name,task_priority,task_status):

    if task_priority == "1":
        priority = "Low"
    elif task_priority =="2":
        priority = "Medium"
    elif task_priority =="3":
        priority = "High"
    
    tasks.append({"Task":task_name, "Priority":priority, "Status": task_status})
    
def found_task(value):
     
     found_task = False
    
     if tasks:
        for task in tasks:
         if task["Task"] == value:
            found_task = True
            break

        if found_task:
           return True
     
        else:
          return False
     else:
         clear_archive()
         return False

def delete_task (task_name):

    if found_task(task_name):
        
        for i,task in enumerate(tasks):
            if task["Task"] == task_name:
                tasks.pop(i)
                save_tasks()
                break

        return f"{task_name} has been deleted"
                
    else:
        return f"{task_name}- was not found"
    
def complete_tasks (task_name):

        if found_task(task_name):
            for task in tasks:
                if task["Task"] == task_name:
                    task["Status"] = "Completed"
                    save_tasks()
                    break
            return f"{task_name}- Has been completed"
        else:
            return f"{task_name}- was not found"

def search_tasks (task_name):

    if found_task(task_name):
        for i,task in enumerate(tasks,start=1):

            if task["Task"] == task_name:
             break

        return f"{task_name}- was found in position {i}"

    else:
      return f"{task_name}- was not found"


def clear_tasks (yes_no):

    if yes_no == "1":
       clear_archive()
       tasks.clear()
       return "All data has been cleared"
    
    else:
        return "Data was not deleted"

print(separator)
print("Loagine menu...")
print(separator)

def menu():

    while True:
       print(separator)
       print("Options")
       print("1.Add task. ")
       print("2.Delete task. ")
       print("3.Show tasks. ")
       print("4.Complete task. ")
       print("5.Show completed tasks. ")
       print("6.Search tasks. ")
       print("7.Clear tasks. ")

       select_option = input("Choose an option. ")

       if select_option == "1":
           
           task_name = input("Task name. ")
           print("choose your task priority")
           print("1. Low ")
           print("2. Medium")
           print("3. High")

           task_priority = input("Choose priority. ")
           status = "Not completed"

           add_task(task_name,task_priority,status)
           save_tasks()
       elif select_option == "2":

           task_to_delete = input("Name of the task. ")
           print(separator)
           print(delete_task(task_to_delete))
           print(separator)

       elif select_option == "3":
           if tasks:
               for i,task in enumerate(tasks,start=1):
                   
                   print(f"{i}. Task: {task["Task"]}")
                   print(f"Priority: {task["Priority"]}")
                   print(f"Status: {task["Status"]}")
                   print(separator)
           else:
               print("No tasks have been added yet")

       elif select_option == "4":
           
           task_to_complete = input("Enter task. ")
           print(complete_tasks(task_to_complete))

       elif select_option == "5":

           if tasks:

               print("Completed tasks")

               for i,task in enumerate(tasks):
                   if task["Status"] == "Completed":
                     print(f"{i}. Task: {task["Task"]}")
                     print(f"Priority: {task["Priority"]}")
                     print(f"Status: {task["Status"]}")
                     print(separator)
           else:

               print("No completed tasks were found")
       elif select_option == "6":

           task_to_find = input("Enter task. ")
           print(separator)
           print(search_tasks(task_to_find))
           print(separator)

       elif select_option =="7":

           print("Are you sure you want to delete all tasks?")
           print("1. Yes")
           print("2. No")
           yes_no = input("Enter your decision. ")

           print(separator)
           print(clear_tasks(yes_no))
           print(separator)

      
                 

if run_menu:
    menu()

else:

    open(source,"w",encoding="utf-8").close()
    menu()


    
            


        



