def solution(clothes):
    answer = 0
    dic = {}
    for clothe in clothes:
        if clothe[1] not in dic:
            dic[clothe[1]] = 1
        else:
            dic[clothe[1]] += 1
    
    size = len(dic)
    dic = list(dic.values())

    for i in range(1, 2**size):
        mul = 1
        flag = bin(i)[2:].zfill(size)
        for j in range(size):
            if flag[j] == '1':
                mul *= dic[j]
        answer += mul
    return answer