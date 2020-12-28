def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville, reverse=True)
    while scoville[-1] < K:
        if len(scoville) < 2:
            return -1
        min1 = scoville.pop()
        min2 = scoville.pop()
        scoville.append(min1 + 2 * min2)
        scoville = sorted(scoville, reverse=True)
        answer += 1

    return answer