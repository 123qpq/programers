def solution(routes):
    answer = 0

    while len(routes) != 0:
        for i in range(2):
            temp = []
            a = routes[0][0]
            b = routes[0][1]
            for route in routes:

                if a <= route[0] <= b or route[0] <= a <= route[1] or \
                    a <= route[1] <= b or route[0] <= b <= route[1]:
                    a = route[0] if abs(a-b) > abs(route[0]-b) else a
                    b = route[1] if abs(b-a) > abs(route[1]-a) else b
                else:
                    temp.append(route)
            answer += 1
            routes = temp

    return answer