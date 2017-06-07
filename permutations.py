from collections import defaultdict
from math import factorial

def permutations(S):
    N = len(S)
    counts = defaultdict(int)
    for i in range(N):
        counts[S[i]] += 1
    
    dups = 1
    for c in counts.values():
        dups *= factorial(c)

    return factorial(N) / dups

print permutations("123")
print permutations("122")
print permutations("1122")
print permutations("1112")
print permutations("1233")
print permutations("testing")
