# def solution(s):
#     a = 0
#     for k in s:
#         if k =='(':
#             a += 1
#         else:
#             a -= 1
#         if a == -1:
#             return False
#     return a == 0

def solution(s):
    st = []
    for c in s:
        if c == '(':
            st.append(c)
        else:
            try:
                st.pop()
            except IndexError:
                return False
    return len(st) == 0