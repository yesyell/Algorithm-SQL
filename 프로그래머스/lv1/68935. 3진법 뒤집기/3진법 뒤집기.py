def solution(n):
    answer = 0
    l = []
    while n:
        l.append(n % 3)
        n = n // 3
    ll = len(l)-1
    for i in l:
        answer += i * 3 ** ll
        ll -= 1
    return answer

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3
#         print(tmp)
#     return int(tmp, 3)