# ==========================================================
# There is a file called interests.txt which contains a paragraph of a university applicant's goals for applying.
# Write code that would read in the paragraph into a string
# (you can assume the file exists in the same folder as the python program).
# Print out the longest and the shortest words in that paragraph, along with the length of those words.
# If there is a tie, you can pick 1 word.
# -------------------------------
file_1 = open("text2.txt", "r")
str_1 = file_1.read()
file_1.close()

word_list = str_1.split()
longest = 0
longest_word = ""

for word in word_list:
    if len(word) > longest:
        longest = len(word)
        longest_word = word

shortest = longest
shortest_word = ""
for word in word_list:
    if len(word) < shortest:
        shortest = len(word)
        shortest_word = word
print(f'The longest word is {longest_word}, with length of {longest}')
print(f'The shortest word is {shortest_word}, with length of {shortest}')
# ===================================================================
