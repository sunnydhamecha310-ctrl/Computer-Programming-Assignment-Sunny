first_name = input("\n\n""Enter your first name: ")
last_name = input("Enter your last name: ")
print("==================================")
current_year = int(input("\n""Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
print("==================================")


age = current_year - birth_year 
print("Hello, " + first_name + "  " + last_name + "!\n\n" + "You are " + str(age) + " years old this year.")
age += 1
print(f"Next year, you'll be {age} years old.")
print("==================================")
print("Completed by, Shivang Dhamecha")
