def add_binary(A, B):
    C = []
    i = len(A)-1
    j = len(B)-1
    r = 0
    while i >= 0 or j >= 0:
        a = A[i] if i >= 0 else 0
        b = B[j] if j >= 0 else 0
        abr = a + b + r
        if abr == 0:
            C.insert(0, 0)
            r = 0
        elif abr == 1:
            C.insert(0, 1)
            r = 0
        elif abr == 2:
            C.insert(0, 0)
            r = 1
        else:
            C.insert(0, 1)
            r = 1
        i = i - 1
        j = j - 1
    return C

print(add_binary([1, 0, 0], []))
print(add_binary([1, 0, 1, 0], [1, 0, 1]))
