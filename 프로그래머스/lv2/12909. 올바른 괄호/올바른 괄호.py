def solution(s):
    a = 0
    for k in s:
        if k =='(':
            a += 1
        else:
            a -= 1
        if a == -1:
            return False
    if a > 0:
        return False
    return True