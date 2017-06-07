# Find longest sequence of zeros in binary representation of an integer.
def solution(N):
    binStr = "{0:b}".format(N)
    maxBinGap = 0
    currentBinGap = 0
    for c in binStr:
        if c == '0':
            currentBinGap += 1
        else:
            maxBinGap = max(maxBinGap, currentBinGap)
            currentBinGap = 0
    return maxBinGap


# given N = 1041 the function should return 5
