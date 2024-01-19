# ===================================
# Prompt the user for the number of students in the following classes; CIS 40, CIS 41A, CIS 41B,
# and create a dictionary with that information.
# Use input validation to ensure that the number is between 0 and 40 inclusive for each class.
# Print out the class name and class count with the most number of students. If there is a tie,
# choose one class to print out.
# ------------------
cls_dict = {}
cls1 = input("class name:")
cls1_n = int(input("class size:"))
if cls1_n > 40 or cls1_n < 0:
    raise ValueError("out range")
cls2 = input("class name:")
cls2_n = int(input("class size:"))
if cls2_n > 40 or cls2_n < 0:
    raise ValueError("out range")
cls3 = input("class name:")
cls3_n = int(input("class size:"))
if cls3_n > 40 or cls3_n < 0:
    raise ValueError("out range")

cls_dict = {
    cls1: cls1_n,
    cls2: cls2_n,
    cls3: cls3_n
}

max_count = 0
max_name = ""
for name, student in cls_dict.items():
    if student > max_count:
        max_count = student
        max_name = name
print(f'largest class is {max_name}, with {max_count} students.')
