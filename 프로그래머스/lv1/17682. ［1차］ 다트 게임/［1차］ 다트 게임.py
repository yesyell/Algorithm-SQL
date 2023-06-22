import re

def solution(dartResult):
    result = []
    pattern = re.compile(r'(10|[0-9])([SDT])([*#]?)')
    
    for i, j, k in pattern.findall(dartResult):
        if j == 'S':
            n = int(i)
        elif j == 'D':
            n = int(i)**2
        elif j == 'T':
            n = int(i)**3
        if k == '*':
            n *= 2
            if len(result) > 0:
                result[-1] *= 2
        elif k == '#':
            n *= -1
        result.append(n)
        
    return sum(result)