from itertools import combinations

def solution(numbers):
    l = []
    for i in list(combinations(numbers, 2)):
        if sum(i) not in l:
            l.append(sum(i))
    l = sorted(l)
    return l