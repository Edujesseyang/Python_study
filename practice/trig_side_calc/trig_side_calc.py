import math

side1 = int(input("Enter the first side length:"))
side2 = int(input("Enter the second side length:"))

hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)

print("The hypotenuse of the triangle is:", f'{hypotenuse:.0f}')
