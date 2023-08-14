def solution(n):
    answer = 0
    x = 0
    l = []
    while True:
        x = n % 3
        l.append(x)
        n = n // 3
        if n == 0:
            break
    ll = len(l)-1
    for i in l:
        answer += i * 3 ** ll
        ll -= 1
        print(answer)
    return answer