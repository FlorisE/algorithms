# Find value that occurs in odd number of elements.
def solution(A):
    found = set()
    for a in A:
        if a in found:
            found.remove(a)
        else:
            found.add(a)
    return found.pop()

A = [0] * 7
A[0] = 9
A[1] = 3
A[2] = 9
A[3] = 3
A[4] = 9
A[5] = 7
A[6] = 9
# expected result: 7
