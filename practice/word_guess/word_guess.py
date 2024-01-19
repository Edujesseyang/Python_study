import random

# ============================================
# guessing word game:
# -----------------------------------------
'''create a word list and random out one word to be the target word.'''
word_list = ["fox", "bee", "box", "cat", "dog",
             'pig', 'owl', 'rat', 'bat', 'elk', 'ape', 'cow']
word_num = random.randint(0, 12)
target_word = word_list[word_num]
final_answer = word_list[word_num]
'''replace the target word to be ------ format'''
hide_target = "-" * len(target_word)
chances = 10


def get_user_input():
    ipt = input("Guess a character may in the word: ")
    return ipt[0]


user_input = ''  # create a var for user input
'''main loop: get user input, check  input and replace with hind_target word.'''
while chances > 0:
    user_input = get_user_input()
    # loop to check if user_input is in the target
    for index in range(len(target_word)):
        # if match, switch user input with hide_word same spot
        if user_input == target_word[index]:
            hide_target = hide_target[: index] + \
                user_input + hide_target[index + 1:]
            target_word = target_word[: index] + "-" + target_word[index + 1:]
    print(hide_target)  # print new hide word
    chances -= 1
    if chances > 1:  # count down chances
        print(f'You have {chances} chances left.')
    elif chances == 1:
        print(f'You have {chances} chance left.')
    else:
        print("No more chance!")
    # if all "-" got replaced by user input chars. break loop & print win statement
    if hide_target.find("-") == -1:
        print("You win!")
        break
else:
    # if loop had completed, means no more chance to guess, print lose statement
    print(f'You lose! Right answer is "{final_answer}"')

# ==========================================================================
