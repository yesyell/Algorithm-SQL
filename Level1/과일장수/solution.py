def solution(k, m, score):
    answer = 0
    score_s = sorted(score, reverse=True)
    for i in range(0, len(score), m):
        if len(score) >= i+m:
            k = min(score_s[i:i+m])
            answer += k * m
    return answer
