def solution(s):
    answer = 0
    double = s*2
    for i in range(len(s)):
        string = double[i:i+len(s)]
        stack = []
        for j in string:
            stack.append(j)
            if len(stack) > 1:
                if (stack[-2]=='(' and stack[-1]==')') or (stack[-2]=='{' and stack[-1]=='}') or (stack[-2]=='[' and stack[-1]==']'):
                    stack.pop()
                    stack.pop()
        if stack == []:
            answer += 1
    return answer