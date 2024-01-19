import math
import random

# Name : Jesse Yang
#-------------------------------------------------------
# Program A : Car insurance costs tool.
# -- The program will prompt the user to ask age and whether user has ever been accident in 2 years.
# -- Then the program will print out the costs for users. 
# -- I added two else conditions to check if age < 16, print out "We don't have any plan fits you." and if user fail to enter yes/no.
#-------------------------------------------------------
# Program B : Car costs compare tool.
# -- This program will prompt the user 3 int prices, and store those values into a list.
# -- Then the program will calculate the maximum cost, the minimum cost, the difference between max and min, and the total cost.
# -- store all those information in a dictionary.

#---------------------Program A------------------------------
age = int(input("Please enter your age: "))  # prompt user enter age
ever_accident = input("Have you ever been in an accident in the last 2 years? (yes/no): ") # prompt user if had accidents
if ever_accident == "yes":   # branch if accident is true
    if 16 < age <= 25:                          # check age group and print out prices
        print("Your costs will be: $3500.")        
    elif 26 < age < 45:
        print("Your costs will be: $2500.")
    elif age >= 46:
        print("Your costs will be: $1500.")
    else:
        print("We don't have any plan fits you.")   # prompt if user enter age less than 16
elif ever_accident == "no":   # branch if accident is false
    if 16 < age <= 25:                          # check age group and print out prices
        print("Your costs will be: $3000.")
    elif 26 < age < 45:
        print("Your costs will be: $2000.")
    elif age >= 46:
        print("Your costs will be: $1200.") 
    else:
        print("We don't have any plan fits you.")  # prompt if user enter age less than 16
else:
    print("Please enter yes/no only.")   # prompt user if user fail to enter yes/no question
    
#-----------------------Program B------------------------------
car_price_1 = float(input("Enter the first car price: "))   # prompt car prices
car_price_2 = float(input("Enter the second car price: "))
car_price_3 = float(input("Enter the third car price: "))

car_list = [car_price_1, car_price_2, car_price_3] # store prices into a list

max_cost = 0   # temporary store the max and total cost
total_cost = 0

for cost in car_list:   # loop through to find the max and total cost
    total_cost += cost
    if cost > max_cost:
        max_cost = cost

min_cost = max_cost # temporary assign the highest value in the list to min cost

for cost in car_list:  # loop through to find the min cost
    if cost < min_cost:
        min_cost = cost
        
diff_max_min = max_cost - min_cost   # find the diff between max and min
     
print(f'The maximum cost is: {max_cost}')  # print all results out
print(f'The minimum cost is: {min_cost}')
print(f'The total cost of all cars is: {total_cost}')
print(f'The difference between max and min is: {diff_max_min}')

compare_result = {               # store all results into a dict
    "Maximum cost" : max_cost,
    "Minimum cost" : min_cost,
    "Total cost" : total_cost,
    "Difference of max and min" : diff_max_min,
    }
    

    
             