def solution(n):
    answer = 1
    for i in range(1, n):
        temp = 0
        while temp < n:
            temp += i
            if temp == n:
                answer += 1
            i += 1
    return answer