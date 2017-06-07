def solution(A):
    N = len(A)
    for i in xrange(N // 2):
        j = N - i - 1
        A[i], A[j] = A[j], A[i]
    return A


print(solution([i for i in range(1, 11)]))
