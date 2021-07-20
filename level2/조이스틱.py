def solution(name):
    answer = 0
    
    check = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
        
    idx = 0

    while True:
        answer += check[idx]
        check[idx] = 0
        
        if sum(check) == 0:
            return answer
        
        left, right = 1, 1
        while check[idx - left] == 0:
            left += 1
            
        while check[idx + right] == 0:
            right += 1
        
        answer += left if left < right else right
        idx += -left if left < right else right
            