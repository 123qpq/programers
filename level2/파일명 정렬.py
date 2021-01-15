import re
def solution(files):
    answer = []
    refiles=[]
    for file in files:
        num = re.findall("\d+", file)[0]
        idx = file.find(num)
        refiles.append((file[:idx], num, file[idx+len(num):]))

    refiles.sort(key = lambda x: (x[0].lower(), int(x[1])))
    return list(map(lambda x: "".join(x), refiles))