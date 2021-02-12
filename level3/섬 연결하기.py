def solution(n, costs):
    
    table = [[99 for i in range(n)] for j in range(n)]
    p = 1
    answer = 0
    lands = [0]
    
    for x, y, z in costs: #인접행렬 생성
            table[x][y] = z
            table[y][x] = z
    
    for t in table:
        print(t)
    print()
    #while len(lands) != n:
    for i in range(n):
        temp = [99 for i in range(n)]
        for land in lands:
            m = min(table[land])
            temp[table[land].index(m)] = min(m, temp[table[land].index(m)])#정복한 땅에서 갈 수 있는 최소값 잡아냄
        #과거에 있던 값이 덮어씌워지는 오류가 있음. 최저값이 제대로 안잡힌다.
        print(temp)
        x = temp.index(min(temp))
        print(land, x, m, lands)
        if x not in lands:
            lands.append(x)
            table[land][x] = 99
            table[x][land] = 99
            answer += m
        if len(lands) == n:
            break

    print(lands)


    return answer