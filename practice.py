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
# ----------------不是能智能, 哈哈---------------

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
#---------------------------above is good example to save inputs into a dict---------------------

# -------------------银行倍率计算器--------------------------------
# interest = float(input("Enter the interest rate:"))
# amount = float(input("How much money do you want to put in:"))
# year = int(input("How many years do you want to save: "))

# for year in range(year): # 这里的第一个year和第二个year不一样, 第一个是方程里的临时名字变量, 第二个是用户输入的变量
#     print(f'In the year {year}, You have {round(amount, 2)}')
#     amount = amount + (amount * interest)
#---------------------------------------------------------------             

#-------------------range() 的用法------------------------------
# lst = range(10, 50, 5)
# for num in lst:
#     print(num)
#----创造一个从10到50的每项增加5的list------------------------------

#--------------class practice--------
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
#---------------------------------------

#-------------class practice------------
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
#-----------------------------------------------------------

#----------------------class practice-----------------------
# for num in range(250, 751, 50):
#     print(num)   
#-----------------------------------------------------------   

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
#---------------------------------------------------------------
    
# ---------------------双 item 的 for loop----------------------
# lst = [1, 2, 3, 4, 5, 6]
# for (index, value) in enumerate(lst):
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

#----------------------Midterm------------------
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

#----------------------Mt 2-----------------------
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
#------------------------------------------    

#---------------MT 3-----------------
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
#--------------------------------------------

#----------------Mt 4------------------------
# grade = int(input("Enter your grade: "))
# if grade >= 1 and grade <= 5:
#     print("Elementary school.")
# elif grade >= 6 and grade <= 8:
#     print("Middle school.")
# elif grade >= 9 and grade <= 12:
#     print("High school.")
#--------------------------------------------

#--------------------------------------------   
# 5. You have the following list of 5 strings:
# ["the", "word", "test", "a", "question"]. Create a new
# list with these words sorted in order of string length.
# If two words have the same length, the order can be
#either way (i.e. with "word" and "test"). You may use any
# string or list function to complete this problem.
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
#---------------------------------------------------
# for nums in range(-1000, 1001, 4):
#     print(nums)
# ===================================================

# ===========================================================
# Cupertino: 59
# Sunnyvale: 60
# Saratoga: 56
# San Jose: 61
# Campbell: 59
# Los Altos: 58
# Put these into a dictionary and print out the city with the highest and lowest temperatures. If there's a tie, just pick one city
# Solution: --------------------------------------------------
# city_temps = {
#     'Cupertino' : 59,
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
