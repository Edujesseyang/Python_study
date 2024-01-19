import math

# -------- this is find trig----------------------------
a = float(input("Enter the a side:"))
b = float(input("Enter the b side:"))

B = float(input("Enter the angle B: "))

Br = (math.radians(B))
sin_Br = math.sin(Br)
sin_Ar = sin_Br / b * a
Ar = math.asin(sin_Ar)
Ad = math.degrees(Ar)

Cd = 180 - B - Ad

Cr = math.radians(Cd)
sin_Cr = math.sin(Cr)

c = sin_Cr / (sin_Br / b)

print(f'A is {round(Ad, 2)} in degree')
print(f'C is {round(Cd, 2)} in degree')
print(f'The side c is {round(c, 2)}')
# ----------------above not work well, but close--------
