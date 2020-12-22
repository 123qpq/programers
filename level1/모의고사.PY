def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    people = [0, 0, 0]
    for i, ans in enumerate(answers):
        if ans == a[i % 5]:
            people[0] += 1
        if ans == b[i % 8]:
            people[1] += 1
        if ans == c[i % 10]:
            people[2] += 1
    for i in range(len(people)):
        if people[i] == max(people):
            answer.append(i + 1)
    return answer