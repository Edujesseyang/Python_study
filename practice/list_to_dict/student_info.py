# ==================================================
# Create a function that asks student for first and last name (separately), student ID,
# classes that get read into a list, and expected graduation year. Create another
# function that prints out the information in this order:
# --------------------------------------
def lst(name, ID, classes, year):
    list_name = {
        'name': input("Enter your name: "),
        'ID': input("Enter your ID: "),
        'classes': input("Enter your class: "),
        'year': input("Enter your graduation year: ")
    }
    return list_name


def prt(name):
    print(name)


student = lst("yang", 124, "python", 2024)
prt(student)
# ====================================================
