

print("Welcome to the tip calculator!")
bill_total = float(input("What was the total bill? $"))
tip_percentage = int(
    input("How much tip would you like to give? 10, 12, or 15? "))
people_number = int(
    input("How many people to split the bill? "))
bill_per_person = bill_total/people_number
result = bill_per_person + ((bill_per_person / 100) * tip_percentage)
print(f"Each person should pay: ${'{:.2f}'.format(result)}")
