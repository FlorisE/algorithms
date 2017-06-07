# Count the number of passing cars on the road.
def solution(A):
    numEast = 0
    numWest = 0
    N = len(A)
    for i in range(N):
        if A[i] == 0:
            numEast += 1
        else:
            numWest += 1
    crossing = 0
    for i in range(N):
        if crossing > 1000000000: return -1
        if A[i] == 0:
            numEast -= 1
            crossing += numWest
        else:
            numWest -= 1
    return crossing

A = [0] * 5
A[0] = 0
A[1] = 1
A[2] = 0
A[3] = 1
A[4] = 1

# expected result: 5
