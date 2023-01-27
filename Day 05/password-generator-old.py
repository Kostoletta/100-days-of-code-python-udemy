import random
print("welcome to the Pypassword generator!")

letters = "qwertyuiopasdfghjklzxcvbnm"
letters += letters.upper()

symbols = "!\"£$%&/()=\\"

numbers = "1234567890"

n_letters = int(input("How many letters would you like in your password?"))
n_symbols = int(input("How many symbols would you like?"))
n_numbers = int(input("How many numbers would you like?"))

password = []

for i in range(n_letters):
    password.append(random.choice(letters))
for i in range(n_symbols):
    password.append(random.choice(symbols))
for i in range(n_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
str_password = ""
for i in password:
    str_password += i

print(f"Your strong password is: {str_password}")
