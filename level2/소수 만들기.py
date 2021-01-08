from itertools import combinations
def solution(nums):
    count = 0
    for num in list(map(sum, combinations(nums, 3))):
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            count += 1
    return count