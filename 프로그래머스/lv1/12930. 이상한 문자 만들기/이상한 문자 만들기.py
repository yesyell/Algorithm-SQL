def solution(s):
    word = s.split(' ')
    result = []
    for w in word:
        new = ''
        for i, a in enumerate(w):
            if i % 2 == 0:
                new += a.upper()
            else:
                new += a.lower()
        result.append(new)
    return ' '.join(result)