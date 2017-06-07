def solution(A):
    N = len(A)
    diff = [0] * N
    for i in range(1, N):
        diff[i] = A[i] - A[i-1]
    local_max = global_max = 0
    for i in range(N):
        local_max = max(0, local_max+diff[i])
        global_max = max(local_max, global_max)
    return global_max

A = [0] * 6
A[0] = 23171
A[1] = 21011
A[2] = 21123
A[3] = 21366
A[4] = 21013
A[5] = 21367

# expected result: 356
