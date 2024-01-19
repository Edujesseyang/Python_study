# =====================================================================================
# 8. Ask user to keep entering names until user is finished.
# Put these names into a list. Print out the longest and shortest names. Spaces count as characters.
# Solution: ---------------------------------------------------------------------------
name_list = []
user_ipt = " "

while user_ipt != "":
    user_ipt = input("Enter a name, double press enter to finish entering: ")
    name_list.append(user_ipt)

name_list.pop(len(name_list) - 1)

longest = 0
longest_name = ""
for name in name_list:
    if len(name) > longest:
        longest_name = name
        longest = len(name)
shortest = longest
shortest_name = ""
for name in name_list:
    if len(name) < shortest:
        shortest_name = name
        shortest = len(name)
print(f'The longest name is {longest_name}, It has {longest} characters.')
print(f'The shortest name is {shortest_name}, It has {shortest} characters.')
# ===============================================================================
