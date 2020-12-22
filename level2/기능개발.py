def solution(progresses, speeds):
    answer = []
    while progresses:
        progresses = [i + j for i, j in zip(progresses, speeds)]
        cnt = 0
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        answer.append(cnt)
    return [i for i in answer if i != 0]