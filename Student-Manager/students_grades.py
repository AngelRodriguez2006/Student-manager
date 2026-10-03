import os
import json
import statistics as stats
from datetime import datetime as dt


enter_name = "Enter student's name. "
separator = "-" * 10
students = list()
source = "students.json"
source_report = "class_report.txt"
archive_exists = False



def load_data():
    with open(source,"r",encoding="utf-8") as f:
        class_load = json.load(f)
        
    with open(source_report, "r", encoding="utf-8") as f1:
        report_load = f1.read()
        
    return class_load,report_load

def save_data():
    with open(source,"w",encoding="utf-8") as f:
        json.dump(students,f,indent=2)

def clear_data(students):
    open(source,"w",encoding="utf-8").close()
    open(source_report,"w",encoding="utf-8").close()
    students.clear()
    

if os.path.exists(source) and os.path.exists(source_report):
    archive_exists = True
    if os.path.getsize(source) > 0:
        print("Loading data...")
        students,class_report = load_data()

        print("Data has been loaded successfully")
    else:
        print("Archive is empty.")
else:
    print("Generating archive")
    clear_data(students)

def find_student(student_to_find):

    if students:
        i,student = next(((i,student)for i,student in enumerate(students) if student["Name"] == student_to_find),(None,None))
        if student:
            return True, student, i
    return False,None,None

def add_student (name):

    students.append({
        "Name": name,
        "Grades": list()
    })
    save_data()

def add_grade (name, grade):

    verify,student,_ = find_student(name)
    if verify:
        if grade >= 0 and grade <= 100:
         student["Grades"].append(grade)
         save_data()
         return True  
    return False


def delete_student(name):

    verify,_,i = find_student(name)
    if verify:
        students.pop(i)
        save_data()
        return True
    return False

def student_average(name):

    verify,student,_ = find_student(name)
    if verify:
        if len(student["Grades"]) >= 1:
           average = stats.mean(student["Grades"])
           return True, average
    return False,None

def failed_students():
    
    if students:
        
        low_avg_students = [f"{student["Name"]} ({stats.mean(student["Grades"])})" for student in students if len(student["Grades"]) > 0 and stats.mean(student["Grades"]) < 70]
        
        if low_avg_students:
            return True, low_avg_students
    return False,None


def statistics(students):

    if students:
      
      key = lambda x: x[1]
      averages = list()
      grades = list()

      for i,student in enumerate(students,start=1):
         if len(student["Grades"]) > 0:
             averages.append([student["Name"],round(stats.mean(student["Grades"]),2)]) 
             grades.append(",".join(map(str,student["Grades"])))
      if averages and grades:
         print("True")

         general_average = round(stats.mean(map(float, ','.join(grades).split(','))),2)
         top_students = sorted(averages, key=key, reverse=True)[:3]
         tops = "\n".join([f"{i}.Name:{student[0]}\n Average: {student[1]}" for i,student in enumerate(top_students,start=1)])
         highest_average,lowest_average = max(averages, key =key),min(averages, key =key)
         all_students = "\n\n".join([f"{i}.{student["Name"]} {student["Grades"]}" for i,student in enumerate(students,start=1)])

        
      
         return True,highest_average,lowest_average,i,general_average,tops,all_students
   
    return False,None,None,None,None,None

def report_generator ():
   
    time_now = dt.now()
    date = time_now.strftime("%Y-%m-%d %H:%M")

    verify,h_average,l_average,n_of_students,general_average,tops,all_students = statistics(students)
    if verify:
     
     _,failed = failed_students()
     try:
      failed_stds = "\n".join(map(str, failed))
     except:
         failed_stds = "No failed students"
         

     class_report = (f"""{separator*3}
     ===CLASS REPORT===

Generated on: {date}

Class Stats:

Active students: {n_of_students}
Highest average: {f"{h_average[0]} ({h_average[1]})"}
Lowest average: {f"{l_average[0]} ({l_average[1]})"}
General average: {general_average}
{separator}

Top  Students

{tops}

{separator}

Failed students

{failed_stds}

{separator}

All students

{all_students}

{separator*3}""")
    
     with open(source_report, "w", encoding="utf-8") as f:
          f.write(class_report)
    if verify:

     return True,class_report
    return False,None

def menu():

    while True:

        print("Options")
        print("1.Add student")
        print("2.Add grade")
        print("3.Show students")
        print("4.Search student")
        print("5.Delete student")
        print("6.Student average")
        print("7.Top/bottom student")
        print("8.Failed students")
        print("9.Statistics")
        print("10.Top students")
        print("11.Generate class report")
        print("12.Show class report")
        print("13.Clear all data")
        print("14.Exit")

        options = input("Enter option. ")

        if options == "14":
            print("Closing menu...")
            break

        try:

         match options:
            case "1":
                student_name = input(enter_name)
                add_student(student_name)
                print(f"{student_name}- Has been added")
                print(separator)
                
            case "2":
                student_name = input(enter_name)
                grade_to_add = float(input("Add grade. "))
                if add_grade(student_name,grade_to_add):
                    print(f"{grade_to_add}- has been added to {student_name}")
                    print(separator)
                else:
                    print(f"Unable to add grade, invalid grade or student was not found.")
                    print(separator)
            case "3":
                if students:
                    for i,student in enumerate(students,start=1):

                         print(f"{i}.{student["Name"]}")
                         print(f"Grades: {",".join(map(str,student["Grades"]))}")
                         print(separator)
                else:
                    print("No students were found.")

            case "4":

                student_to_find = input(enter_name)
                verify,grade,position = find_student(student_to_find)

                if verify:
                    position +=1
                    print(f"{student_to_find}- was found in position {position}")
                    print(f"Grades: {grade["Grades"]}")
                    print(separator)
                else:
                    print(f"{student_to_find}- was not found.")
                    print(separator)

            case "5":
                student_to_delete = input(enter_name)
                if delete_student(student_to_delete):
                    print(f"{student_to_delete}- has been deleted")
                    print(separator)
                else:
                    print(f"{student_to_delete} was not found")
                    print(separator)
            case "6":

                student_name = input(enter_name)
                verify,average = student_average(student_name)
                if verify:
                    print(f"{student_name}'s average = {average}")
                    print(separator)
                else:
                    print(f"No grades have been assigned to -{student_name}- yet")
                    print(separator)
            case "7":

                 if students:
                     
                     verify,top_student,bottom_student,_,_,_,_ = statistics(students)

                     if verify:
                         print(f"Top student: {top_student[0]}\n Average: {top_student[1]}")
                         print(separator)
                         print(f"Bottom: {bottom_student[0]}\n Average: {bottom_student[1]}")
                         print(separator)

                 else:
                     print("No students were found")
                     print(separator)
                                
            case "8":

                verify, failed = failed_students()

                if verify:
                    
                    print("Failed students")
                    print("\n".join(map(str, failed)))
                    print(separator)

                else:
                    print("No failed students found.")
                    print(separator)
            case "9":
                

                verify,highest_average,lowest_average,amount_of_students,general_average,top_students,_ = statistics(students)

                if verify:
                    print("Statistics:")
                    print(separator)
                    print(f"Highest average: {highest_average[0]} ({highest_average[1]})")
                    print(f"Lowest average: {lowest_average[0]} ({lowest_average[1]})")

                    print(f"General average: {general_average}")
                    print(f"Number of students: {amount_of_students}")
                    print(separator)
                    
                    print("TOP STUDENTS")

                    print(top_students)

                    print(separator)

                    print("Failed sutdents")
                    _,failed = failed_students()
                    try:
                          failed_stds = "\n".join(map(str, failed))
                    except:
                             failed_stds = "No failed students"
                    print(failed_stds)
                    print(separator)

                else:
                    print("Statistics are currently unavailable. Missing data")
            case "10":
                 print("Top students")
                 verify,_,_,_,_,tops,_ = statistics(students)
                 if verify:
                     print(tops)
                     print(separator)
                 else:
                     print("Missing data")
                     print(separator)


            case "11":
                 
                 verify,_ = report_generator()
                 if verify:
                    print("Generating report...")
                    print(separator)
                    print("Report successfully generated.")
                    print(separator)
                 else:
                     print("Unable to generate report. Missing data...")
                     print(separator)

            case "12":
                 
                 verify,report = report_generator()
                 if verify:
                  
                  print(report)
                  print(separator)
                 else:
                     print("No report have been generated")
                     print(separator)
            case "13":
                 print("This process will delete all data saved")
                 print("1.Confirm")
                 print("2.Cancel")
                 print(separator)

                 option = input("Enter an option")

                 if option == "1":
                     print("Clearing all data...")
                     clear_data(students)
                     print("All data has been cleared")
                     print(separator)
                 else:
                     print("Data clearing process was canceled.")
                     print(separator)

             
        except ValueError:
            print(f"Enter numbers only")
            print(separator)
        except:
            print("Unable to run program...")
            print(separator)
        
if __name__ == "__main__":
    menu()
                        
    






    

        

