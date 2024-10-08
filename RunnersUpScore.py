if __name__ == '__main__':
    name_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([name, score])


def sort_student(name_score):
    score = []
    for student in name_score:
        score.append(student[1])


sorted_score = sorted(set(score))
second_sorted_score = sorted_score[1]

names_second_lowest = []
for names in name_score:
    if names_second_lowest[1] == second_sorted_score
        names_score_lowest.append(names[0])
names_second_lowest = sorted(names_second_lowest)