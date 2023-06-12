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
    
def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    if answer == '' :
        return '-1'
    elif answer[0] == '0':
        return '0'
    else :
        return answer