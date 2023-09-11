from collections import Counter
def solution(s):
    return Counter(s.lower())['p']==Counter(s.lower())['y']
    # return s.lower().count('p') == s.lower().count('y')
