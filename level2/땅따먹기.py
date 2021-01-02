def solution(land):
    answer = 0
    land.append([0, 0, 0, 0])
    for i in range(len(land)-1):
        nowmax = max(land[i])
        nextmax = max(land[i+1])
        if land[i].index(nowmax) == land[i+1].index(nextmax):
            if sorted(land[i])[-1] + sorted(land[i+1])[-2] < sorted(land[i])[-2] + sorted(land[i+1])[-1]:
                print(answer, sorted(land[i])[-2])
                answer += sorted(land[i])[-2]
            else:
                print(answer, nowmax)
                answer += nowmax + sorted(land[i+1])[-2] - sorted(land[i+1])[-1]
        else:
            print(answer, nowmax)
            answer += nowmax
            

    return answer