# Find the minimal nucleotide from a range of sequence DNA.
def solution(S, P, Q):
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    N = len(S)
    Apref = [0] * (N + 1)
    Cpref = [0] * (N + 1)
    Gpref = [0] * (N + 1)
    
    for i in range(N):
        Apref[i+1] = Apref[i] + (1 if S[i] == 'A' else 0)
        Cpref[i+1] = Cpref[i] + (1 if S[i] == 'C' else 0)
        Gpref[i+1] = Gpref[i] + (1 if S[i] == 'G' else 0)
    
    result = []
    M = len(P)
    for i in range(M):
        start = P[i]
        end = Q[i]
        if Apref[end+1] - Apref[start] > 0:
            result.append(impact_factor['A'])
            continue
        elif Cpref[end+1] - Cpref[start] > 0:
            result.append(impact_factor['C'])
            continue
        elif Gpref[end+1] - Gpref[start] > 0:
            result.append(impact_factor['G'])
            continue
        else:
            result.append(impact_factor['T'])
            
    return result


S = "CAGCCTA" # and arrays P, Q such that:

P = [0] * 3
P[0] = 2
P[1] = 5
P[2] = 0

Q = [0] * 3
Q[0] = 4
Q[1] = 5
Q[2] = 6

# expected result: [2, 4, 1]
