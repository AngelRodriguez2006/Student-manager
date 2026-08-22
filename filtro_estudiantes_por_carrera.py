students = list()

def add_student (name,career,age):

    return({"Name":name, "Career": career, "Age": age})

def show_students ():

    for i,student in enumerate(students, start=1):

        print(f"{i}.Name: {student["Name"]}")
        print(f"Career: {student["Career"]}")
        print(f"Age: {student["Age"]}")
        print("-" * 10)


def menu():

    while True:

        print("Options")
        print("1. Add student")
        print("2. Show students")

        options = input("Which option would u like to select. =")

        if options =="1":
            nam = input("Name of the student. =")
            car = input("Career of the student. =")
            ag = int(input("Age of the student"))

            result = add_student(nam,car,ag)
            students.append(result)

        if options =="2":

            show_students()
            

if __name__ == "__main__":
    menu()
