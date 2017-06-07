def solution(A):
    A_sorted = sorted(A)
    
    last = None
    counter = 0
    for a in A_sorted:
        if a != last:
            counter+=1
            last = a
    return counter

A = [0] * 6
A[0] = 2
A[1] = 1
A[2] = 1
A[3] = 2
A[4] = 3
A[5] = 1
# expected result: 3
