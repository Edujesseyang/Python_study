# =======================================================
# Prompt user for another sentence about programming.
# Then ask user to enter in a word.
# Using string methods to check if the word is in the sentence.
# -----------------------------------------
string = input("Enter a sentence: ")
word = input("Enter a word: ")
if string.find(word) == -1:
    print(f'There is no word: {word} in the sentence. ')
else:
    print("The word is in the sentence.")
