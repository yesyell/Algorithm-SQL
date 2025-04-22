def solution(participant, completion):
    data = dict()
    hash_sum = 0
    
    for p in participant:
        data[hash(p)] = p
        hash_sum += hash(p)
    for c in completion:
        hash_sum -= hash(c)
    
    return data[hash_sum]