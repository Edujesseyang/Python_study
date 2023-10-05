import math
import random

# problem 1

year_wage = int(input("Enter yearly wage:"))

weekly_wage = year_wage / 52
print("The weekly wage is :", weekly_wage)

daily_wage = weekly_wage / 5
print("The daily_wage is :", daily_wage)

hourly_wage = daily_wage / 8
print("The hourly_wage is:", hourly_wage)

# problem 2

weekly_wage = math.ceil(year_wage / 52)
print("The round off weekly wage is:", weekly_wage)

daily_wage = math.ceil(weekly_wage / 5)
print("The round off daily wage is:", daily_wage)

hourly_wage = math.ceil(daily_wage / 8)
print("The round off hourly wage is:", hourly_wage)




