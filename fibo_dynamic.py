def fibo(n):
    """ 
    returns the nth fibonacci number
    >>> fibo(10)
    55
    """
    def fibo_memo(n, seen):
        if n in seen:
            return seen[n]

        for i in range(2, n+1):
            seen[i] = seen[i-1] + seen[i-2]
        return seen[n]
    seen = {0: 0, 1: 1}
    return fibo_memo(n, seen)
