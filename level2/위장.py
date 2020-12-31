def solution(clothes):
    answer = 1
    dic = {}
    for clothe in clothes:
        if clothe[1] not in dic:
            dic[clothe[1]] = 2
        else:
            dic[clothe[1]] += 1
    
    for i in list(dic.values()):
        answer *= i
        
    return answer - 1