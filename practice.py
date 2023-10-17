import math
import random
from collections import namedtuple

# # -----------------problem 1-----------------

# year_wage = int(input("Enter yearly wage:"))

# weekly_wage = year_wage / 52
# print("The weekly wage is :", weekly_wage)

# daily_wage = weekly_wage / 5
# print("The daily_wage is :", daily_wage)

# hourly_wage = daily_wage / 8
# print("The hourly_wage is:", hourly_wage)

# # -----------------problem 2-----------------

# weekly_wage = math.ceil(year_wage / 52)
# print("The round off weekly wage is:", weekly_wage)

# daily_wage = math.ceil(weekly_wage / 5)
# print("The round off daily wage is:", daily_wage)

# hourly_wage = math.ceil(daily_wage / 8)
# print("The round off hourly wage is:", hourly_wage)

# # -----------------problem 3-----------------

# side1 = int(input("Enter the first side length:"))
# side2 = int(input("Enter the second side length:"))

# hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)

# print("The hypotenuse of the triangle is:", f'{hypotenuse:.0f}')

# # -----------------problem 4------------------

# date = int(input("Enter a date in format of MMDDYYYY:"))
# month = date // 1000000
# year = date % 10000
# day = date // 10000 % 100
# print("The month is:", month)
# print("The year is:", year)
# print("The day is:", day)

# # ------------------problem 5-------------------

# random_num = random.randint(0, 1000)
# user_num = int(input("Enter a number:"))
# print("The random num is:", random_num)
# print("User num is:", user_num)
# print("The different of those two numbers is:", round(math.fabs(random_num - user_num)))


# # -------------------try out----------------------
# input_num = float(input("Enter a float number:"))

# print("Round off the number:" ,round(input_num))

# roundOf_2 = round(input_num, 2)

# print("Round it off 2 decimal:", roundOf_2)

# -------This is tuple-------------
# sth = (1, 2, 3, 4, 5)
# x = len(sth) + sth[0]

# print("len + first is:", x )
# print(sth)

# ----------This is namedtuple------------
# my_class = namedtuple('my_cass', ['first_class', 'second_class', 'third_class'])

# today_class = my_class('ENG10', 'Math1A', 'CIS40')

# print(today_class)

# --------------------------------------------

# score = {"math": 100, 'english':53, 'eng10':34}
# print(score['math'])
# if score['math'] != 100:
#     print("Stupid")
# else:
#     print("good job")

# -------------------------EX 1 cpt 3--------------------
# name = str(input("Enter a name: "))

# len = len(name)

# if len % 3 == 0 :
#     print("city name: ", name)
# else:
#     print(name[0], name[-1])

# print("The length is :", len)


# ---------------------EX 2---------------------------
# names0 = str(input("Enter 1 name: "))
# names1 = str(input("Enter 2 name: "))
# names2 = str(input("Enter 3 name: "))
# names3 = str(input("Enter 4 name: "))
# names4 = str(input("Enter 5 name: "))
# names = [names0, names1, names2, names3, names4]

# print(names)
# tem_name = names0
# if names0 < names1:
#     tem_name = names0
# if names1 < names2:
#     tem_name= names3
# print(tem_name)  = names1
# if names2 < names3:
#     tem_name = names2
# if names3 < names4:
#     tem_name 

# ---------------------EX 3---------------
# temp = {}
# temp['San F'] = 50
# temp["LA"] = 54
# temp['nyc'] = 34

# print(temp)
# del temp['LA']
# print(temp)

# temp['nyc'] = 54
# print(temp)

#____________________________EX4____________

# age = int(input("Enter your age: "))
# ht = int(input("Enter your height in inches: "))

# if age < 18:
#     if ht < 50:
#         print("You cannot ride")
#     else:
#         print("you can ride with parents")
# else:
#     print("you can ride")

# ______________loop_______________
# Flip a number:
num = int(input("Enter a number:"))
num2 = 0

while num > 0:
    num2 = num2 * 10
    num2 = (num % 10) + num2
    num = num // 10
   
print(num2)

#_________