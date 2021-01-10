def solution(n, words):
    answer = []
    for idx, word in enumerate(words):
        if idx == 0 or word not in answer and answer[-1][-1] == word[0]:
            answer.append(word)
        else:
            return [len(answer) % n + 1, len(answer) // n + 1]
    return [0, 0]