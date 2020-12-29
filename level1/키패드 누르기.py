ltemp = 10
rtemp = 12

def checkhand(hand):

    if hand == 'left':
        return ('L')
    else:
        return ('R')

def usehand(i, save):
    global ltemp
    global rtemp

    llen = abs((ltemp // 3) - (i // 3)) + abs((ltemp % 3) - (i % 3))
    if rtemp % 3 == 0:
        rlen = abs((rtemp // 3 - 1) - (i // 3)) + 1
    else:
        rlen = abs((rtemp // 3) - (i // 3))
    
    if llen == rlen:
        if save == 'L':
            ltemp = i
            return ('L')
        else:
            rtemp = i
            return ('R')
    elif llen < rlen:
        ltemp = i
        return ('L')
    else:
        rtemp = i
        return ('R')


def solution(numbers, hand):
    save = checkhand(hand)
    answer = ''
    global ltemp
    global rtemp
    for i in numbers:
        if i == 0:
            answer += usehand(11, save)
        elif i % 3 == 1:
            ltemp = i
            answer += 'L'
        elif i % 3 == 0:
            rtemp = i
            answer += 'R'
        else:
            answer += usehand(i, save)
    return answer