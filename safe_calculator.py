import operator
total_message = "Your total is ="
  
def sum (num1,num2): 
     return num1 + num2

def substract (num1,num2):
      return num1 - num2

def multiply (num1,num2): 
      return num1 * num2
  
def divide (num1,num2):
      return num1 / num2

def power (num1,num2):
      return  num1 ** num2

while True:

   print ("Options")
   print("1.Sum")
   print("2.Substract")
   print("3.Multiply")
   print("4.Divide")
   print("5.Power")
   print("6.Exit")


   options = input("Enter your selection")

   if options == "6":
        print("Closing calculator")
        break
        

   try:
     num1 = float(input("Enter first digit/s"))
     num2 = float(input("Enter second digit/s"))

     match options:
          case "1":
               print(f"{total_message}{sum(num1,num2)}")
          case "2":
               print(f"{total_message}{substract(num1,num2)}")
          case "3":
               print(f"{total_message}{multiply(num1,num2)}")
          case "4":
               print(f"{total_message}{divide(num1,num2)}")
          case "5":
               print(f"{total_message}{power(num1,num2)}")
          case _:
               print("Not a valid option")
   except ValueError:
        print("Enter a valid value (numbers)")
   except ZeroDivisionError:
        print("Come on man, they taught this in school. YOU CANNOT DIVIDE BY 0")
   except:
        print("Unable to complete operation")
   



           