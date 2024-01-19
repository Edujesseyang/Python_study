names0 = str(input("Enter 1 name: "))
names1 = str(input("Enter 2 name: "))
names2 = str(input("Enter 3 name: "))
names3 = str(input("Enter 4 name: "))
names4 = str(input("Enter 5 name: "))
names = [names0, names1, names2, names3, names4]

print(names)
tem_name = names0
if names0 < names1:
    tem_name = names0
if names1 < names2:
    tem_name = names3
if names2 < names3:
    tem_name = names2
if names2 < names3:
    tem_name = names2
if names3 < names4:
    tem_name
