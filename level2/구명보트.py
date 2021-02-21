from collections import deque
def solution(people, limit):
    boats = 0
    people.sort()
    people = deque(people)
    while people:
        boats += 1
        if len(people) == 1:
            break
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()
    return boats