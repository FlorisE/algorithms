def solution(A):
    N = len(A)
    for i in range(N):
        A[i] = abs(A[i])
    s = set(A)
    return len(s)

A = [0] * 6
A[0] = -5
A[1] = -3
A[2] = -1
A[3] =  0
A[4] =  3
A[5] =  6

# Expected result: 5
