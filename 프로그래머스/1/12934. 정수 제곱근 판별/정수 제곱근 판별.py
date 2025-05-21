def solution(n):
    if n == int(n**(1/2))**2:
        return (n**(1/2)+1)**2
    return -1