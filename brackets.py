def solution(S):
    N = len(S)
    stack = [0] * N
    stack_counter = 0
    for i in range(N):
        if S[i] == '[':
            stack[stack_counter] = '['
            stack_counter += 1
        elif S[i] == ']':
            if stack_counter > 0 and stack[stack_counter-1] == '[':
                stack_counter -= 1
            else:
                return 0
        elif S[i] == '(':
            stack[stack_counter] = '('
            stack_counter += 1
        elif S[i] == ')':
            if stack_counter > 0 and stack[stack_counter-1] == '(':
                stack_counter -= 1
            else:
                return 0
        elif S[i] == '{':
            stack[stack_counter] = '{'
            stack_counter += 1
        elif S[i] == '}':
            if stack_counter > 0 and stack[stack_counter-1] == '{':
                stack_counter -= 1
            else:
                return 0
    return 1 if stack_counter == 0 else 0

# given S = "{[()()]}", the function should return 1 
# given S = "([)()]", the function should return 0
