def solution(n):
    return list(filter(lambda x: '3' not in str(x), 
                       (filter(lambda x:x%3!=0, range(1000)))))[n-1]
