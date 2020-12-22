def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)]

    for truck in truck_weights:
        while sum(bridge) - bridge.pop(0) + truck > weight:
            bridge.append(0)
            answer += 1
            
        bridge.append(truck)
        answer += 1

    answer += bridge_length
    return answer