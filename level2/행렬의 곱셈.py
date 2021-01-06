def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            answer[i] = list(map(lambda x, y: x + y , answer[i], list(map(lambda x: arr1[i][j] * x , arr2[j]))))
    return answer