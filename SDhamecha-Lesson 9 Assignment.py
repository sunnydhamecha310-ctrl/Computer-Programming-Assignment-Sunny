#while True:
#    try:
#        userInput = input("Enter a number: ")
#        print("Obtained Input")
#        numberInput = float(userInput) 
        
#        if numberInput > 100:
#            raise ValueError("Invalid Entry, number must be below 100!")
        
#        break
#    except ValueError as e:
#        print(f"There was a value error, please enter a number! Error: {e}") 
#    except Exception as e:
#        print(f"An error has occurred! The error was: {e}")

#print("We made it out of the block")

def get_monthly_income():
    while True:
        try:
            userInput = input("Enter your total monthly income: ")
            income = float(userInput)
            if income < 0:
                raise ValueError("Income must be a positive value (cannot be below 0)!")
            return income
        except ValueError as e:
            print(f"There was a value error, please enter a number! Error: {e}")
        except Exception as e:
            print(f"An error has occurred! The error was: {e}")

def get_expenses():
    expenses = []
   
    while True:
        userInput = input("Enter expense amount (or 0 to stop):")
        if userInput.lower() == userInput == '0':
            break
        try:
            expense = float(userInput)
            if expense < 0:
                raise ValueError("Expense must be a positive value (cannot be below $0)!")
            expenses.append(expense)
        except ValueError as e:
            print(f"There was a value error, please enter a number! Error: {e}")
        except Exception as e:
            print(f"An error has occurred! The error was: {e}")
    return expenses

def main():
    print("Welcome to the Simple Budget Tracker")
    print("*" * 30)
    
    total_income = get_monthly_income()
    expense_list = get_expenses()
    
    total_expenses = sum(expense_list)
    remaining_budget = total_income - total_expenses
    
    
    
    print("\n" * 2)
    print("*" * 30)
    print("Budget Result:")
    
    print(f"Total Income: ${total_income:,.2f}")
    print(f"Total Expenses:       ${total_expenses:,.2f}")
    print(f"Remaining Budget:     ${remaining_budget:,.2f}")
    

    
    
    print("\nExpsense List")
    print("*" * 30)
    
    if not expense_list:
        print("No expenses were recorded.")
    else:
        i = 0
        while i < len(expense_list):
            expense = expense_list[i]
            expense_number = i + 1
            print(f"{expense_number:2}. ${expense:,.2f}")
            i += 1
    
  
    
    print ("*"* 50) 
    print("\nCompleted by Shivang Dhamecha")
    print ("*"* 50) 

if __name__ == "__main__":
    main()