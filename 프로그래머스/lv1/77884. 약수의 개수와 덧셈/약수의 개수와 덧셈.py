def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        l = []
        for j in range(1, i+1):
            if i % j == 0:
                l.append(j)
        if len(l) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

    # for i in range(left, right+1):
    #     if int(i**0.5)==i**0.5: # 제곱수이면
    #         answer -= i
    #     else:
    #         answer += i
    # return answer