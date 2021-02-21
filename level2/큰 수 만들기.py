def solution(number, k):
    num = []
    for i in number:
        while len(num) != 0 and k != 0 and i > num[-1]:
            num.pop()
            k -= 1
        num.append(i)
    if k != 0:
        num = num[:-k]
    return ''.join(num)