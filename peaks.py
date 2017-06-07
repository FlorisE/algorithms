def solution(A):
    N = len(A)
    if N < 3:
        return 0
    divisors = []
    peaks = set()
    # N
    for i in range(1, N-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.add(i)
    if len(peaks) == 0:
        return 0
    max_blocks = 1
    for i in range(2, N-1):
        if (N % i) == 0:
            size = N/i
            blocks = N/size
            fitted = 0
            for peak in sorted(peaks):
                if peak < (fitted + 1) * size and peak >= fitted * size:
                    fitted += 1
            if fitted == blocks:
                max_blocks = blocks
    return max_blocks


A = [0] * 12
A[0] = 1
A[1] = 2
A[2] = 3
A[3] = 4
A[4] = 3
A[5] = 4
A[6] = 1
A[7] = 2
A[8] = 3
A[9] = 4
A[10] = 6
A[11] = 2

# expected result: 3
