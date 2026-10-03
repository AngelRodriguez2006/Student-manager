from datetime import datetime
import os
separator = "-" * 10
source = "banking_history.txt"
source_balance = "balance.txt"

transaction_history = list()

balance = 0
archive_exists = False

#First three functions are all about data managing, saving, loading and deleting data.
def save_data(balance):

    if os.path.getsize(source) > 0:
             open(source,"w").close()

    with open(source, "a", encoding="utf-8") as f:
        for transaction in transaction_history:
          f.write(f"{transaction} \n")

    with open(source_balance,"w",encoding="utf-8") as f2:
        f2.write(str(balance))


def load_data():

    with open(source_balance,"r",encoding="utf-8") as f2:
     with open(source,"r",encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()], float(f2.read())
    
    

def clear_archive_data():

    transaction_history.clear()
    open(source_balance,"w",encoding="utf-8").close()
    open (source,"w",encoding="utf-8").close()

if os.path.exists(source) and os.path.exists(source_balance):

    archive_exists = True

    if os.path.getsize(source) > 0 and os.path.getsize(source_balance) > 0:

        print("Loading transaction history...")

        transaction_history,balance = load_data()
        
        print("Transaction history has been loaded.")
        print(separator)
    else:
        print("No archive data")
        print(separator)
else:
    clear_archive_data()

#This function fixes a bug in which when you pressed option "5" and deleted everything, the balance would remain
#Unless you re-started the program.
def ghost_balance_fix (balance):
    
    if archive_exists and os.path.getsize(source_balance) <= 0:
        return 0
    return balance

def deposit(amount,balance,date):
    

    if amount <= 0:
        return balance, f"The minimum deposit amount is 1$."
    else:
        balance += amount
        msg = f"{amount}- Has been deposited in the account"
        transaction_history.append(f"{msg}. date: {date}")
        save_data(balance)
        return balance,msg

def withdraw(amount,balance,date):

    if amount > balance:
        return balance, f"Insuficient funds. Current balance: {balance}"
    elif amount < 5:
        return balance, f"Minimum withdraw amount is 5$"

    else:
        balance -= amount
        msg = f"Withdrawal of -{amount}- successfull"
        transaction_history.append(str(f"{msg}. date: {date}"))
        save_data(balance)
        return balance,msg

print("Loading app...")


def menu(balance):
    
    while True:

        balance = ghost_balance_fix(balance)

        date = str(datetime.today())
        print("Options")
        print("1.Check balance")
        print("2.Make deposit")
        print("3.Withdraw")
        print("4.Show transaction history")
        print("5.Delete history")
        print("6.Exit")
        print(separator)

        options = input("Enter an option. ")

        if options == "6":
            print("Closing app...")
            break

        try:
         match options:
                case "1":
                                           
                    print(f"Your current balance: {balance}")
                    print(separator)
                case "2":
                    amount_to_deposit = float(input("How much would u like to deposit?"))
                    balance,msg = deposit(amount_to_deposit,balance,date)
                    print(msg)
                    print(separator)
                    
                case "3":
                    amount_to_withdraw = float(input("Balance to withdraw = "))
                    balance,msg = withdraw(amount_to_withdraw,balance,date)
                    print(msg)
                    print(separator)
                    
                case "4":
                    if transaction_history:
                     print("Transaction History:")
                     print(separator)
                     for i,transaction in enumerate(transaction_history,start=1):
                         print(f"{i}.{transaction}")
                         print(separator)
                    else:
                        print("History is empty.")
                        print(separator)

                case "5":
                    clear_archive_data()
                    print("All data has been cleared")
                    print(separator)
                 
                case _:

                    print(f"{options}- Is not among the options. Try again.")
                    print(separator)

        except ValueError:
            print("Please enter numbers only.")
            print(separator)
        except:
            print("Fatal error 203. Try again please.")
            print(separator)
        
if __name__ == "__main__":
    
    menu(balance)           