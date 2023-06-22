def solution(arr):
    stack = []
    for i in arr:
        stack.append(i)
        if len(stack) > 1:
            if stack[-2] == stack[-1]:
                stack.pop()
    return stack