str = input()
result = ''
for s in str:
    if s.isupper():
        s = s.lower()
    else:
        s = s.upper()
    result += s
print(result)
# print(input().swapcase())
