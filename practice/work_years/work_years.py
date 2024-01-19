# ==========================================================================
# 9. Ask user to enter number of years of work experience.
# Print out the following message based on the answer.
# All ranges are inclusive.
# 0-2 years: "New grad"
# 3-5 years: "Mid"
# 6-10 years: "Senior"
# 11 or more years: "Leadership"
# solution: ------
user_years = int(input("Enter your years of working experience: "))
if user_years > 0:
    if user_years < 2:
        print("New grad")
    elif user_years >= 3 and user_years <= 5:
        print("Mid")
    elif user_years >= 6 and user_years <= 10:
        print("Senior")
    elif user_years >= 11:
        print("Leadership")
# ===============================================================
