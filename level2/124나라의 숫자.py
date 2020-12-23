def solution(n):
    base = str.maketrans('012', '124')
    answer = ''

    while n // 3 != 0 and n != 3:
        n -= 1
        answer += str(n % 3)
        n //= 3
    answer += str(n - 1)

    return answer[::-1].translate(base)