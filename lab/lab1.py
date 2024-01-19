import math

# Full name: Jesse Yang

# This program will collect 3 inputs, and calculate the total and print out data in the terminal.
# Details will be between steps

input1 = float(input("Please Enter Your First item: $"))
input2 = float(input("Please Enter The Second item: $"))
input3 = float(input("Please Enter The Third item: $"))

subtotal = input1 + input2 + input3
print("The subtotal is: $", round(subtotal, 2))
# print out the init subtotal.

after_discount = subtotal * 0.9
print("After 10% discount: $", round(after_discount, 2))
# print out the total after discount

after_tax = after_discount * 1.0875
print("With tax, total is: $", round(after_tax, 2))
# print out the total after tax

payment = float(input("Enter the payment: $"))
change = payment - after_tax
print("Change is: $", f'{change:.2f}')
# collect the payment data, calculate the change and print out

# -----------Extra credit--------------
print("=========Extra credit=========")

dollar = math.floor(change)
cents = (change - dollar) * 100
print("Which is", dollar, "dollars, and", round(cents), "cents.")
# floor down the change to get dollar, use (change - dollar) * 100 to get cents, and print out
