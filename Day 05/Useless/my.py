#Write your code below this row 👇
import time
start_time = time.time()
for i in range (1, 10000000):
  if i % 3 and i % 5:
    resp = i
  else:
    resp = ""
    if not i % 3:
      resp += "Fizz"
    if not i % 5:
      resp += "Buzz"  
  print(resp)
print("--- %s seconds ---" % (time.time() - start_time))



    

