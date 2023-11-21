# Lab 4
# Name: Jesse Yang
#
# ================= Part 1 ===========================
# '''This program is a palindrome checker, it include a function call palindrome check, when user calls this function,
# it requests a string type argument, function has two loops and two temp variables, those loops will create two lists, 
# one lays out all chars in arrange order, other one is in reverse order, the last part "if else" checks if these two are same,
# return true or false'''

def palindrome_check(string):
    char_list = []
    compare_list = []
    for char in string:
        if char.isupper() == True:
            compare_list.append(char.lower())
        elif char.islower() == True:
            compare_list.append(char)
    
    i = len(string) - 1
    while i >= 0:
        if string[i].isupper() == True:
            char_list.append(string[i].lower())
        elif string[i].islower() == True:
            char_list.append(string[i])
        i -= 1
   
    if char_list == compare_list:
        return True
    else:
        return False
    
# TEST:
test_strings = ["Race! car", "Testing", "@$%@@ AbCdE #523 dcBa !!"]

for string in test_strings:
    if palindrome_check(string) == True:
        print("This is a palindrome string.")
    else:
        print("This is not a palindrome string.")

# ========================== Part 2 =======================
# This program is a list rotator, it has one list type argument. The function will create a temp variable to store the last element of the list.
# Then it will insert the temp variable to the first, and pop the last element. The function will return the new version of the list.

def list_rotator(list):
    temp_element = list[len(list)-1]
    list.insert(0, temp_element)
    list.pop()
    return list

# TEST:
test_lists = [
    [1, 2, 3, 4, 5],
    ["a", "b", "c", "d", "e"],
    [1, "a", 2, "b", 3]
]
for list in test_lists:
    print(list_rotator(list))