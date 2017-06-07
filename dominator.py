def solution(A):
    N = len(A)
    stack = [0] * N
    stack_counter = 0
    for i in range(N):
        stack[stack_counter] = A[i]
        stack_counter += 1
        if stack_counter == 1:
            continue
        if stack[stack_counter-1] != stack[stack_counter-2]:
            stack_counter -= 2
    if stack_counter == 0:
        return -1
    candidate = stack[stack_counter-1]
    counter = 0
    candidate_found_at = -1
    for i in range(N):
        if A[i] == candidate:
            counter += 1
            candidate_found_at = i
    if N/counter >= 2:
        return -1
    return candidate_found_at

A = [0] * 8
A[0] = 3
A[1] = 4
A[2] = 3
A[3] = 2
A[4] = 3
A[5] = -1
A[6] = 3
A[7] = 3
# expected result: 0, 2, 4, 6 or 7
