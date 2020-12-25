def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if answer == []:
        answer = [-1]
    return answer