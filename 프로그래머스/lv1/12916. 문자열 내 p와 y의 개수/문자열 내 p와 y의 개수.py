from collections import Counter
def solution(s):
    c = Counter(s.lower())
    return True if c['p']==c['y'] else False