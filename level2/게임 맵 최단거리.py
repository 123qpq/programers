from collections import deque
def solution(maps):
    answer = 0
    endx = len(maps[0])
    endy = len(maps)
    visited = [[False]*endx for _ in range(endy)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([(0, 0)])
    
    while q:
        answer += 1
        for _ in range(len(q)):
            now = q.popleft()
            if now == (endx-1, endy-1):
                return answer
            else:
                for i in range(4):
                    dxx = now[0] + dx[i]
                    dyy = now[1] + dy[i]
                    if 0 <= dxx < endx and 0 <= dyy < endy and maps[dyy][dxx] == 1:
                        maps[dyy][dxx] = 0
                        q.append((dxx, dyy))
    return -1
                