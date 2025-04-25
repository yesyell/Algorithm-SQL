from collections import Counter

def solution(clothes):
    count = Counter([category for _, category in clothes])
    
    multiple = 1
    for n in count.values():
        multiple *= (n+1)
    
    return multiple-1