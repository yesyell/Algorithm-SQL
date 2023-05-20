def solution(k, score):
    answer = []
    l = []
    for s in score:
        l.append(s)
        if len(l) < k:
            answer.append(min(l))
        else:
            answer.append(min(sorted(l, reverse=True)[:k]))
    return answer
