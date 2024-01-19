# ==============================================
# Prompt the user for a list of numbers. Create a function that takes the list
# in and returns a 2-element list back with a sum of the odd numbers in the
# input list and a sum of the even numbers in the input list.
# -----------------------------------------
num_list = []
ipt = 0
while ipt != "":
    ipt = input("Enter a number: ")
    if ipt != "":
        num_list.append(int(ipt))


def sum(my_list):
    result = []
    sum_odd = 0
    sum_even = 0
    for num in my_list:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    result = [sum_even, sum_odd]
    return result


answer = sum(num_list)
print(f'Sum of odd is {answer[1]}')
print(f'Sum of even is {answer[0]}')
# ================================================
