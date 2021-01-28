def solution(begin, target, words):
    if target not in words:
        return 0
    graph = {}
    
    words.append(begin)
    for word in words:
        temp = []
        for j in words:
            cnt = len([x for x in range(len(word)) if word[x] == j[x]]) #위치도 같이 비교
            if cnt == len(begin) - 1: #한글자만 다른 경우 모음
                temp.append(j)
        graph[word] = set(temp) # 그래프 구축
    print(graph)
    
    queue = [(begin, [begin])]
    result = []
    
    while queue: #너비탐색
        n, path = queue.pop(0)
        if n == target:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))

    return min([len(x) for x in result]) - 1