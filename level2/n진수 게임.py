def changeBase(num, n):
    p, q = divmod(num, n)
    return changeBase(p, n) + '0123456789ABCDEF'[q] if p else '0123456789ABCDEF'[q]
    
def solution(n, t, m, p):
    temp, num = '', 0
    while len(temp) <= t * m:
        temp += changeBase(num, n)
        num += 1
    return ''.join(temp[i * m + p - 1] for i in range(t))