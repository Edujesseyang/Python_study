lst = ["the", "word", "test", "a", "question"]
new_lst = []
longest = 0
i = 0
temp = ""
index = 0
while i < len(lst):
    for word in lst:
        if len(word) > longest:
            longest = len(word)
            temp = word
            index = lst.index(word)
    i += 1
    new_lst.append(temp)
    # lst.pop(index)
print(longest)
print(temp)
print(new_lst)
