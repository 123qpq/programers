def solution(brown, yellow):
    for i in range(1, 1414):
        if yellow % i == 0:
            row = yellow / i
            col = yellow / row
            if 4 + 2 * row + 2 * col == brown:
                return [row + 2, col + 2]