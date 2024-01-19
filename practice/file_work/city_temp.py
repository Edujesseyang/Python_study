# ========================================
# Imagine there is a file called city elevations.
# txt with the following elevations
# (these are not meant to represent real numbers,
#  they are just made up for this problem).
# San Francisco 800

# San Jose 600

# Los Angeles 100

# San Diego 250

# Sacramento 50
# Read these in to your python program and print out the average,
# highest, and lowest city elevations.
# You can use built in functions to python for this problem.
# ------------------
file_1 = open("text.txt", "r")
str_1 = file_1.read()
file_1.close()
word_list = str_1.split()
num_list = []

for word in word_list:
    try:
        num_list.append(int(word))
    except:
        pass

print(f'The highest elevation is {max(num_list)}')
print(f'The lowest elevation is {min(num_list)}')
print(f'The avg of the elevation is {sum(num_list) / len(num_list)}')
# ==============================================
