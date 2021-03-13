from collections import deque
def solution(numbers, target):
    ans = 0
    n = len(numbers)
    q = deque()
    q.append((0, 0))
    while q:
        level, res = q.popleft()
        if level == n:
            if res == target:
                ans += 1
        else:
            q.append((level+1, res+numbers[level]))
            q.append((level+1, res-numbers[level]))
    
    return ans