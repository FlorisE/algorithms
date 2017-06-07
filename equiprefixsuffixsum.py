def solution(A):
    N = len(A)
    if N == 0:
        return -1
    left = 0
    right = 0
    for i in range(N):
        right += A[i]
    for i in range(0, N):
        if i != 0:
            left += A[i-1]
        right -= A[i]
        if left == right:
            return i
    return -1

A = [0] * 8
A[0] = -1
A[1] =  3
A[2] = -4
A[3] =  5
A[4] =  1
A[5] = -6
A[6] =  2
A[7] =  1

# expected result: 1, 3, or 7
