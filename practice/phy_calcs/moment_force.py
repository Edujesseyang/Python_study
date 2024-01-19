# -------------moment and force ------------------
# || Usage: enter f1 and d1, select what answers do you need. ||
# ------------------------------------------------
print("Usage: enter f1 and d1, select what answers do you need. ")
f_1 = float(input("Enter the force 1: "))
d_1 = float(input("Enter the distance between force 1 and pivoted point: "))
bool = input("You need to find the force 2 or the distance? f/d :")
if bool == "f":
    d_2 = float(input("What is the distance of force 2 to the pivoted point: "))
    ans = (f_1 * d_1) / d_2
    print(f'The force 2 is : {ans}')
elif bool == "d":
    f_2 = float(input("What is the force 2: "))
    ans = (f_1 * d_1) / f_2
    print(f'The distance between the point and force 2 is : {ans}')
# ------------------------------------------------------------------------
