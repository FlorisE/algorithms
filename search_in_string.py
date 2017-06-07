"""
Bla
"""
def search(needle, haystack):
    """
    Searches for needle inside haystack
    """
    N = len(haystack)
    M = len(needle)

    if M > N:
        return -1

    hashed = [0] * N
    preorder = [0] * (N+1)
    for i in xrange(N):
        hashed[i] = hash(haystack[i])
        preorder[i+1] = hashed[i] + preorder[i]
    print preorder
    needle_hash = 0
    for i in xrange(M):
        needle_hash += hash(needle[i])
    for i in xrange(M-1, N):
        print i, M
        if (preorder[i] - preorder[i - M]) == needle_hash:
            match = True
            for j in xrange(i-M, i):
                needle_index = j - i + M
                haystack_index = j
                print "haystack index", haystack_index, "item", haystack[haystack_index], "needle index", needle_index, "item", needle[needle_index]
                if haystack[haystack_index] != needle[needle_index]:
                    match = False
                    break
            if match:
                return i - M
    return -1
