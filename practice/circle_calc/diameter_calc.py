import math

# =========================================
# Write a function that calculates the diameter of a circle given the circle's area.
# ---------------------------------------


def diam(area):
    return 2 * math.sqrt(area / math.pi)


area = 15
print(f'Area is {area}, diameter is {round(diam(area), 2)}')

diam(int(input('Enter area: ')))
# =================================================
