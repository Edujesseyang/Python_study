nums = []
for i in range(5):
    nums.append(int(input("Enter a number:")))

print(nums)
total = 0
count = 0
for num in nums:
    total += num
    count += 1
print(f'The sum is: {total}, The avg is: {round((total / count), 2)}')
