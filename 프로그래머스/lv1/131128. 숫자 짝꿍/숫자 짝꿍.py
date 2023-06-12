# def solution(X, Y):
#     s = ''
#     for x in X:
#         if x in Y:
#             s += x
#             Y = Y.replace(x, '', 1)
#     if not s:
#         return "-1"
#     s = ''.join(sorted(s, reverse=True))
#     if s[0] == "0":
#         return "0"
#     else: 
#         return s
    
from collections import Counter

def solution(X, Y):
    char_count_X = Counter(X)
    char_count_Y = Counter(Y)
    common_chars = []
    
    for char in char_count_X:
        count = min(char_count_X[char], char_count_Y[char])
        common_chars.extend([char] * count)
    
    if not common_chars:
        return "-1"
    
    common_chars.sort(reverse=True)
    result = ''.join(common_chars)
    
    if result[0] == '0':
        return "0"
    else:
        return result