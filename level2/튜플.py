def solution(s):
    answer = []
    lst = []
    s = s.split("},")
    for x in s:
        lst.append(x.replace('{', '').replace('}',''))
    lst.sort(key = lambda x : len(x))
    for l in lst:
        temp = map(int, l.split(','))
        for x in temp:
            if x not in answer:
                answer.append(x)
    return answer