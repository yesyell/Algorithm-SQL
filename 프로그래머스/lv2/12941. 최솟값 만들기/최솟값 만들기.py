def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for a in range(len(A)):
        answer += A[a] * B[a]
    return answer