def search(mid, times):
    res = 0
    for time in times:
        res += mid // time
    return res


def solution(n, times):
    times.sort()
    rt = n * times[-1]
    lt = 0
    ans = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if n <= search(mid, times):
            ans = mid
            rt = mid - 1
        else:
            lt = mid + 1
        
    return ans