investment_amount = 0
while True:
    try:
        investment_amount = int(input("Enter the investment amount (greater than 0 and less than 50000): "))
        if 0 < investment_amount < 50001:
            break
        print("Invalid amount. Please enter a value between 1 and 50,000.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

interest_rate = 0
while True:
    try:
        interest_rate = int(input("Enter the interest rate (greater than 0 and less than 15): "))
        if 0 < interest_rate < 15:
            break
        print("Invalid rate. Please enter a value between 1 and 14.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

investment_years = 0
while True:
    try:
        investment_years = int(input("Enter the investment duration in years (greater than 0): "))
        if investment_years > 0:
            break
        print("Invalid duration. Please enter a value greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

total_months = investment_years * 12
monthly_rate_decimal = (interest_rate / 100) / 12
future_total = 0.0

for month in range(total_months):
    
    future_total += investment_amount
    
    interest_earned = future_total * monthly_rate_decimal
    
    future_total += interest_earned
    
    if (month + 1) % 12 == 0:
        current_year = (month + 1) // 12
        print(f"Year {current_year}: ${round(future_total, 2)}")

print("\n" +"*"*60)
print("Investment Duration:", investment_years, "years" )
print(f"Yearly Interest Rate: {interest_rate}%")
print(f"Monthly Investment Amount: ${investment_amount}")
print(f"Total Amount of Investment After Compounding: ${round(future_total, 2)}")
print("*"*60)
print("\nCompleted by, Shivang Dhamecha")
