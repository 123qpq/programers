import heapq
def solution(n, edge):
    answer = 0
    table = [[] for j in range(n)]
    
    for x, y in edge: #인접리스트 생성
            table[x-1].append(y-1)
            table[y-1].append(x-1)
            
    dist = [0] + [n+1 for i in range(n-1)] #거리저장소
    queue = []
    heapq.heappush(queue, 0) #큐에 첫 노드 저장
    
    while queue: # 큐 탐색
        current_node = heapq.heappop(queue) #연결된 노드, 현재노드
        #print(dist)
        for next_node in table[current_node]:

            d = dist[current_node] + 1 #거리비교, 어차피 1이 더해지는건데 더 줄일 수 없을까?
            #print(current_node+1, next_node+1)
            if d < dist[next_node]: #노드를 통한 거리 < 거리저장소 => 거리저장소에 저장
                dist[next_node] = d
                heapq.heappush(queue, next_node) # 그 노드들은 큐에 삽입
    
    return dist.count(max(dist))