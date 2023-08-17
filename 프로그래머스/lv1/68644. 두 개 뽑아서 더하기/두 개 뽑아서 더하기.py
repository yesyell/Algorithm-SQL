from itertools import combinations

def solution(numbers):
    l = []
    for i in list(combinations(numbers, 2)):
        l.append(sum(i))
    return sorted(list(set(l)))