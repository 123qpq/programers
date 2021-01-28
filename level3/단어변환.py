def solution(begin, target, words):
    if target not in words:
        return 0
    graph = {}
    
    words.append(begin)
    for word in words:
        temp = []
        for j in words:
            cnt = len([x for x in word if x in j])
            if cnt == len(begin) - 1: #한글자만 다른 경우 모음
                temp.append(j)
        graph[word] = set(temp) # 그래프 구축
    print(graph)
    
    visited = []
    stack = [begin]
    
    while stack: #깊이탐색
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
            print(stack, visited)
        if target in stack:
            print(visited)
            return len(visited)

    return 0