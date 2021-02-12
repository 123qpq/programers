def solution(n, costs):
    
    table = [[0 if i == j else -1 for i in range(n)] for j in range(n)]
    p = 1
    answer = 0
    lands = [0]
    
    for x, y, z in costs: #인접행렬 생성
            table[x][y] = z
            table[y][x] = z
    
    for t in table:
        print(t)
        
    while len(lands) != n:
        
        for land in lands:
            if p in table[land] and table[land].index(p) not in lands:
                lands.append(table[land].index(p))
                answer += p
        print(lands)
        p += 1
        break
    return answer