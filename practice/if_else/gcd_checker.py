num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
gcd = 0
while num1 != num2:
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1
    gcd = num1

print(gcd)
# ----The program above is a tool to look for the greatest common denominator.--------
# ----num1 and num2 are user input nums. gcg is greatest common denominator of both nums.-------
