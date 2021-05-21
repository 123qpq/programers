import heapq
def solution(N, road, K):
    route = [float('inf')] * (N)
    graph = [[] for _ in range(N)]
    
    for r in road:
        u, v, w = r
        graph[u-1].append((w, v-1))
        graph[v-1].append((w, u-1))
    
    hq = []
    route[0] = 0
    heapq.heappush(hq, (0, 0))

    while hq:
        length, node = heapq.heappop(hq)
        if route[node] < length:
            continue
        for l, n in graph[node]:
            l += length
            if l < route[n]:
                route[n] = l
                heapq.heappush(hq, (l, n))

    return len(list(filter(lambda x : x <= K, route)))