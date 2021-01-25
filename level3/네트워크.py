def solution(n, computers):
    lst= []
    for computer in computers:   
        temp = list(filter(lambda x: computer[x] == 1, range(len(computer))))
        
        for i in range(len(lst)):
            if set(lst[i]) & set(temp):
                lst[i] = list(set(lst[i]) | set(temp))
                print(lst[i])
                break
        else:
            lst.append(temp)

    return len(lst)