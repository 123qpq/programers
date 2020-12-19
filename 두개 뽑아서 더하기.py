def solution(numbers):
    answer = []
    lenn = len(numbers)
    for i in range(lenn-1):
        for j in range(i + 1, lenn):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    return sorted(answer)