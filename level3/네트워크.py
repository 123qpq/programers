from collections import deque
def solution(n, computers):
    lst= [i for i in range(n)]
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            q = deque()
            q.append(i)
            while q:
                node = q.popleft()
                for j in range(n):
                    if visited[j] == False and computers[node][j] == 1:
                        lst[j] = lst[node]
                        visited[j] = True
                        q.append(j)
    
    return len(set(lst))