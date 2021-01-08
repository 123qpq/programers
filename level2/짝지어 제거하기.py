def solution(s):
    s = list(s)
    pv = 1
    while pv != 0:
        pv = 0
        for idx, n in enumerate(s):
            if s[idx] == s[idx-1]:
                pv = 1
                s.pop(idx)
                s.pop(idx-1)
    if len(s) == 0:
        return 1
    else:
        return 0