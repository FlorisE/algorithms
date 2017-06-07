from math import sqrt

def solution(A):
    N = len(A)
    if N < 3:
        return 0
    
    peaks = []
    for i in range(1, N-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
    
    num_peaks = len(peaks)
    if num_peaks < 2:
        return num_peaks
    
    distance = peaks[num_peaks-1] - peaks[0]
    max_possible_flags = num_peaks + 1
    max_flags = 2
    
    for i in range(3, max_possible_flags):
        last_peak = peaks[0]
        fitted = 1
        for j in range(1, num_peaks):
            if peaks[j] - last_peak < i:
                continue
            last_peak = peaks[j]
            fitted += 1
            if fitted == i:
                max_flags = i
                break
        if fitted != i:
            break
    
    return max_flags


A = [0] * 12
A[0] = 1
A[1] = 5
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

# expected return value: 3
