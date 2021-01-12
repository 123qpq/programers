def solution(msg):
    answer = []
    dic = {chr(a) : i+1 for i, a in enumerate(range(65, 91))}
    idx = 0
    for i in range(len(msg)): #3번조건 자동화
        if i < idx:
            continue
        word = msg[i] #검사 시작점 저장
        for j in range(i+1, len(msg)):
            temp = word + msg[j]
            if temp not in dic: #최대 검사가능문자에 도달하면
                answer.append(dic[word]) #최대 문자의 사전값 저장
                dic[temp] = max(dic.values()) + 1 #없는 부분은 딕셔너리 추가작업
                idx = j
                break
            word += msg[j] #최대 검사가능문자에 도달 못했다면 for 돌림
        else: #만약 끝까지 돌았다면 그냥 탈출하면 됨
            break
    answer.append(dic[msg[idx:]])
    return answer