import math
import random
from collections import namedtuple
from typing import Any

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
# my_class = namedtuple('my_class', ['first_class', 'second_class', 'third_class'])

# today_class = my_class('ENG10', 'Math1A', 'CIS40')

# print(today_class)
# --------------------------------------------

# score = {"math": 100, 'english':53, 'eng10':34}
# print(score['math'])
# if score['math'] != 100:
#     print("Stupid")
# else:
#     print("good job")

# _____________EX 1 cpt 3_____________________
# name = str(input("Enter a name: "))

# len = len(name)

# if len % 3 == 0 :
#     print("city name: ", name)
# else:
#     print(name[0], name[-1])

# print("The length is :", len)


# __________________EX 2__________________
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

# ___________EX 3____________________
# temp = {}
# temp['San F'] = 50
# temp["LA"] = 54
# temp['nyc'] = 34

# print(temp)
# del temp['LA']
# print(temp)

# temp['nyc'] = 54
# print(temp)

# ____________________________EX4____________

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
# num = int(input("Enter a number:"))
# num2 = 0

# while num > 0:
#     num2 = num2 * 10
#     num2 = (num % 10) + num2
#     num = num // 10

# print(num2)

# _________GCD__________
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))
# gcd = 0
# while num1 != num2:
#     if num1 > num2:
#         num1 = num1 - num2
#     else:
#         num2 = num2 - num1
#     gcd = num1

# print(gcd)
# ----The program above is a tool to look for the greatest common denominator.--------
# ----num1 and num2 are user input nums. gcg is greatest common denominator of both nums.-------

# ___________ 模拟机器人聊天软件___________
# print("欢迎使用机器人聊天1.0")
# print("使用指南: 你可以问我任何问题, 我会知无不言言无不尽! 输入再见 '886' 对话.")
# print("_______________________________________________")
# print("你好, 请问有什么需要帮助的吗?")

# ipt = input()
# while input != 886:
#     num = random.randint(0, 33)
#     if num == 1:
#         ipt = input("谢谢你的提问, 你喜欢吃辣吗?\n")
#     elif num == 2:
#         ipt = input("哦, 这都不知道是吗? 真了不起! 你觉得呢?\n")
#     elif num == 3:
#         ipt = input("啊? 我不太清楚, 真的不知道吗?\n")
#     elif num == 4:
#         ipt = input("真不错! 为你高兴呢? 还有什么问题?\n")
#     elif num == 5:
#         ipt = input("呵呵, 真喜欢跟你聊天! \n")
#     elif num == 6:
#         ipt = input("啊? 我不知道耶, 换个话题吧?\n")
#     elif num == 7:
#         ipt = input("真有你的, 我也不知道, 还有吗?\n")
#     elif num == 8:
#         ipt = input("真好玩啊, 你来告诉我一些吧!\n")
#     elif num == 9:
#         ipt = input("哈哈, 太棒了! 然后呢?\n")
#     elif num == 10:
#         ipt = input("啊? 为什么呢?\n")
#     elif num == 11:
#         ipt = input("So? 你想表达什么?\n")
#     elif num == 12:
#         ipt = input("快说些别的把! \n")
#     elif num == 13:
#         ipt = input("哎呀! 可真有你的! 这都不懂?\n")
#     elif num == 14:
#         ipt = input("不然呢! 你还能怎样?\n")
#     elif num == 15:
#         ipt = input("真是恐怖! 还有什么?\n")
#     elif num == 16:
#         ipt = input("啊? 这个话题....不太好吧?\n")
#     elif num == 17:
#         ipt = input("哈哈? 可说呢? 真是的! \n")
#     elif num == 18:
#         ipt = input("Really? 简直了! 继续. \n")
#     elif num == 19:
#         ipt = input("是吗? 快讲讲, 快讲讲!\n")
#     elif num == 20:
#         ipt = input("哎! 那有什么办法啊?\n")
#     elif num == 21:
#         ipt = input("去去去, 小孩子懂得什么?\n")
#     elif num == 22:
#         ipt = input("这个事情可不好说.\n")
#     elif num == 23:
#         ipt = input("哎, 连爱因斯坦恐怖也搞不清楚! \n")
#     elif num == 24:
#         ipt = input("不能比这个问题还有趣了吧? \n")
#     elif num == 25:
#         ipt = input("那个...啊?  你在说什么?\n")
#     elif num == 26:
#         ipt = input("我去, 不是吧, 这也问? 太夸张了啊!\n")
#     elif num == 27:
#         ipt = input("那是! 你也不想想, 怎么可能?\n")
#     elif num == 28:
#         ipt = input("你不要这样说好不好?\n")
#     elif num == 29:
#         ipt = input("话可不能这么说.\n")
#     elif num == 30:
#         ipt = input("诶? 何出此言啊? \n")
#     elif num == 31:
#         ipt = input("自古有云: 云什么来着? \n")
#     elif num == 32:
#         ipt = input("你再好好想想吧?\n")
#     elif num == 33:
#         ipt = input("要说对吧, 也不完全对, 不对吧? 又似乎有道理! \n")
#     else:
#         ipt = input("你这句话说的, 我都不知道怎么反驳! \n")

# print("跟你聊天真开心, 再见!")
# -------------------------------

# ------------input nums to get the avg---------------
#  || usage: keep input nums, when finish, input 0. ||
# ----------------------------------------------------

# ipt_current = int(input("Enter your numbers: "))
# sum_nums = 0
# ipt_count = 0

# while  ipt_current != 0:
#     sum_nums = sum_nums + ipt_current
#     ipt_count += 1
#     ipt_current = int(input("Keep entering, enter 0 to start calculating: "))
# print("The average of those numbers is:", sum_nums / ipt_count)
# ---------输入数字 最后output这些数字的平均值.---------

# --------try out the for loop------
# str = "abcdefg"

# for a in str:
#     print(a)

# Here "a" is a temp name of the variable to represent every char in the string.

# lst = [0, 1, 2, 3, 4, 5, 6]

# for i in lst:
#     j = i + 1

#     print(f'{i} is the number {j} - 1')
# Here the variable "i" is a temp name to represent the index of this list.

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5
# }
# for name in dict:
#     print(f'{name} : {dict[name]}')
# Here the variable name is representing the name of every object in the dict. dict[name] is the value assigned to the name.

# str = " Hi, how are you doing?"
# new_str = ""
# for char in str:
#     new_str = new_str + char + "_"

# print(new_str)
# ----------------------------------------

# -------- this is find trig----------------------------
# a = float(input("Enter the a side:"))
# b = float(input("Enter the b side:"))

# B = float(input("Enter the angle B: "))

# Br = (math.radians(B))
# sin_Br = math.sin(Br)
# sin_Ar = sin_Br / b * a
# Ar = math.asin(sin_Ar)
# Ad = math.degrees(Ar)

# Cd = 180 - B - Ad

# Cr = math.radians(Cd)
# sin_Cr = math.sin(Cr)

# c = sin_Cr / (sin_Br / b)

# print(f'A is {round(Ad, 2)} in degree')
# print(f'C is {round(Cd, 2)} in degree')
# print(f'The side c is {round(c, 2)}')
# ----------------above not work well, but close--------

# ---------- calculate Resistance of a circuit---------
# Rt = 0
# ipt = 1
# while ipt != 0:
#     print("Enter 0 to start calculate!")
#     R = float(input("Enter the resistance R: "))
#     ipt = R
#     bool = input("Is is series or parallel, enter 's' / 'p': ")
#     if bool == "s":
#         Rt = Rt + R
#     else:
#         R = R + (1 / R)
#         Rt = 1 / R
# print(f'The total resistance of the circuit is {Rt}')
# ------------------------------------------------------

# -------------above is not working good-------------
# lst = [1,2,3,4,5,6]

# for num in reversed(lst):
#     print(f'The num in reversed order is {num}')
# ----------- -This is the reversed check------------

# --------------.split or . add--for input----------
# lst = input("Enter stuff:").split()  #-----------------------------Good--------------------

# for item in lst:
#     print(item)
# ---------------------------------------------------

# ---------------------------------------------------
# string = "How can I help you?"
# for word in string.split(" "):   # ---- split 的另一个用法---------
#     print(word)
# ----------------------------------------

# -------split 用于将 string 的每一个词变成 list 中的各个项-------
# str ="Yo! what's up! How are yo doing?"
# lst = str.split(" ", 2)
# print(lst)
# -------------------------------------------------------------

# ------------save input to dist------------------------
# print("usage: enter item name, enter item value, enter " " to end entering,  then print dict in 'item_name : item_value' formate.")
# dict = {}
# ipt = ""

# while ipt != " ":
#     name = input("Enter item name:")
#     ipt = name
#     if ipt == " ":
#         break


#     value = input("Enter item value: ")
#     dict[name] = value

#  # print("Check:",dict) --use this to check dict

# for item in dict:
#     print(f'{item} : {dict[item]}')
# ---------------------------above is good example to save inputs into a dict---------------------

# -------------------银行倍率计算器--------------------------------
# interest = float(input("Enter the interest rate:"))
# amount = float(input("How much money do you want to put in:"))
# year = int(input("How many years do you want to save: "))

# for year in range(year): # 这里的第一个year和第二个year不一样, 第一个是方程里的临时名字变量, 第二个是用户输入的变量
#     print(f'In the year {year}, You have {round(amount, 2)}')
#     amount = amount + (amount * interest)
# ---------------------------------------------------------------

# -------------------range() 的用法------------------------------
# lst = range(10, 50, 5)
# for num in lst:
#     print(num)
# ----创造一个从10到50的每项增加5的list------------------------------

# --------------class practice--------
# nums = []
# for i in range(5):
#     nums.append(int(input("Enter a number:")))

# print(nums)
# total = 0
# count = 0
# for num in nums:
#     total += num
#     count += 1
# print(f'The sum is: {total}, The avg is: {round((total / count), 2)}')
# ---------------------------------------

# -------------class practice------------
# num = random.randint(0, 100)
# user_ipt = int(input("Guess a number:  "))
# tries = 7
# while user_ipt != num or tries > 0:

#     if tries > 0:
#         if user_ipt < num:
#             print("Guess higher next time!")
#         elif user_ipt == num:
#             print(f'YOU WIN, the number is {num}')
#             break
#         else:
#             print("Guess lower next time!")
#     else:
#         print(f'You lost, the right number is {num}')
#         break
#     tries -= 1
#     user_ipt = int(input("Guess a number: "))
#     print(f'You have {tries} more chances to guess!')
# -----------------------------------------------------------

# ----------------------class practice-----------------------
# for num in range(250, 751, 50):
#     print(num)
# -----------------------------------------------------------

# ------------------class practice--------------------------------
# || Usage: input num of students, input name and scores pairs, ||
# ||       Program will calculate avg score, list all paris,    ||
# ||       find and print the hightest score and student name.  ||
# ----------------------------------------------------------------
# scores = {}
# total = 0
# students_count = int(input("How many students: "))
# for name in range(students_count):
#     name = input("Enter your student name: ")
#     scores[name] = int(input("Enter your score: "))
#     total += scores[name]

# for name in scores:
#     print(f'{name} : {scores[name]}')

# print(f'Avg is {round((total/students_count), 2)}')

# hightest = 0
# for name in scores:
#     if scores[name] > hightest:
#         hightest = scores[name]
# for name in scores:
#     if scores[name] == hightest:
#         print(f'The hightest score is "{name}" : {hightest}. ')
#         break
# ---------------------------------------------------------------

# ---------------------双 item 的 for loop----------------------
# lst = [1, 2, 3, 4, 5, 6]
# for (index, value) in enumerate(lst):                                                               ???
#     print(f'{index} : {lst[index]}')
# ---------用 enumerate() 方程来实现 显示 index 和 value ----------

# ----------------trig calculator---------------
# a = float(input("Enter a side: "))
# b = float(input("Enter b side: "))
# c = float(input("Enter c side: "))
# cos_A = ((c ** 2) + (b ** 2) - (a ** 2)) / (2 * b * c)
# cos_B = ((c ** 2) + (a ** 2) - (b ** 2)) / (2 * a * c)
# cos_C = ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b)
# A_d = math.degrees(math.acos(cos_A))
# B_d = math.degrees(math.acos(cos_B))
# C_d = math.degrees(math.acos(cos_C))

# print(f'The 3 angles are :\n A : {A_d} \n B : {B_d} \n C : {C_d}')
# ----------------------------------------------------------

# -------------moment and force ------------------
# || Usage: enter f1 and d1, select what answers do you need. ||
# ------------------------------------------------
# print ("Usage: enter f1 and d1, select what answers do you need. ")
# f_1 = float(input("Enter the force 1: "))
# d_1 = float(input("Enter the distance between force 1 and pivoted point: "))
# bool = input("You need to find the force 2 or the distance? f/d :")
# if bool == "f":
#     d_2 = float(input("What is the distance of force 2 to the pivoted point: "))
#     ans = (f_1 * d_1) / d_2
#     print(f'The force 2 is : {ans}')
# elif bool == "d":
#     f_2 = float(input("What is the force 2: "))
#     ans = (f_1 * d_1) / f_2
#     print(f'The distance between the point and force 2 is : {ans}')
# ------------------------------------------------------------------------

# ----------------------Midterm------------------
# ipt = input("Enter the name of the city:")
# i = 0
# for char in ipt:
#     if char != " ":
#         i += 1
# if i % 2 == 0:
#     print("The name is even.")
# else:
#     print("The name is odd.")
# #-----------------------------------------------

# ----------------------Mt 2-----------------------
# lst = []
# while ipt != -1:
#     ipt = (input("Enter ints:"))
#     lst.append(ipt)


# max_num = max(lst)
# second_max = -1
# for num in lst:
#     if num > second_max and num != max_num :
#         second_max_num = num
# if second_max == -1:
#     second_max = max_num
# print("The second max is", second_max)
# ------------------------------------------

# ---------------MT 3-----------------
# phone_num = input("Enter a phone number: ")
# digits = {
#     '0' : 0,
#     '1' : 0,
#     '2' : 0,
#     '3' : 0,
#     '4' : 0,
#     '5' : 0,
#     '6' : 0,
#     '7' : 0,
#     '8' : 0,
#     '9' : 0
#     }

# for digit in phone_num:
#     if digit != "-":
#         digits[digit] += 1
# print(digits)
# --------------------------------------------

# ----------------Mt 4------------------------
# grade = int(input("Enter your grade: "))
# if grade >= 1 and grade <= 5:
#     print("Elementary school.")
# elif grade >= 6 and grade <= 8:
#     print("Middle school.")
# elif grade >= 9 and grade <= 12:
#     print("High school.")
# --------------------------------------------

# --------------------------------------------
# 5. You have the following list of 5 strings:
# ["the", "word", "test", "a", "question"]. Create a new
# list with these words sorted in order of string length.
# If two words have the same length, the order can be
# either way (i.e. with "word" and "test"). You may use any
# string or list function to complete this problem.
# ---------------------------------
# # Solution:
# lst = ["the", "word", "test", "a", "question"]   # test body
# new_lst = [] # result list
# longest = 0
# i = 0
# temp = ""
# count = len(lst)
# for word in lst:    # find the longest word
#     if len(word) > longest:
#         longest = len(word)
# shortest = longest        # make the temp shortest to be the longest

# while i < count:       # loop len(lst) times
#     shortest = longest   # re-set  temp shortest every loop
#     temp = ""           # re-set temp word every loop
#     for word in lst:        # find the shortest word
#         if len(word) <= shortest:
#             temp = word    # assign temp to be the shortest word
#             shortest = len(word)    # re-assign the length of the shortest

#     new_lst.append(temp)   # add temp to result list

#     for word in lst:      # loop list body find and remove the shortest word
#         if  word == temp:
#             lst.remove(word)
#     i += 1

# print(new_lst)   # print result
# --------------------------------------------------------------------------

# =================================================
# 6. Print out all of the numbers from -1000 to 1000 (inclusive, exclusive) in groups of 4.
# ---------------------------------------------------
# for nums in range(-1000, 1001, 4):
#     print(nums)
# ===================================================

# ===========================================================
# Fremont: 59
# Sunnyvale: 60
# Saratoga: 56
# San Jose: 61
# Campbell: 59
# Los Altos: 58
# Put these into a dictionary and print out the city with the highest and lowest temperatures. If there's a tie, just pick one city
# Solution: --------------------------------------------------
# city_temps = {
#     'Fremont' : 59,
#     'Sunnyvale' : 60,
#     'Saratoga' : 56,
#     'San Jose' : 61,
#     'Campbell' : 59,
#     'Los Altos' : 58,
# }
# hightest = 0
# hi_city = ""
# for name in city_temps:
#     if city_temps[name] > hightest:
#         hightest = city_temps[name]
#         hi_city = name
# lowest = hightest
# lo_city = ""
# for name in city_temps:
#     if city_temps[name] < lowest:
#         lowest = city_temps[name]
#         lo_city = name
# print(f'The hottest city is {hi_city}, the temperature is {hightest}.')
# print(f'The coldest city is {lo_city}, the temperature is {lowest}.')
# ====================================================================================

# =====================================================================================
# 8. Ask user to keep entering names until user is finished.
# Put these names into a list. Print out the longest and shortest names. Spaces count as characters.
# Solution: ---------------------------------------------------------------------------
# name_list = []
# user_ipt = " "

# while user_ipt != "":
#     user_ipt = input("Enter a name, double press enter to finish entering: ")
#     name_list.append(user_ipt)

# name_list.pop(len(name_list) - 1)

# longest = 0
# longest_name = ""
# for name in name_list:
#     if len(name) > longest:
#         longest_name = name
#         longest = len(name)
# shortest = longest
# shortest_name = ""
# for name in name_list:
#     if len(name) < shortest:
#         shortest_name = name
#         shortest = len(name)
# print(f'The longest name is {longest_name}, It has {longest} characters.')
# print(f'The shortest name is {shortest_name}, It has {shortest} characters.')
# ===============================================================================

# ==========================================================================
# 9. Ask user to enter number of years of work experience.
# Print out the following message based on the answer.
# All ranges are inclusive.
# 0-2 years: "New grad"
# 3-5 years: "Mid"
# 6-10 years: "Senior"
# 11 or more years: "Leadership"
# solution: ------
# user_years = int(input("Enter your years of working experience: "))
# if user_years > 0:
#     if user_years < 2:
#         print("New grad")
#     elif user_years >= 3 and user_years <= 5:
#         print("Mid")
#     elif user_years >= 6 and user_years <= 10:
#         print("Senior")
#     elif user_years >= 11:
#         print("Leadership")
# ===============================================================

# ===============================================================
# Ask user to enter a number between 1 and 10.
# Keep prompting the user to guess until the user is correct.
# Once the user is correct, the user wins the game.
# You may choose the winning number and hard code it.
# Print when the user won and how many tries it took.
# Solution: -----------
# answer = random.randint(1, 10)
# user_ipt = int(input("Guess a number between 1 and 10: "))
# tries = 1
# while user_ipt != answer:
#     user_ipt = int(input("WRONG! Try again: "))
#     tries += 1
# else:
#     print(f'You Win, You had the right number in {tries} tries.')
# ================================================================
# ===================================================
#
# lst = ["the", "word", "test", "a", "question"]
# new_lst = []
# longest = 0
# i = 0
# temp = ""
# index = 0
# while i < len(lst):
#     for word in lst:
#         if len(word) > longest:
#             longest = len(word)
#             temp = word
#             index = lst.index(word)
#     i += 1
#     new_lst.append(temp)
#     # lst.pop(index)
# print(longest)
# print(temp)
# print(new_lst)
# =========================================

# =========================================
# Write a function that calculates the diameter of a circle given the circle's area.
# ---------------------------------------
# def diam (area):
#     return 2 * math.sqrt(area / math.pi)
# area = 15
# print(f'Area is {area}, diameter is {round(diam(area), 2)}')
# =================================================

# ==================================================
# Create a function that asks student for first and last name (separately), student ID,
# classes that get read into a list, and expected graduation year. Create another
# function that prints out the information in this order:
# --------------------------------------
# def lst(name, ID, classes, year):
#     list_name = {
#     'name' : input("Enter your name: "),
#     'ID' : input("Enter your ID: "),
#     'classes' : input("Enter your class: "),
#     'year' : input("Enter your graduation year: ")
#     }
#     return list_name


# def prt(name):
#     print(name)

# student = lst("yang", 124, "python", 2024)
# prt(student)
# ====================================================

# ==============================================
# Prompt the user for a list of numbers. Create a function that takes the list
# in and returns a 2-element list back with a sum of the odd numbers in the
# input list and a sum of the even numbers in the input list.
# -----------------------------------------
# num_list = []
# ipt = 0
# while ipt != "":
#     ipt = input("Enter a number: ")
#     if ipt != "":
#       num_list.append(int(ipt))

# def sum(my_list):
#     result = []
#     sum_odd = 0
#     sum_even = 0
#     for num in my_list:
#         if num % 2 == 0:
#             sum_even += num
#         else:
#             sum_odd += num
#     result = [sum_even, sum_odd]
#     return result

# answer = sum(num_list)
# print(f'Sum of odd is {answer[1]}')
# print(f'Sum of even is {answer[0]}')
# ================================================

# ====================================================
# print pics
# -------------------------
# def cowboy_hat():
#     print("    ____")
#     print("   |    |")
#     print("   |====|  ")
#     print("~~~~~~~~~~~~")
# def magic_hat():
#     print("     )(")
#     print("    /  \ ")
#     print("   /... \ ")
#     print("~~~~~~~~~~~~")
# def man_face(type_hat):
#     type_hat()
#     print(" q  O  O  p")
#     print("  \  ||  /  ")
#     print("   \ ^^ /")
#     print("    \__/")
# def girl_face(type_hat):
#     type_hat()
#     print("|q|^O  O^|p|")
#     print("||\  __  /||")
#     print("|| \____/ ||")
# def body(type_hat, type_face):
#     type_face(type_hat)
#     print("   __||__ ")
#     print("  /  \/  \ ")
#     print(" /|  88  |\ ")
#     print("| |  88  | | ")
#     print(" \|__88__|/")
#     print("  |  __  |  ")
#     print("  |  ||  | ")
#     print("  |  ||  |")
#     print("  |__||__|")
#     print(" (__/  \__)")

# print("print menu: ")
# print("1: cowboy hat, 2: magic hat")
# hat = int(input("Enter hat number: "))
# print("1: man face, 2: girl face")
# face = int(input("Enter face number: "))
# if hat == 1 and face == 1:
#     body(cowboy_hat, man_face)
# elif hat == 1 and face == 2:
#     body(cowboy_hat, girl_face)
# elif hat == 2 and face == 1:
#     body(magic_hat, man_face)
# elif hat == 2 and face == 2:
#     body(magic_hat, girl_face)
# else:
#     print("Please enter the right number. ")
# =====================================

# =====================================
# Arbitrary argument list
# *args
# -----------------------
# def add_up(x, y, *more):
#     result = x + y
#     for num in more:
#         result += num
#     return result

# print(add_up(1, 3, 4, 5, 6))
# -------------------------
# **kwargs
# ---------------------
# def info(name, **info):
#     print(f'{name}:')
#     for category, context in info.items():
#         print(f'{category} is {context}')
# info("Jesse", age=35, gender="male", wife="Chloe", favorite_food="noodle")
# ====================================================

# ====================================
# function that return multiple values
# # ----------------------
# def circle_calcs(r):
#     A = 3.141592653 * r * r
#     P = 2 * 3.141592653 * r
#     return A, P
# given_radius = 5.0
# units = "cm"
# area, perimeter = circle_calcs(given_radius)
# print(f'A circle with radius is {given_radius}{units}, the area is {round(area, 2)}{units}^2, the perimeter is {round(perimeter, 2)}{units}. ')
# =====================================================

# ===========================================
# try out:
# prompt user to enter a number
# only collect numbers in the string
# make a new string for all numbers
# re-type the string to be int.
# return if result in 1-20.
# --------------------------------------------
# def get_input():
#     result = ""
#     vail = False
#     while vail == False:
#         get_input = input("Enter: ")
#         for char in get_input:
#             if 48 <= ord(char) <= 57:
#                 result = result + char
#                 vail = True
#     result = int(result)
#     while 1 <= result <= 20:
#         return result
#     else:
#         print("enter vail number")
# x = get_input()
# print(x)
# ============================================

# ============================================
# guessing word game:
# -----------------------------------------
# '''create a word list and random out one word to be the target word.'''
# word_list = ["fox", "bee", "box", "cat", "dog", 'pig', 'owl', 'rat', 'bat', 'elk', 'ape', 'cow']
# word_num = random.randint(0, 12)
# target_word = word_list[word_num]
# final_answer = word_list[word_num]
# '''replace the target word to be ------ format'''
# hide_target = "-" * len(target_word)
# chances = 10

# def get_user_input():
#     ipt = input("Guess a character may in the word: ")
#     return ipt[0]

# user_input = '' # create a var for user input
# '''main loop: get user input, check  input and replace with hind_target word.'''
# while chances > 0:
#     user_input = get_user_input()
#     for index in range(len(target_word)):   # loop to check if user_input is in the target
#         if user_input == target_word[index]:    # if match, switch user input with hide_word same spot
#             hide_target = hide_target[: index] + user_input + hide_target[index + 1 :]
#             target_word = target_word[: index] + "-" + target_word[index + 1 : ]
#     print(hide_target)  # print new hide word
#     chances -= 1
#     if chances > 1:  # count down chances
#         print(f'You have {chances} chances left.')
#     elif chances == 1:
#         print(f'You have {chances} chance left.')
#     else:
#         print("No more chance!")
#     if hide_target.find("-") == -1:  # if all "-" got replaced by user input chars. break loop & print win statement
#         print("You win!")
#         break
# else:
#     print(f'You lose! Right answer is "{final_answer}"')  # if loop had completed, means no more chance to guess, print lose statement

# ==========================================================================

# ==========================================================================
#  Prompt user for a sentence about programming. Slice the string for every other character.
# Then, count the  number of vowels and consonants (punctuation and spaces don't count) and print those values out.
# ------------------------------------
# string = input("Enter a sentence:")
# string = string[: : 2]
# vowels_count = 0
# consonants_count = 0

# string = string.lower()
# for char in string:
#     if char != " ":
#         if char == "a" or "e" or "i" or "o" or "u":
#             vowels_count += 1
#         elif char.isalpha() == True:
#             consonants_count += 1

# print(f'There is {vowels_count} vowels, and {consonants_count} consonants.' )
# print(string)
# ======================================================

# =======================================================
# Prompt user for another sentence about programming.
# Then ask user to enter in a word.
# Using string methods to check if the word is in the sentence.
# -----------------------------------------
# string = input("Enter a sentence: ")
# word = input("Enter a word: ")
# if string.find(word) == -1:
#     print(f'There is no word: {word} in the sentence. ')
# else:
#     print("The word is in the sentence.")
# ========================================================

# =======================================================
# Use a while loop to keep prompting user for more positive integers until user types -1.
# ----------------------------------------------------------
# num = int(input("Enter a positive int: "))
# num_list = [num]
# while True:
#     try:
#         num = int(input("Enter a positive int: "))
#         num_list.append(num)
#     except ValueError:
#         break

# dict = {}

# for num in num_list:
#     if not num in dict:
#         dict[num] = 0

# for num in num_list:
#     if num in dict:
#         dict[num] += 1
# print(dict)
# ===========================================================

#     ========================
#    ||                      ||
#    ||       GOOD JOB       ||
#    ||                      ||
#     ========================

#   恭喜你突破了1000行 python 练习.
#     请继续努力, 争取更大的进步.
#            加油!!!

# ======================================================

# ===============================================
# Enter numbers, get the avg of all numbers
# ----------------------------------------
# nums = []
# while True:
#     try:
#         nums.append(int(input("Enter a int number: ")))
#     except ValueError:
#         break

# total_sum = sum(nums)
# avg = total_sum/len(nums)

# print(f'Avg of those numbers is: {round(avg, 2)}')
# =================================================

# ===============================================
# class problem, Module 9
# Create a student class. The class should have an init function and member variables:
# first_name, last_name, id, courses. Classes should be a dictionary that maps a course id to a list containing course name,
# grade as percentage float, and grade as string letter (i.e. B+). Percentage float should be rounded to 2 decimal places.
# Solution:
# class Student:
#     def __init__(self, first_name,last_name, id):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.id = id
#         self.courses = []
#         self.grade = ""
#         self.gpa = 0.0
#         self.info = {}
#     def get_info(self):
#         self.info = {
#         "First name" : self.first_name,
#         "Last name" : self.last_name,
#         "ID" : self.id,
#         "Course" : self.courses,
#         "Grade" : self.grade,
#         "GPA" : self.gpa
#         }
#         return self.info
#     def print_info(self):
#         '''No return'''
#         print(f'{self.last_name}, {self.first_name}:\n ID:   {self.id}\n Course:   {self.courses}\n   Grade:{self.grade}\n   GPA: {self.gpa}')
#     def add_courses(self):

#         '''No input, No return'''
#         self.input = (input("Enter your courses: "))
#         while self.input != "":
#             self.input = (input("Enter your courses: "))
#             self.courses.append(self.input)
#         self.courses.pop()
#         self.grade = input("Enter your grade: ")
#         valid = False
#         while valid == False:
#             try:
#                 self.gpa = float(input("Enter your GPA: "))
#                 valid = True
#             except ValueError:
#                 print("Invalid GPA.")

# '''Create student_1'''
# student_1 = Student("Jesse", "Yang", 20545215)
# student_1.add_courses()

# '''TEST'''
# print(student_1.get_info())
# student_1.print_info()

# ===================================================

# ==================================================
# 1. Prompt the user to write a few sentences about future academic interests.
# Split the string into individual words and
# write them out line by line into a file called words.txt.
#
# 2. Read in the words from the text file line by line and calculate the average word length. Then, print it to screen.
# -------------------
# solution:
# user_input = input("Enter a few lines sentences about future academic: ")
# input_words = user_input.split(" ")
# print(input_words)

# txt_file = open("text.txt", "w")

# for word in input_words:
#     txt_file.write(word)
#     txt_file.write("\n")
# txt_file.close()

# file_open = open("text.txt", "r")
# txt_read = file_open.readlines()

# word_count = 0
# total_length = 0
# for word in txt_read:
#     total_length += len(word[:-1])
#     word_count += 1
# avg_length = total_length / word_count

# print(f'Total length is {total_length} \nWord count is {word_count}')
# print(f'The avg length of those words is {round(avg_length, 1)}')
# file_open.close()

# file_open = open("text.txt", "r")
# content = file_open.read()
# print(content)
# ==========================================

# =================================
# Ask the user to provide the URL of a website.
# (Assume the user input is valid) Using what you know about strings,
# get the domain of the website. For example,
# the domain name for https://www.deanza.edu/directory/user.html?u=readjustinLinks to an external site.
# would be deanza.edu. You can assume that the website is the standard format, i.e.
# https://www.domainname.com/something/something/etcLinks to an external site.,
# so there won't be any en.wikipedia.org or any different formats for this problem.
# ----------------------
# ucl = input("Please enter website add: ")
# ucl_list = ucl.split(".")
# ucl_sub_list = ucl_list[2].split("/")
# print(f'{ucl_list[1]}.{ucl_sub_list[0]}')
# ============================================

# ===================================
# Prompt the user for the number of students in the following classes; CIS 40, CIS 41A, CIS 41B,
# and create a dictionary with that information.
# Use input validation to ensure that the number is between 0 and 40 inclusive for each class.
# Print out the class name and class count with the most number of students. If there is a tie,
# choose one class to print out.
# ------------------
# cls_dict = {}
# cls1 = input("class name:")
# cls1_n = int(input("class size:"))
# if cls1_n >40 or cls1_n < 0:
#     raise ValueError("out range")
# cls2 = input("class name:")
# cls2_n = int(input("class size:"))
# if cls2_n > 40 or cls2_n < 0:
#     raise ValueError("out range")
# cls3 = input("class name:")
# cls3_n = int(input("class size:"))
# if cls3_n > 40 or cls3_n < 0:
#     raise ValueError("out range")

# cls_dict = {
#     cls1 : cls1_n,
#     cls2 : cls2_n,
#     cls3 : cls3_n
# }

# max_count = 0
# max_name = ""
# for name, student in cls_dict.items():
#     if student > max_count:
#         max_count = student
#         max_name = name
# print(f'largest class is {max_name}, with {max_count} students.')
# ==========================================================

# ==========================================================
# Create a GroceryStore class that includes the following items with an initial price of 0:
# bread, milk, cheese, fruit, vegetable.
# Create 2 functions with this class,
# one that will set the value of the prices (so the user will pass them in),
# and another function that will print out the prices of all the items.
# ------------------------------------
# class Menu:
#     def __init__(self, bread=0.0, milk=0.0, cheese=0.0, fruit=0.0, vegetable=0.0):
#         self.bread = bread
#         self.milk = milk
#         self.cheese = cheese
#         self.fruit = fruit
#         self.vegetable = vegetable

#     def print_price(self):
#         print(f'bread : ${self.bread}')
#         print(f'milk : ${self.milk}')
#         print(f'cheese : ${self.cheese}')
#         print(f'fruit : ${self.fruit}')
#         print(f'vegetable : ${self.vegetable}')

# p1 = Menu(1.99, 2.99,3.99, 4.99, 5.99)
# p1.print_price()
# ========================================

# ========================================
# Imagine there is a file called city elevations.
# txt with the following elevations
# (these are not meant to represent real numbers,
#  they are just made up for this problem).
# San Francisco 800

# San Jose 600

# Los Angeles 100

# San Diego 250

# Sacramento 50
# Read these in to your python program and print out the average,
# highest, and lowest city elevations.
# You can use built in functions to python for this problem.
# ------------------
# file_1 = open("text.txt", "r")
# str_1 = file_1.read()
# file_1.close()
# word_list = str_1.split()
# num_list = []

# for word in word_list:
#     try:
#         num_list.append(int(word))
#     except:
#         pass

# print(f'The highest elevation is {max(num_list)}')
# print(f'The lowest elevation is {min(num_list)}')
# print(f'The avg of the elevation is {sum(num_list) / len(num_list)}')
# ==============================================

# ==========================================================
# There is a file called interests.txt which contains a paragraph of a university applicant's goals for applying.
# Write code that would read in the paragraph into a string
# (you can assume the file exists in the same folder as the python program).
# Print out the longest and the shortest words in that paragraph, along with the length of those words.
# If there is a tie, you can pick 1 word.
# -------------------------------
# file_1 = open("text.txt", "r")
# str_1 = file_1.read()
# file_1.close()

# word_list = str_1.split()
# longest = 0
# longest_word = ""

# for word in word_list:
#     if len(word) > longest:
#         longest = len(word)
#         longest_word = word

# shortest = longest
# shortest_word = ""
# for word in word_list:
#     if len(word) < shortest:
#         shortest = len(word)
#         shortest_word = word
# print(f'The longest word is {longest_word}, with length of {longest}')
# print(f'The shortest word is {shortest_word}, with length of {shortest}')
# ===================================================================


# exam_scores_by_id = {'1' : 95, '2' : 50, '3' : 75, '4' : 90, '5' : 65}
# highest = 0
# highest_id = ""
# for id, score in exam_scores_by_id.items():
#     if score > highest:
#         highest = score
#         highest_id = id
# print(f'The highest score is {highest}, id is {highest_id}')

# def sphere_surface_calc(radius):
#     s = 0.0
#     s = 4.0 * 3.141592653 * (radius ** 2)
#     return round(s, 2)

# def main():

#     S = Student("Sam", classList)         # create a Student object with an instance attribute called name, to
#                                          # store the input name ("Sam" in this case), and an instance attribute
#                                          # called classes, to store the classes in the classList argument.
#     S.search("CIS 40")                   # print "found" if "CIS 40" is in the student's class list
#                                          # or print "not found" otherwise
#     S.print()                             # print the name of the student and then print all the student's classes


# class Student:
#     def __init__(self, name, classList):
#         self.name = name
#         self.classList = classList


#     def search(self, className):
#         found_bool = 0
#         for classes in self.classList:
#             if classes == className:
#                 print("found")
#                 found_bool = 1
#         if found_bool == 0:
#             print("not found")


#     def print(self):
#         print(f'Name: {self.name}: ')
#         print("Classes:")
#         for classes in self.classList:
#             print(classes)
#            
#     def class_count(self):
#         count = len(self.classList)
#         print(f'The student totally enrolled {count} classes.')



# classes_list = ["math", "calc", "english"]
# yang = Student("Yang", classes_list)
# yang.search("english")
# yang.print()
# yang.class_count()


# =====================Course completed======================