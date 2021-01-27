import heapq
def solution(jobs):
    answer = 0
    heap = []
    jobs = sorted(jobs)
    t1 = jobs[0][0] #현재시간
    
    for job in jobs:
        if job[0] <= t1: #현재시간보다 일찍 요청한 애들 저장
            heapq.heappush(heap, (job[1], job[0]))
        elif len(heap) != 0: # 막혔을 경우 요청1개 처리함
            temp = heapq.heappop(heap)
            answer += abs(t1 - temp[1]) + temp[0] #현재시간-요청시간+처리시간
            t1 += temp[0] #처리 소요시간을 현재시간에 적용
            heapq.heappush(heap, (job[1], job[0])) #else문으로 빠지며 실행못한 부분 보충
    
    while len(heap) != 0: #for문으로 요청을 다 받더라도 수행되지 못한 요청들이 있을 수 있으므로 처리
            temp = heapq.heappop(heap)
            answer += t1 - temp[1] + temp[0]
            t1 += temp[0]

    return answer // len(jobs)