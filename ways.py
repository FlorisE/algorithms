from collections import defaultdict

def ways(n):
    memo = defaultdict(list)
    for i in xrange(1, n+1):
        if i < 7:
            memo[i].append([i])
        for j in range(1, max(7, i)):
            for k in memo[i-j]:
                temp = [j]
                for l in k:
                    temp.append(l)
                memo[i].append(temp)
    return memo
