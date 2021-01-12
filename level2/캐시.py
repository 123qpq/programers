def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for c in cities:
        c = c.lower()
        if cacheSize == 0:
            return len(cities) * 5
        elif c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        elif len(cache) >= cacheSize:
            cache.pop(0)
            cache.append(c)
            answer += 5
        else:
            cache.append(c)
            answer += 5
    return answer