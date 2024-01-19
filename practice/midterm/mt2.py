lst = []
while ipt != -1:
    ipt = (input("Enter ints:"))
    lst.append(ipt)


max_num = max(lst)
second_max = -1
for num in lst:
    if num > second_max and num != max_num:
        second_max_num = num
if second_max == -1:
    second_max = max_num
print("The second max is", second_max)
