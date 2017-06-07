def ways(n):
    if n == 0:
        return 
    memo = {}
    # create base cases
    for i in xrange(1, min(7, n+1)):
        memo[i] = 2**(i-1)
    #if n < 7: return memo[n]
    for i in range(7, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3] + memo[i-4] + memo[i-5] + memo[i-6]
    return memo[n]
