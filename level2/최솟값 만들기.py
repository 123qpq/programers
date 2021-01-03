def solution(A,B):
    return sum(list(map(lambda a, b : a * b , sorted(A), sorted(B, reverse=True))))