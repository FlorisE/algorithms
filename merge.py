def merge(A, p, q, r):
    print "Merge (p: " + str(p) + ", q: " + str(q) + ", r: " + str(r) + "): " + str(A)
    n_1 = q - p
    n_2 = r - q + 1
    L = A[p:q]
    R = A[q:r+1]
    i = 0
    j = 0
    for k in range(p, r+1):
        if i == n_1:
            for l in range(j, n_2):
                A[k] = R[l]
                k = k + 1
            break
        elif j == n_2:
            for l in range(i, n_1):
                A[k] = L[l]
                k = k + 1
            break
        elif L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    print "Merged: " + str(A)

def merge_sort(A, p, r):
    if p < r:
        q = ((p+r)/2)
        #print "p: " + str(p) + ", q: " + str(q) + ", r: " + str(r)
        #print "Merge sort: " + str(A[p:r+1])
        #print "Left: " + str(A[0:q+1])
        #print "Right: " + str(A[q+1:r+1])
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q+1, r)
A = [8, 7, 6, 5, 4, 3, 2, 1]
#merge(A, 0, 4, 7)
merge_sort(A, 0, 7)
print(A)
