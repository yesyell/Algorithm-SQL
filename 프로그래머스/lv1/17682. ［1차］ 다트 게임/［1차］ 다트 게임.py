import re

def solution(dartResult):
    answer = []
    for i, j, k in re.findall(r'(10|[0-9])([SDT])([*#]?)', dartResult):
        print(i, j, k)
        if j == 'S':
            n = int(i)
        elif j == 'D':
            n = int(i)**2
        elif j == 'T':
            n = int(i)**3
        if k == '*':
            n *= 2
            if len(answer) > 0:
                answer[-1] *= 2
        elif k == '#':
            n *= -1
        answer.append(n)
    return sum(answer)