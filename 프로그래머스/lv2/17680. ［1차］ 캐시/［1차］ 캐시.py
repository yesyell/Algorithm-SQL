from collections import deque
def solution(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache: # hit
            answer += 1
            cache.remove(city)
            cache.append(city)
        else: # miss
            cache.append(city)
            answer += 5
    return answer