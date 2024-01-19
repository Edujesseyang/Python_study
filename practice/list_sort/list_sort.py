# --------------------------------------------
# 5. You have the following list of 5 strings:
# ["the", "word", "test", "a", "question"]. Create a new
# list with these words sorted in order of string length.
# If two words have the same length, the order can be
# either way (i.e. with "word" and "test"). You may use any
# string or list function to complete this problem.
# ---------------------------------
# # Solution:
lst = ["the", "word", "test", "a", "question"]   # test body
new_lst = []  # result list
longest = 0
i = 0
temp = ""
count = len(lst)
for word in lst:    # find the longest word
    if len(word) > longest:
        longest = len(word)
shortest = longest        # make the temp shortest to be the longest

while i < count:       # loop len(lst) times
    shortest = longest   # re-set  temp shortest every loop
    temp = ""           # re-set temp word every loop
    for word in lst:        # find the shortest word
        if len(word) <= shortest:
            temp = word    # assign temp to be the shortest word
            shortest = len(word)    # re-assign the length of the shortest

    new_lst.append(temp)   # add temp to result list

    for word in lst:      # loop list body find and remove the shortest word
        if word == temp:
            lst.remove(word)
    i += 1

print(new_lst)   # print result
# --------------------------------------------------------------------------
