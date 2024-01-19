# ===============================================
# Enter numbers, get the avg of all numbers
# ----------------------------------------
nums = []
while True:
    try:
        nums.append(int(input("Enter a int number: ")))
    except ValueError:
        break

total_sum = sum(nums)
avg = total_sum/len(nums)

print(f'Avg of those numbers is: {round(avg, 2)}')
# =================================================
