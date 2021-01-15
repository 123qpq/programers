from itertools import permutations
from math import sqrt
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    size = len(numbers)
    numlist = []
    
    for i in range(1, size + 1):
        for j in permutations(numbers, i):
            j = "".join(j)
            if j[0] == '0' or j[-1] == '0' or j in numlist:
                continue
            numlist.append(j)

    for num in numlist:
        num = int(num)
        if num == 2 or num == 3: answer += 1
        if num >= 4:
            for i in range(2, int(sqrt(num))+1):
                if num % i == 0:
                    break
                if i == int(sqrt(num)):
                    answer += 1
                    break

    return answer