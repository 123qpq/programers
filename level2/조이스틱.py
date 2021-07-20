def solution(name):
    answer = 0
    for i in name:
        alpha = ord(i) - ord('A')
        if alpha > 13:
            answer += 26 - alpha
        else:
            answer += alpha
        
    if name[1] == 'A':
        answer += len(name) - 2
        if name[2] == 'A':
            answer -= 1
    elif name[-1] == 'A':
        answer += len(name) - 2
        if name[-2] == 'A':
            answer -= 1
    else:
        answer += len(name) - 1
    return answer