def solution(cacheSize, cities):
    answer = 0
    cache = {}
    citiess = []
    if len(cities) == 0:
        return 0
    
    for c in cities:
        citiess.append(c.lower())
    
    for c in citiess:
        if c in cache:
            cache[c] += 1
            answer += 1
        elif len(cache) >= cacheSize and cacheSize != 0:
            for k, v in cache.items():
                if v == cache[min(cache)]:
                    del cache[k]
                    break
            cache[c] = 1
            answer += 5
        else:
            cache[c] = 1
            answer += 5
    
    return answer