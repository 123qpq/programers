def solution(N, number):
    if N == 1:
        return number if number <= 8 else -1
    lst = [0]
    for i in range(1, N):
        lst.append(i+1)
    lst.append(1)
    print(lst)
    print(number//N, number%N)
    
    answer = 0
    return answer