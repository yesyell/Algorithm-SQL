import re

def solution(my_string):
    n = re.findall('[0-9]', my_string)
    return sum(map(int, n))
