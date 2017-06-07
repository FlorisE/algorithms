def solution(A):
    A_sorted = sorted(A)
    N = len(A)
    for i in range(N-2):
        P = A_sorted[i]
        Q = A_sorted[i+1]
        R = A_sorted[i+2]
        if P + Q > R and Q + R > P and R + P > Q:
            return 1
    return 0

A = [0] * 6
A[0] = 10
A[1] = 2
A[2] = 5
A[3] = 1
A[4] = 8
A[5] = 20
# expected result: 1

A = [0] * 4
A[0] = 10
A[1] = 50
A[2] = 5
A[3] = 1
# expected result: 0
