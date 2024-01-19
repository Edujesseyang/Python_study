import random
import math


random_num = random.randint(0, 1000)
user_num = int(input("Enter a number:"))
print("The random num is:", random_num)
print("User num is:", user_num)
print("The different of those two numbers is:",
      round(math.fabs(random_num - user_num)))
