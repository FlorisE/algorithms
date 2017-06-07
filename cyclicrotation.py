def solution(A, K):
    N = len(A)
    if N == 0: return []
    
    tempA = [0] * N
    shift = K % N
    for i in range(N):
        tempA[i] = A[(i-shift) % N]
    return tempA


