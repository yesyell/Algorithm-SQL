def solution(s):
    answer = []
    d = {}
    for i in s:
        l = list(filter(lambda x: s[x] == i, range(len(s))))
        p = -1
        if i in d:
            p = d[i][1] - d[i][0]
            if len(d[i]) > 2:
                l = d[i][1:]
        d[i] = l
        answer.append(p)
    return answer
