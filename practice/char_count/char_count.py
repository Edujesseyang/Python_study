# ==========================================================================
#  Prompt user for a sentence about programming. Slice the string for every other character.
# Then, count the  number of vowels and consonants (punctuation and spaces don't count) and print those values out.
# ------------------------------------
string = input("Enter a sentence:")
string = string[:: 2]
vowels_count = 0
consonants_count = 0

string = string.lower()
for char in string:
    if char != " ":
        if char == "a" or "e" or "i" or "o" or "u":
            vowels_count += 1
        elif char.isalpha() == True:
            consonants_count += 1

print(f'There is {vowels_count} vowels, and {consonants_count} consonants.')
print(string)
# ======================================================
