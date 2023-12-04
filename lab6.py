# lab 6

# name: Jesse Yang
 
# This program has 3 functions:
# 1) count how many time the user word occurred in the text. return an int.
# 2) make a dict pairs every word and its occurring counts. return dict pairs format as {"word" : int}
# 3) find the top 5 common words from the input string and return a dict with them and their count pairs 
 
# This program create a file called response.txt, it will ask user a word, and call function 1 to find out how many time the word occurred in the file text.
# Then function 2 will count every word and make them a count list dict them with their counts. 
# Then function 3 will find the top 5 most common words and make a dict with their pairs.
# At the end, the program will rewrite the file with the results of function 1 and 2.
# This program will also print results of function 1, 2, and 3 in the terminal.  


text = "I plan to get a degree in computer engineer major. Python 40 is a good langrage for this major to build fundamental knowledge and understanding in programming. I enjoy to programming, I do really want to start a career in this area. I will keep up to learn and practice. One day, I will be a true expert for programming!"  

user_word = input("Enter a word that you want to search for: ")

response = open("response.txt", "r")
file_txt = response.read()
response.close()

def word_count (string, target_word):
    '''count how many times target_word match words in string'''
    '''input str, str'''
    '''output int'''
    clean_txt = ""
    for char in string:
        if char.isalpha() == True or char == " ":
            clean_txt += char.lower()

    word_list = clean_txt.split(" ")
    count = 0
    for word in word_list:
        if target_word.lower() == word:
            count += 1
    return count

def count_dict(string):
    '''return dict {word : count} pairs'''
    '''input str'''
    '''output dict'''
    clean_txt = ""
    for char in string:
        if char.isdigit() == True:
            clean_txt += char
    clean_txt += " "        
    for char in string:
        if char.isalpha() == True or char == " " or char.isdigit() == True:
            clean_txt += char.lower()
    
    word_dict = {}
    word_list = clean_txt.split(" ")
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1 
    return word_dict

def top5_common_words(string):
    '''return a dict with top 5 common words in the dict with counts'''
    '''input str'''
    '''output dict'''
    clean_txt = ""
    for char in string:
        if char.isdigit() == True:
            clean_txt += char
    clean_txt += " "        
    for char in string:
        if char.isalpha() == True or char == " ":
            clean_txt += char.lower()
    word_list = clean_txt.split(" ")
    word_dict = {}
    top5_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1 
    
    count = max(word_dict.values())

    while len(top5_dict) < 5 and count > 0:
        for key, values in word_dict.items():
            if count == values:
                top5_dict[key] = values
        count -= 1        
    first_5_items = list(top5_dict.items())[:5]
    top5_dict = dict(first_5_items)
    
    return top5_dict

file = open("response.txt", 'w')

file.write(f'{user_word} is occurred {word_count(file_txt, user_word)} times in the text. ')
file.write("\n")
file.write("\n")
file.write("The top 5 common words are: ")
file.write("\n")
file.write("\n")

for key, values in top5_common_words(file_txt).items():
    file.write(f'{key} : {values}')
    file.write("\n")

file.close()    
    
print(f'{user_word} is occurred {word_count(file_txt, user_word)} times in the text. ')
print("The words counts pairs are: ")
print(count_dict(file_txt)) 
print(top5_common_words(file_txt))