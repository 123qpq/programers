def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if len(citations) - idx <= citation:
            return len(citations) - idx
    return 0