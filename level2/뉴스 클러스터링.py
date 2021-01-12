from collections import Counter
def solution(str1, str2):
    str1 = Counter([str1[i:i+2].lower() for i in range(0, len(str1) -1) if str1[i:i+2].isalpha()])
    str2 = Counter([str2[i:i+2].lower() for i in range(0, len(str2) -1) if str2[i:i+2].isalpha()])
    if sum((str1&str2).values()) == 0 and sum((str1|str2).values()) == 0:
        return 65536
    return int(sum((str1&str2).values()) / sum((str1|str2).values()) * 65536)