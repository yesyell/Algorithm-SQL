n = int(input())
n_list = list(map(int, input().split(' ')))

m = int(input())
m_list = list(map(int, input().split(' ')))

from collections import Counter

counts = dict(Counter(n_list))
# print(counts)

answer = [str(counts[i]) if i in counts.keys() else '0' for i in m_list]
print(' '.join(answer))