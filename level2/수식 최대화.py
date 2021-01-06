import re
import copy
from itertools import permutations

def solution(expression):
    answer = 0
    signs = list(permutations(list(set(re.findall("\D", expression)))))
    expression = re.split("(\W)", expression)
    for sign in signs:
        exp = copy.deepcopy(expression)
        for s in sign:
            for idx, i in enumerate(exp):
                if idx == 0:
                    continue
                if i == '-' and s == i:
                    exp[idx-1] = - int(exp.pop(idx+1)) + int(exp.pop(idx-1))
                    exp.insert(0, 0)

                if i == '+' and s == i:
                    exp[idx-1] = int(exp.pop(idx+1)) + int(exp.pop(idx-1))
                    exp.insert(0, 0)

                if i == '*' and s == i:
                    exp[idx-1] = int(exp.pop(idx+1)) * int(exp.pop(idx-1))
                    exp.insert(0, 0)

        if answer < abs(int(exp[-1])):
            answer = abs(int(exp[-1]))
    return answer