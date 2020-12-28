def compare_digit(num1, num2):
    for i in range(len(num2)):
        if num1[i] != num2[i]:
            return i
    return(len(num2))

def solution(numbers):
    answer = ''
    strnumbers = []
    cnt = 0
    for i in numbers:
        strnumbers.append(str(i))
    strnumbers = sorted(strnumbers, reverse = True)
    
    for i in range(len(strnumbers)):
        if '0' in strnumbers[i] and strnumbers[i] != strnumbers[-1]: #0이 있으면서 리스트의 마지막이 아닐때
            same_digit = compare_digit(strnumbers[i], strnumbers[i+1])
            if len(strnumbers[i+1]) == same_digit or strnumbers[i][same_digit+1] < strnumbers[i+1][same_digit+1]:
                strnumbers.insert(i, strnumbers.pop(i+1))
    for i in strnumbers:
        answer += i
    
    return answer