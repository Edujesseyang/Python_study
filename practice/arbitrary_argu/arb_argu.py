# =====================================
# Arbitrary argument list
# *args
# -----------------------
def add_up(x, y, *more):
    result = x + y
    for num in more:
        result += num
    return result


print(add_up(1, 3, 4, 5, 6))
# -------------------------
# **kwargs
# ---------------------


def info(name, **info):
    print(f'{name}:')
    for category, context in info.items():
        print(f'{category} is {context}')


info("Jesse", age=35, gender="male", wife="Chloe", favorite_food="noodle")
# ====================================================
