#Write your code below this row 👇
import time
start_time = time.time()
for number in range(1, 10000000):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
print("--- %s seconds ---" % (time.time() - start_time))



    

