# ------------save input to dist------------------------
print("usage: enter item name, enter item value, enter " " to end entering,  then print dict in 'item_name : item_value' formate.")
dict = {}
ipt = ""

while ipt != " ":
    name = input("Enter item name:")
    ipt = name
    if ipt == " ":
        break

    value = input("Enter item value: ")
    dict[name] = value

 # print("Check:",dict) --use this to check dict

for item in dict:
    print(f'{item} : {dict[item]}')
# ---------------------------above is good example to save inputs into a dict---------------------
