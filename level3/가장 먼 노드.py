def solution(n, edge):
    answer = 0
    table = [[0 for i in range(n)] for j in range(n)]
    
    for x, y in edge:
        if x < y:
            table[x-1][y-1] = 1
        else:
            table[y-1][x-1] = 1
    
    lst = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 0:
                continue
            if lst[j] == 0:
                lst[j] = lst[i] + table[i][j]
        print(lst)
                
    return(lst.count(max(lst)))