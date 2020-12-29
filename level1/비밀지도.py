def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = "{:b}".format(arr1[i] | arr2[i], 'b').rjust(n, '0')
        answer.append(line.replace('0', ' ').replace('1', '#'))    
    return answer