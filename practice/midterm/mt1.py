ipt = input("Enter the name of the city:")
i = 0
for char in ipt:
    if char != " ":
        i += 1
if i % 2 == 0:
    print("The name is even.")
else:
    print("The name is odd.")
