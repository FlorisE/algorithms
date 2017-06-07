# Compute number of integers divisible by k in range [a..b].

def solution(A, B, K):
    return B/K - max(0, (A-1)/K) + (1 if A == 0 else 0)

#  A = 6, B = 11 and K = 2, result = 3
