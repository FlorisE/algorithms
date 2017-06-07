def solution(N):
    i = 1
    candidates = []
    while i * i <= N:
        if N % i == 0:
            candidates.append(i)
        i += 1
    return 2 * candidates[len(candidates)-1] + 2 * N / candidates[len(candidates)-1]

# example: N=30 -> result=22
