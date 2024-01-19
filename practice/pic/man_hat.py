# ====================================================
# print pics
# -------------------------
def cowboy_hat():
    print("    ____")
    print("   |    |")
    print("   |====|  ")
    print("~~~~~~~~~~~~")


def magic_hat():
    print("     )(")
    print("    /  \ ")
    print("   /... \ ")
    print("~~~~~~~~~~~~")


def man_face(type_hat):
    type_hat()
    print(" q  O  O  p")
    print("  \  ||  /  ")
    print("   \ ^^ /")
    print("    \__/")


def girl_face(type_hat):
    type_hat()
    print("|q|^O  O^|p|")
    print("||\  __  /||")
    print("|| \____/ ||")


def body(type_hat, type_face):
    type_face(type_hat)
    print("   __||__ ")
    print("  /  \/  \ ")
    print(" /|  88  |\ ")
    print("| |  88  | | ")
    print(" \|__88__|/")
    print("  |  __  |  ")
    print("  |  ||  | ")
    print("  |  ||  |")
    print("  |__||__|")
    print(" (__/  \__)")


print("print menu: ")
print("1: cowboy hat, 2: magic hat")
hat = int(input("Enter hat number: "))
print("1: man face, 2: girl face")
face = int(input("Enter face number: "))
if hat == 1 and face == 1:
    body(cowboy_hat, man_face)
elif hat == 1 and face == 2:
    body(cowboy_hat, girl_face)
elif hat == 2 and face == 1:
    body(magic_hat, man_face)
elif hat == 2 and face == 2:
    body(magic_hat, girl_face)
else:
    print("Please enter the right number. ")
# =====================================
