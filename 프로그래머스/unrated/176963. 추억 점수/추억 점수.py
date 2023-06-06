def solution(name, yearning, photo):
    answer = []
    name_yearning = {}
    for i in range(len(name)):
        name_yearning[name[i]] = yearning[i]
    for i in photo:
        sum_num = 0
        for j in name_yearning:
            if j in i:
                sum_num += name_yearning[j]
        answer.append(sum_num)
    return answer