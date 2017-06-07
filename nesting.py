def solution(S):
    N = len(S)
    stack_counter = 0
    for i in range(N):
        if S[i] == '(':
            stack_counter += 1
        else:
            if stack_counter == 0:
                return 0
            stack_counter -= 1
    return 1 if stack_counter == 0 else 0

# S = "(()(())())", expected result: 1 
# S = "())", expected result: 0
