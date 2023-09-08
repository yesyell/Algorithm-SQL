def solution(arr, d):
    l = []
    for a in arr:
        if a % d == 0:
            l.append(a)
    return sorted(l) if l != [] else [-1]