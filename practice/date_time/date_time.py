date = int(input("Enter a date in format of MMDDYYYY:"))
month = date // 1000000
year = date % 10000
day = date // 10000 % 100
print("The month is:", month)
print("The year is:", year)
print("The day is:", day)
