def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):
        line = "{:b}".format(arr1[i] | arr2[i], 'b')
        if len(line) < n:
            line = '0' * (n-len(line)) + line
        answer.append(line.replace('0', ' ').replace('1', '#'))    
    return answer