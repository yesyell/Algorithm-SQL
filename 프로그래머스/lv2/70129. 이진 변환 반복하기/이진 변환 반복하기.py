def solution(s):
    n = 0
    sum = 0
    while s != '1':
        n += 1
        sum += s.count('0')
        s = bin(s.count('1'))[2:]
    return [n, sum]