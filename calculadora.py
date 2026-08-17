calc_history = []

shoertened = calc_history.append


def add ():

    calc = number_1 + number_2
    
    str_convertion = f"{str(number_1)} + {str(number_2)}"
    shoertened({"Calculus": "Addition", "Numbers": str_convertion, "Final_value": calc})
    print(calc)
    
def substract ():
   calc = number_1 - number_2
   str_convertion = f"{str(number_1)} - {str(number_2)}"
   shoertened({"Calculus": "Substraction", "Numbers": str_convertion, "Final_value": calc})
   print(calc)

def divide ():

   if number_2 == 0:
      print("Unable to devide by 0")
      
   else:
    
    calc = number_1 / number_2

    str_convertion = f"{str(number_1)} / {str(number_2)}"
    shoertened({"Calculus": "Division", "Numbers": str_convertion, "Final_value": calc})
    print(calc)

def multiply ():

   calc = number_1 * number_2

   str_convertion = f"{str(number_1)} x {str(number_2)}"
   shoertened({"Calculus": "Mutiplication", "Numbers": str_convertion, "Final_value": calc})
   print(calc)
def power ():

      calc = number_1 ** number_2

      str_convertion = f"{str(number_1)} ^ {str(number_2)}"
      shoertened({"Calculus": "Power", "Numbers": str_convertion, "Final_value": calc})
      print(calc)
      
def show_calc_history ():

   if not calc_history:

      print("No calculus have been made yet")

   else:

      for i,history in enumerate(calc_history, start=1):

         print(f"{i}.Calculus: {history["Calculus"]}")
         print(f"Values: {history["Numbers"]}")
         print(f"Final value: {history["Final_value"]}")
         print("-" * 8)
         print("-" * 8)
         
      
   
      

while True:

 options = input("What operation would u like to make. 1= add, 2= substract, 3 = divide, 4 = multiply, 5 = power, 6 = Show history, 7 = exit:")

 if options == "6":
    show_calc_history()
 elif options == "7":
    print("Closing menu...")
    break
 
 elif options != "1" and options !="2" and options !="3" and options!= "4" and options != "5":
    print(f"{options}, was not found in the options list")

 else:

  number_1 = float(input("First value"))
  number_2 = float(input("second value"))


 if options =="1":
    add()
    
 elif options =="2":
    substract()
    
 elif options =="3":
    divide()
    
 elif options =="4":
    multiply()
    
 elif options =="5":
    power()
    
