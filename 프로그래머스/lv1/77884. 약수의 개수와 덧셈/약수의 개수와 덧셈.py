def solution(left, right):
    s = 0
    ll = []
    for i in range(left, right+1):
        l = []
        for j in range(1, i+1):
            if i % j == 0:
                l.append(j)
        s = i
        if len(l) % 2 != 0:
            s *= -1
        ll.append(s)
    return sum(ll)