import heapq
def solution(n, edge):
    answer = 0
    table = [[0 if i == j else n+1 for i in range(n)] for j in range(n)]
    
    for x, y in edge: #인접행렬 생성
            table[x-1][y-1] = 1
            table[y-1][x-1] = 1
    
    dist = [0] + [n+1 for i in range(n-1)] #거리저장소
    queue = []
    heapq.heappush(queue, [table[0], 0]) #큐에 첫 노드 저장
    
    while queue: # 큐 탐색
        current_distance, current_destination = heapq.heappop(queue) #현재노드에서의 거리와 위치
        
        for new_destination, new_distance in enumerate(table[current_destination]):
            if new_distance == 0 or new_distance == n+1: #0이거나 inf 값 건너뛰기
                continue
            d = dist[current_destination] + new_distance #거리비교
            
            if d < dist[new_destination]: #노드를 통한 거리 < 거리저장소 => 거리저장소에 저장
                dist[new_destination] = d
                heapq.heappush(queue, [table[new_destination], new_destination]) # 그 노드들은 큐에 삽입
    
    return dist.count(max(dist))