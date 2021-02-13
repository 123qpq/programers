def solution(priorities, location):
    answer = 0
    candidate = [(j, i) for i, j in enumerate(priorities)]
    
    while True:
        m = max(candidate)[0]
        c = candidate.pop(0)
        if c[0] == m:
            answer += 1
            if c[1] == location:
                return answer
        else:
            candidate.append(c)