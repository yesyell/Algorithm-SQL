def solution(n):
    i = (n**(1/2)+1)**2
    return i if int(i)==i else -1