# ====================================
# function that return multiple values
# # ----------------------
def circle_calcs(r):
    A = 3.141592653 * r * r
    P = 2 * 3.141592653 * r
    return A, P


given_radius = 5.0
units = "cm"
area, perimeter = circle_calcs(given_radius)
print(
    f'A circle with radius is {given_radius}{units}, the area is {round(area, 2)}{units}^2, the perimeter is {round(perimeter, 2)}{units}. ')
# =====================================================
