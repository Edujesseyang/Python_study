# ------------input nums to get the avg---------------
#  || usage: keep input nums, when finish, input 0. ||
# ----------------------------------------------------

ipt_current = int(input("Enter your numbers: "))
sum_nums = 0
ipt_count = 0

while ipt_current != 0:
    sum_nums = sum_nums + ipt_current
    ipt_count += 1
    ipt_current = int(input("Keep entering, enter 0 to start calculating: "))
print("The average of those numbers is:", sum_nums / ipt_count)
# ---------输入数字 最后output这些数字的平均值.---------
