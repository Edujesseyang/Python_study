# ===========================================
# try out:
# prompt user to enter a number
# only collect numbers in the string
# make a new string for all numbers
# re-type the string to be int.
# return if result in 1-20.
# --------------------------------------------
def get_input():
    result = ""
    vail = False
    while vail == False:
        get_input = input("Enter: ")
        for char in get_input:
            if 48 <= ord(char) <= 57:
                result = result + char
                vail = True
    result = int(result)
    while 1 <= result <= 20:
        return result
    else:
        print("enter vail number")


x = get_input()
print(x)
# ============================================
