import heapq
def solution(n, costs):
    
    total_cost = 0
    nodes = {i:[] for i in range(n)}
    
    for x, y, z in costs:
        nodes[x].append((z, y))
        nodes[y].append((z, x))
    
    connected = [0]
    candidate = nodes[0]
    heapq.heapify(candidate)
    
    while candidate:
        cost, y = heapq.heappop(candidate)
        
        if y not in connected: #사이클이 생기지 않으면
            connected.append(y) #새 노드 연결
            total_cost += cost #연결값 반영
            
            for n in nodes[y]: #다음노드에서 이어갈 수 있는 노드들
                if n[1] not in connected: #만약 그 다음노드들이 사이클을 만들지 않으면
                    heapq.heappush(candidate, n) #힙에 추가한다
    
    return total_cost