import random

# ===============================================================
# Ask user to enter a number between 1 and 10.
# Keep prompting the user to guess until the user is correct.
# Once the user is correct, the user wins the game.
# You may choose the winning number and hard code it.
# Print when the user won and how many tries it took.
# Solution: -----------
answer = random.randint(1, 10)
user_ipt = int(input("Guess a number between 1 and 10: "))
tries = 1
while user_ipt != answer:
    user_ipt = int(input("WRONG! Try again: "))
    tries += 1
else:
    print(f'You Win, You had the right number in {tries} tries.')
# ================================================================
