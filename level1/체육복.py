def solution(n, lost, reserve):
    answer = 0
    student = [1 for i in range(n)]
    for i in range(n):
        if i+1 in lost:
            student[i] -= 1
        if i+1 in reserve:
            student[i] += 1
            
    for i in range(1,n):
        if student[i] == 2 and student[i-1] == 0:
            student[i] = 1
            student[i-1] = 1
    for i in range(n-1):
        if student[i] == 2 and student[i+1] == 0:
            student[i] = 1
            student[i+1] = 1

    
    return student.count(1) + student.count(2)