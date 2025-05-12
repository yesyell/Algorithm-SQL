from collections import Counter

def solution(progresses, speeds):
    
    remains = [int(100-i) for i in progresses]
    stack = []
    
    r, s = remains[0], speeds[0]
    answer = [r//s if r%s==0 else r//s+1]
    
    for r, s in zip(remains, speeds):
        n = r//s if r%s==0 else r//s+1
        stack.append(n)
        
        if len(stack) > 1:
            if stack[-2] > stack[-1]: # 누적
                answer.append(stack[-2])
                stack.pop()
            else: # 배포
                # stack.pop(0)
                answer.append(stack[-1])

    return list(Counter(answer).values())