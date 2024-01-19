# ==========================================================
# Create a GroceryStore class that includes the following items with an initial price of 0:
# bread, milk, cheese, fruit, vegetable.
# Create 2 functions with this class,
# one that will set the value of the prices (so the user will pass them in),
# and another function that will print out the prices of all the items.
# ------------------------------------
class Menu:
    def __init__(self, bread=0.0, milk=0.0, cheese=0.0, fruit=0.0, vegetable=0.0):
        self.bread = bread
        self.milk = milk
        self.cheese = cheese
        self.fruit = fruit
        self.vegetable = vegetable

    def print_price(self):
        print(f'bread : ${self.bread}')
        print(f'milk : ${self.milk}')
        print(f'cheese : ${self.cheese}')
        print(f'fruit : ${self.fruit}')
        print(f'vegetable : ${self.vegetable}')


p1 = Menu(1.99, 2.99, 3.99, 4.99, 5.99)
p1.print_price()
# ========================================
