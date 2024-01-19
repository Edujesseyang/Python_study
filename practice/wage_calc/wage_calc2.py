import math

year_wage = int(input("Enter yearly wage:"))

weekly_wage = math.ceil(year_wage / 52)
print("The round off weekly wage is:", weekly_wage)

daily_wage = math.ceil(weekly_wage / 5)
print("The round off daily wage is:", daily_wage)

hourly_wage = math.ceil(daily_wage / 8)
print("The round off hourly wage is:", hourly_wage)
