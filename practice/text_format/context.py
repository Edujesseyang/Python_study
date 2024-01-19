# ==================================================
# 1. Prompt the user to write a few sentences about future academic interests.
# Split the string into individual words and
# write them out line by line into a file called words.txt.
#
# 2. Read in the words from the text file line by line and calculate the average word length. Then, print it to screen.
# -------------------
# solution:
user_input = input("Enter a few lines sentences about future academic: ")
input_words = user_input.split(" ")
print(input_words)

txt_file = open("text.txt", "w")

for word in input_words:
    txt_file.write(word)
    txt_file.write("\n")
txt_file.close()

file_open = open("text.txt", "r")
txt_read = file_open.readlines()

word_count = 0
total_length = 0
for word in txt_read:
    total_length += len(word[:-1])
    word_count += 1
avg_length = total_length / word_count

print(f'Total length is {total_length} \nWord count is {word_count}')
print(f'The avg length of those words is {round(avg_length, 1)}')
file_open.close()

file_open = open("text.txt", "r")
content = file_open.read()
print(content)
# ==========================================
