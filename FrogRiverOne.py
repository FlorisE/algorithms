# Find the earliest time when a frog can jump to the other side of a river.

def solution(X, A):
    fallen = [0] * X
    N = len(A)
    fsum = 0
    for i in range(N):
        fall = fallen[A[i]-1]
        if fall == 0:
            fallen[A[i]-1] = 1
            fsum += 1
        if fsum == X:
            return i
    return -1

X = 5
A = [0] * 8
A[0] = 1
A[1] = 3
A[2] = 1
A[3] = 4
A[4] = 2
A[5] = 3
A[6] = 5
A[7] = 4
# expected result: 6
