print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

compost_name = (name1 + name2).lower()
true_count = 0
true_count += compost_name.count("t")
true_count += compost_name.count("r")
true_count += compost_name.count("u")
true_count += compost_name.count("e")

love_count = 0
love_count += compost_name.count("l")
love_count += compost_name.count("o")
love_count += compost_name.count("v")
love_count += compost_name.count("e")

score = true_count * 10 + love_count

if score < 10 or score > 90:
  message = ", you go together like coke and mentos"
elif score > 40 and score < 50:
  message = ", you are alright together"
else:
  message = ""

print(f"Your score is {score}" + message + ".")


#percentage = str(true_count) + str(love_count)
#print(true_count, love_count)