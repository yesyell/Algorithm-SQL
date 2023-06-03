import collections

def solution(A, B):
    if A == B:
        return 0
    cp = collections.deque(A)
    for i in range(len(A)):
        cp.rotate(1)
        if ''.join(cp) == B:
            return i + 1
    return -1
    # return (B*2).find(A)
