# --------try out the for loop------
str = "abcdefg"

for a in str:
    print(a)

# Here "a" is a temp name of the variable to represent every char in the string.

lst = [0, 1, 2, 3, 4, 5, 6]

for i in lst:
    j = i + 1

    print(f'{i} is the number {j} - 1')
# Here the variable "i" is a temp name to represent the index of this list.

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}
for name in dict:
    print(f'{name} : {dict[name]}')
# Here the variable name is representing the name of every object in the dict. dict[name] is the value assigned to the name.

str = " Hi, how are you doing?"
new_str = ""
for char in str:
    new_str = new_str + char + "_"

print(new_str)
