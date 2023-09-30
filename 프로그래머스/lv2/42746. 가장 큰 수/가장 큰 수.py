# from itertools import permutations
# def solution(numbers):
#     m = 0
#     for i in list(permutations(numbers, len(numbers))):
#         s = ''
#         for j in range(len(numbers)):
#             s += str(i[j])
#             m = max(int(s), m)
#     return str(m)

def solution(numbers):
    if max(numbers) == 0:
        return "0"
    numbers = list(map(lambda x:str(x)*3,numbers))
    numbers.sort(reverse=True)

    return ''.join(map(lambda x:x[:len(x)//3],numbers))