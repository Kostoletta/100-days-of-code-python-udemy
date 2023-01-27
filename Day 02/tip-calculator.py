print("Welcome to the tip calculator!")
total_bill = float(input("What was teh total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_number = int(input("How many people to split the bill? "))

result = total_bill / people_number
result += (result / 100) * tip_percentage

print(f"Each person should pay: ${result}")

