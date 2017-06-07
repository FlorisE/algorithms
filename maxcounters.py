# Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.

def solution(N, A):
    counter = [0] * N
    max_counter = 0
    triggered_max = 0
    length = len(A)
    
    for i in range(length):
        a = A[i]
        if a == N + 1:
            triggered_max = max_counter
        else: 
            item = a-1
            if counter[item] < triggered_max:
                counter[item] = triggered_max
            counter[item] += 1
            max_counter = max(counter[item], max_counter)
            
    for i in range(N):
        if counter[i] < triggered_max:
            counter[i] = triggered_max
    return counter

N = 5
A = [0] * 7
A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4
# results in:
#(0, 0, 1, 0, 0)
#(0, 0, 1, 1, 0)
#(0, 0, 1, 2, 0)
#(2, 2, 2, 2, 2)
#(3, 2, 2, 2, 2)
#(3, 2, 2, 3, 2)
#(3, 2, 2, 4, 2) (final result)
