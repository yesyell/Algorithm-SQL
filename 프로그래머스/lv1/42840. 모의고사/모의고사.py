def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    collects = [0,0,0]
    result = []
   
    for i, answer in enumerate(answers):
        if s1[i % len(s1)] == answer:
            collects[0] += 1
        if s2[i % len(s2)] == answer:
            collects[1] += 1
        if s3[i % len(s3)] == answer:
            collects[2] += 1
            
    for i in range(len(collects)):
        if max(collects)==collects[i]:
            result.append(i+1)
   
    return result