def solution(A, K):
    temp = [0] * len(A)
    for i in range(0, len(A)):
        temp[(i + K) % len(A)] = A[i]
    return temp

print(solution([3, 8, 9, 7, 6], 3))
