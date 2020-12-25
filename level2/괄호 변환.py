def check(p):
    check = 0
    B = '('
    if p[0] == ')':
        B = ')'

    for i, bracket in enumerate(p): #균형잡힌 괄호 추출
        if bracket == B:
            check += 1
        else:
            check -= 1
            
        if check == 0:
            return i
            break

def change(p): 
    temp = ''
    for i in p[1:-1]:   #처음, 끝 제외 문자열 뒤집기
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return(temp)

def solution(p):
    if not p:           #빈 문자열은 반환
        return ''
    chk = check(p)
    if p[0] == '(':     #올바른 괄호
        return p[:chk + 1] + solution(p[chk + 1:])
    else:               #올바르지 못한 괄호
        return '(' + solution(p[chk + 1:]) + ')' + change(p[:chk + 1])