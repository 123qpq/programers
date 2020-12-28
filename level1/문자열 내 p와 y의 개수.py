def solution(s):
    py = 0
    for a in s:
        if a == 'p' or a == 'P':
            py += 1
        if a == 'y' or a == 'Y':
            py -= 1
    return True if py == 0 else False