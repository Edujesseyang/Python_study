import random

# ======================================
# Name: 
# Jesse Yang
# -------------------
# Description:
# This program include three functions:
# (1) get user input: prompt user to enter a number between 1 to 20
# (2) check answer: compare the user input with a random int.
# (3) start game: main function call to start the game, it gets a random int.
# and loop 5 time to call get user inputs function. 
# Each loop calls check answer function to check if user input match the random int.
# Output of this game:
# Each time when user enter a int, the program will print out a result.
# "Too high", "Too low", or "You got it."
# It will also count down the chances left.
# The default setting is 5 chances to guess.
# ======================================

def get_user_input():
    '''Get user input number, return an int between 1 to 20.'''
    user_input = int(input("Enter a number between 1 to 20: "))
    while user_input < 1 or user_input > 20:
        user_input = int(input("Enter a number between 1 to 20: "))
    return user_input

def check_answer(number, random_number):
    '''compare two arguments, print out result, no return value.'''
    if number > random_number:
        print("Too high! ")
    elif number < random_number:
        print("Too low! ")
    else:
        print('\033[92m' + "WIN, you got it!" + '\033[0m')
    return None

default_guess_chance = 5 # default total guessing chances the user has

def start_game():
    '''Get a random int.'''
    get_random = random.randint(1, 20)
    winning = False # default winning status
    '''Main loop prompts user to enter input for default_chance times, compare answer, and print out chances left.'''
    for i in range(default_guess_chance):
        user_input = get_user_input()
        check_answer(user_input, get_random)
        if user_input != get_random and i == default_guess_chance - 2:
            print(f'You have {default_guess_chance - 1 - i} chance to guess. ') # Modify the singular and plural forms of "chance" when only 1 chance is left.
        elif user_input != get_random and i != default_guess_chance - 1:
            print(f'You have {default_guess_chance - 1 - i} chances to guess. ') # count down guessing chances.
        if user_input != get_random and i == default_guess_chance - 1:
            print('\033[31m' + "You lose." + '\033[0m') # print out if user lose
            print('\033[31m' + "GAME OVER!" + '\033[0m')
        if user_input == get_random: # loop breaker if user got the right answer.
            winning = True
            break
    if winning == False: # give out the right answer after user lost.
        print(f'The right answer is {get_random}.')   
             
start_game() 
        
        






        
