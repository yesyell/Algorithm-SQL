def solution(n, m, section):
    answer = 1
    i = 0    
    while section[-1] - section[i] + 1 > m:
        answer += 1
        j = i
        k = i
        while section[j+1] - section[k] + 1 <= m:
            i += 1
            j += 1
        i += 1
    return answer
