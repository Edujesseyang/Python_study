name = str(input("Enter a name: "))

len = len(name)

if len % 3 == 0:
    print("city name: ", name)
else:
    print(name[0], name[-1])

print("The length is :", len)
