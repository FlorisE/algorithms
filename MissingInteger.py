def solution(A):
    N = len(A)
    count = [0] * N
    for i in range(N):
        if A[i] > 0 and (A[i]-1) < N:
            count[A[i]-1] += 1
    for c in range(N):
        if count[c] == 0:
            return c+1
    return N+1

A = [0] * 6
A[0] = 1
A[1] = 3
A[2] = 6
A[3] = 4
A[4] = 1
A[5] = 2
# expected result: 5
