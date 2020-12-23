def solution(arr):
    a = -1
    answer = []
    for i in range(len(arr)):
        if a != arr[i]:
            answer.append(arr[i])
            a = arr[i]
    return answer