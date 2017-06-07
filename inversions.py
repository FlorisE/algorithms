inversions = 0

def merge(A, p, q, r):
    n_1 = q - p
    n_2 = r - q + 1
    L = A[p:q]
    R = A[q:r+1]
    i = 0
    j = 0
    global inversions
    for k in range(p, r+1):
        if i == n_1:
            for l in range(j, n_2):
                k = k + 1
            break
        elif j == n_2:
            for l in range(i, n_1):
                k = k + 1
            break
        elif L[i] <= R[j]:
            i = i + 1
        else:
            j = j + 1
        if L[i] > R[j]:
            inversions += 1

def merge_sort(A, p, r):
    if p < r:
        q = ((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q+1, r)
A = [8, 7, 6, 5, 4, 3, 2, 1]
B = [4, 3, 2, 1]
#merge(A, 0, 4, 7)
merge_sort(A, 0, 7)
print A
print inversions
inversions = 0
merge_sort(B, 0, 3)
print B
print inversions
