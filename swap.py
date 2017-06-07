def solution(A, B, m):
    N = len(A) # assume len(A) == len(B)
    sA = sum(A)
    sB = sum(B)
    for i in xrange(N):
        for j in xrange(N):
            if sA - A[i] + B[j] == sB - B[j] + A[i]:
                return A[i], B[j]
    return None

print(solution([1, 2, 3, 4, 11], [-1, 2, 3, 4, 9], 9))
