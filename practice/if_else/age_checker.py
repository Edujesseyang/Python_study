age = int(input("Enter your age: "))
ht = int(input("Enter your height in inches: "))

if age < 18:
    if ht < 50:
        print("You cannot ride")
    else:
        print("you can ride with parents")
else:
    print("you can ride")
