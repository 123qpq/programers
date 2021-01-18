def solution(lines):
    answer = 0
    newlines = []
    for line in lines:
        time = line.split(' ')[1].split(':')
        finishsec = 60 * (60 * int(time[0]) + int(time[1])) + float(time[2])
        runtime = float(line.split(' ')[2][:-1])
        startsec = finishsec - runtime
        newlines.append([startsec, finishsec] + [startsec + i for i in range(1, 3) if runtime > i])
        
    for  pv in newlines:
        temp = 0
        for newline in newlines:
            for sec in newline:
                if pv[1] <= sec and sec < pv[1] + 0.999:
                    temp += 1
                    if answer < temp:
                        answer = temp
                    break

    return answer