import math

# ----------------trig calculator---------------
a = float(input("Enter a side: "))
b = float(input("Enter b side: "))
c = float(input("Enter c side: "))
cos_A = ((c ** 2) + (b ** 2) - (a ** 2)) / (2 * b * c)
cos_B = ((c ** 2) + (a ** 2) - (b ** 2)) / (2 * a * c)
cos_C = ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b)
A_d = math.degrees(math.acos(cos_A))
B_d = math.degrees(math.acos(cos_B))
C_d = math.degrees(math.acos(cos_C))

print(f'The 3 angles are :\n A : {A_d} \n B : {B_d} \n C : {C_d}')
