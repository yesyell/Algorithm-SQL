n = int(input())
nums = list(map(int, input().strip().split()))[:n]
answer = 0

nums.sort()
for i in nums:
    answer += n * i
    n -= 1
        
print(answer)