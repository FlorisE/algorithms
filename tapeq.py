
def solution(A):
    N = len(A)
    right = sum(A)
    left = 0
    minf = 100000
    mini = 0
    for i in xrange(N):
        left = left + A[i]
        right = right - A[i]
        tsum = abs(left - right)
        if tsum < minf:
            minf = tsum
            mini = i
    return minf

print(solution([3, 1, 2, 4, 3]))
