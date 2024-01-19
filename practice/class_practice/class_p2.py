import random
import math

num = random.randint(0, 100)
user_ipt = int(input("Guess a number:  "))
tries = 7
while user_ipt != num or tries > 0:

    if tries > 0:
        if user_ipt < num:
            print("Guess higher next time!")
        elif user_ipt == num:
            print(f'YOU WIN, the number is {num}')
            break
        else:
            print("Guess lower next time!")
    else:
        print(f'You lost, the right number is {num}')
        break
    tries -= 1
    user_ipt = int(input("Guess a number: "))
    print(f'You have {tries} more chances to guess!')
