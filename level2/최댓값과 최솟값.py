def solution(s):
    temp = ''
    lst = []
    for i in s:
        if i != ' ':
            temp += i
        else:
            lst.append(int(temp))
            temp =''
    lst.append(int(temp))
    return str(min(lst)) + ' ' + str(max(lst))