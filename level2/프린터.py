def solution(priorities, location):
    answer = 0
    maxnum = max(priorities)
    idx = None
    while maxnum > priorities[location]:
            while maxnum == max(priorities):
                answer += 1
                idx = priorities.index(maxnum)
                priorities[idx] = 0
            maxnum = max(priorities)
            
    if idx != None:
        if location < idx:
            answer += priorities[idx:].count(maxnum)
        else:
            for i in range(idx):
                priorities[i] = 0
    
    while location != priorities.index(maxnum):
        answer += 1
        priorities[priorities.index(maxnum)] = 0
    return answer + 1