def mul(c):
    if c == 'S':
        return (1)
    elif c == 'D':
        return (2)
    elif c == 'T':
        return (3)

def solution(dartResult):
    answer = 0
    res = 0
    temp = 0
    num = []
    num.append(0)

    for i, x in enumerate(dartResult):

        if x.isdigit():
            res = res * 10 + int(x)
        elif x.isalpha():
            res **= mul(x)
            print(res)
            num.append(res)
            temp = res
            res = 0

        if x == '*':
            num[-2] *= 2
            num[-1] *= 2
        if x == '#':
            num[-1] *= -1
            
    for i in num:
        answer += i
    return answer