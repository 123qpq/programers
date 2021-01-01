def solution(s):
    answer = 0
    for i in s:
        if i == '(':
            answer += 1
        else:
            answer -=1
        if answer < 0:
            return False
    
    if s[0] == '(' and answer == 0:
        return True
    else:
        return False