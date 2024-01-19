# =======================================================
# Use a while loop to keep prompting user for more positive integers until user types -1.
# ----------------------------------------------------------
num = int(input("Enter a positive int: "))
num_list = [num]
while True:
    try:
        num = int(input("Enter a positive int: "))
        num_list.append(num)
    except ValueError:
        break

dict = {}

for num in num_list:
    if not num in dict:
        dict[num] = 0

for num in num_list:
    if num in dict:
        dict[num] += 1
print(dict)
# ===========================================================
