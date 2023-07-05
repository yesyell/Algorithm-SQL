from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_lst.append(str1[i] + str1[i+1])

    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            str2_lst.append(str2[j] + str2[j+1])
    
    inter = list((Counter(str1_lst) & Counter(str2_lst)).elements())
    union = list((Counter(str1_lst) | Counter(str2_lst)).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)