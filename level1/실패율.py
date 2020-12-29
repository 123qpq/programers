def solution(N, stages):
    answer = []
    stage = [0 for i in range(N + 1)]
    percent = [0 for i in range(N)]
    people = len(stages)

    for i in stages: 
        stage[int(i - 1)] += 1
    del stage[-1]

    for i, x in enumerate(stage): 
        percent[i] = x / people
        people -= x
        if people == 0:
            break
    
    for x in range(0, len(percent)):
        answer.append(percent.index(max(percent)) + 1)
        percent[percent.index(max(percent))] = -1
    
    return answer