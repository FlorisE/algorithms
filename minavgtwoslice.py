# Find the minimal average of any slice containing at least two elements.
def solution(A):
    N = len(A)
    P = [0] * (N + 1)
    for i in range(N):
        P[i+1] = P[i] + A[i]
    
    minimum = 100000
    index = 0
    for i in range(1, N):
        for j in range(i+1, min(N+1, i+3)):
            curr = (P[j] - P[i-1]) / float(j - i + 1)
            if curr < minimum:
                minimum = curr
                index = i-1
                
    return index

A = [0] * 7
A[0] = 4
A[1] = 2
A[2] = 2
A[3] = 5
A[4] = 1
A[5] = 5
A[6] = 8
# expected result: 1
