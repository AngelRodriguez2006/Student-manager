
balance = 10000

def deposit (amount):
     global balance
     
     if amount > 0:
      balance += amount
      return f"{amount}- has been added. current balance: {balance}"
     else:
          return f"You cannot deposit -{amount}- invalid amount, can only make deposits starting from 1$"

def withdraw (amount):
     global balance
     if amount <  5:
          return f"You can only withdraw 5$ or more"
     elif amount > balance:
          return f"Unable to withdraw -{amount}. Your current balance is: {balance}"
     
     else:
          balance -= amount
          return f"You have successfully withdrawn -{amount}"
     
print("Loading ATM...")
print("Fully loaded")

while True:


     print("Options")
     print("1.Check balance")
     print("2.Deposit")
     print("3.Withdraw")
     print("4.Exit")

     options = input("Enter an option")

     if options == "4":
          print("Closing ATM...")
          break

     try:

      match options:
               case "1":
                    print(f"Your current balance is = {balance}")
               case "2":
                    amount_to_deposit = float(input("Enter balance. "))
                    print(deposit(amount_to_deposit))
               case "3":
                    amount_to_withdraw = float(input("Enter balance. "))
                    print(withdraw(amount_to_withdraw))
               case _:
                    print("Enter one of the options above")


     except ValueError:
         print("You can only enter numbers")
     except:
         print("Error #202. Try again")

     
                


     