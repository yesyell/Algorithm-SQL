def solution(players, callings):
    answer = []
    answer.extend(players)
    for calling in callings:
        i = answer.index(calling)
        answer[i-1], answer[i] = answer[i], answer[i-1]
    return answer
