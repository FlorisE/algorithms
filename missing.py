def solution(A):
    N = len(A) + 1
    sN = N * (N + 1) / 2
    sA = sum(A)
    return sN - sA


print(solution([1, 6, 3, 4, 5, 7]))
