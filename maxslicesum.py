def solution(A):
    local_max_slice = 0
    global_max_slice = -1 * 10**9
    for a in A:
        local_max_slice = max(-1 * 10**9, local_max_slice+a, a)
        global_max_slice = max(global_max_slice, local_max_slice)
    return global_max_slice

A = [0] * 5
A[0] = 3  
A[1] = 2  
A[2] = -6
A[3] = 4  
A[4] = 0
# expected result: 5
