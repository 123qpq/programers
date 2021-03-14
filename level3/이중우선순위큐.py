from collections import deque
import bisect
def solution(operations):
    q = deque()
    for operation in operations:
        oper = operation.split()
        if oper[0] == "I":
            bisect.insort_left(q, int(oper[1]))
        elif len(q) != 0:
            if oper[1] == "1":
                q.pop()
            else:
                q.popleft()
    if len(q) == 0:
        return [0, 0]
    else:
        return [q[-1], q[0]]