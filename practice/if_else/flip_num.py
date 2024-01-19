# Flip a number:
num = int(input("Enter a number:"))
num2 = 0

while num > 0:
    num2 = num2 * 10
    num2 = (num % 10) + num2
    num = num // 10

print(num2)
