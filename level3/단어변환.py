def solution(begin, target, words):
    if target not in words:
        return 0
    comp = begin
    graph = []
    
    for word in words:
        temp = []
        cnt = len([x for x in begin if x in word])
        if cnt == 2:
            temp.append(word)
            words.remove(word)
        graph.append(temp)
                
    return 0