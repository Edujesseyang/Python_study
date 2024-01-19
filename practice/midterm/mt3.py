phone_num = input("Enter a phone number: ")
digits = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

for digit in phone_num:
    if digit != "-":
        digits[digit] += 1
print(digits)
