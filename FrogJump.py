# Count minimal number of jumps from position X to Y.

from math import ceil

def solution(X, Y, D):
    return int(ceil((Y - X) / float(D))) 

X = 10
Y = 85
D = 30
# expected result: 3
