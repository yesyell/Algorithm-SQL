def solution(sizes):
    max_s = 0
    min_l = []
    for size in sizes:
        if max(size) > max_s:
            max_s = max(size)
        min_l.append(min(size))
    return max_s * max(min_l)