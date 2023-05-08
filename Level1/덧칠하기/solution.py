def solution(n, m, section):
    answer = 1
    i = 0    
    while section[-1] - section[i] + 1 > m:
        answer += 1
        j = i
        while section[i+1] - section[j] + 1 <= m:
            i += 1
        i += 1
    return answer
