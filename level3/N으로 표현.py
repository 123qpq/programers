def solution(N, number):
    a = []
    lst = [[11, 11, 1, 1, 1, 1], [11, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
    '''
    if number == N:
        return 1
    for i in range(10922, 255, -1):
        temp = list(filter(None, (bin(i)[2:] + '1').split('0')))
        if temp not in lst and ''.join(temp).count('1') == 8:
            lst.append(temp)
            #print(temp)
    '''
    for i in lst:
        search = [N]
        answer = 1
        for j in i:
            answer += len(str(j))
            add = list(map(lambda x : x + j*N, search))
            div = list(map(lambda x : x // (j*N), search))
            mul = list(map(lambda x : x * j*N, search))
            new = list(set(add + div + mul))
            if number in new:
                a.append(answer)
            else:
                search = new
    print(a)
    if len(a) != 0:
        return min(a)
    else:
        return -1
