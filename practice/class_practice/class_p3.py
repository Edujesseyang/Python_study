# ------------------class practice--------------------------------
# || Usage: input num of students, input name and scores pairs, ||
# ||       Program will calculate avg score, list all paris,    ||
# ||       find and print the hightest score and student name.  ||
# ----------------------------------------------------------------
scores = {}
total = 0
students_count = int(input("How many students: "))
for name in range(students_count):
    name = input("Enter your student name: ")
    scores[name] = int(input("Enter your score: "))
    total += scores[name]

for name in scores:
    print(f'{name} : {scores[name]}')

print(f'Avg is {round((total/students_count), 2)}')

hightest = 0
for name in scores:
    if scores[name] > hightest:
        hightest = scores[name]
for name in scores:
    if scores[name] == hightest:
        print(f'The hightest score is "{name}" : {hightest}. ')
        break
# ---------------------------------------------------------------
