def solution(survey, choices):
    answer = ''
    data = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for k, v in zip(survey, choices):
        if v > 4:
            data[k[1]] += v-4
        else: 
            data[k[0]] += 4-v
            
    keys = list(data.keys())
    for i in range(0, len(keys)-1, 2):
        if data[keys[i]] >= data[keys[i+1]]:
            answer += keys[i]
        else: answer += keys[i+1]
    return answer