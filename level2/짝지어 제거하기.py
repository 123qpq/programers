def solution(s):
    lst = [0]
    for i in s:
        if lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)
    return 0 if lst[-1] != 0 else 1