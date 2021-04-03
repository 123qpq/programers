def solution(dirs):
    answer = 0
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    dic = {"U" : 0, "L" : 1, "D" : 2, "R" : 3}
    visited = set()
    x, y = 0, 0
    for d in dirs:
        i = dic[d]
        dxx, dyy = x + dx[i], y + dy[i]
        if -5 <= dxx <= 5 and -5 <= dyy <= 5:
            if (x, y, dxx, dyy) not in visited:
                visited.add((x, y, dxx, dyy))
                visited.add((dxx, dyy, x, y))
                answer += 1
            x, y = dxx, dyy
    return answer