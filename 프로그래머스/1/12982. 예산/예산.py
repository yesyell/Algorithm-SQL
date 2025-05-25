def solution(d, budget):
    d.sort()
    print(d)
    for i in range(len(d), -1, -1):
        if sum(d[:i]) <= budget:
            return i
