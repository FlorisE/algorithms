def solution(A):
    N = len(A)
    
    if N == 3: return A[0] * A[1] * A[2]

    A = sorted(A)
    numNegatives = 0
    for a in A:
        if a < 0:
            numNegatives += 1
        else:
            break
    
    # only negatives or only one negative: just multiply largest
    if numNegatives == N or numNegatives == 1:
        return A[N-3] * A[N-2] * A[N-1]
    # only one or two positives: multiply most negative times most positive
    elif numNegatives == N-1 or numNegatives == N-2:
        return A[0] * A[1] * A[N-1]
    # at least three positives:
    else:
        # if two most negative are larger than two penpositive, use negatives:
        if A[0] * A[1] > A[N-3] * A[N-2]:
            return A[0] * A[1] * A[N-1]
        # else just multiply the positives
        else:
            return A[N-3] * A[N-2] * A[N-1]

A = [0] * 6
A[0] = -3
A[1] = 1
A[2] = 2
A[3] = -2
A[4] = 5
A[5] = 6

# expected result: 60
