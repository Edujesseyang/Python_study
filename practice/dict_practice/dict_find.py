exam_scores_by_id = {'1': 95, '2': 50, '3': 75, '4': 90, '5': 65}
highest = 0
highest_id = ""
for id, score in exam_scores_by_id.items():
    if score > highest:
        highest = score
        highest_id = id
print(f'The highest score is {highest}, id is {highest_id}')
